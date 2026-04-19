---
name: i2c-sensor-debug
description: Reverse-engineer I2C sensor data formats by dumping raw bytes and deriving the correct bit-layout formula from real sensor data. Use when an I2C sensor is detected but the conversion formula is unknown, wrong, or produces inconsistent results.
homepage: 
tags: [arduino, i2c, debugging, hardware, sensors]
metadata:
  hermes:
    tags: [arduino, i2c, debugging, hardware]
---

# I2C Sensor Debug — Raw Byte Reverse-Engineering

When an I2C sensor is detected (Wire scan works), returns garbage or wildly inconsistent values, and standard library code isn't giving correct results — reverse-engineer the data format from raw bytes.

## Workflow

### Step 1: Add raw byte debug output to the sketch

In the `readSensor()` function, print all raw bytes before any conversion:

```cpp
Wire.requestFrom(SENSOR_ADDRESS, NUM_BYTES);
for (int i = 0; i < NUM_BYTES; i++) {
    byte b = Wire.read();
    Serial.print(" b");
    Serial.print(i);
    Serial.print("=0x");
    Serial.print(b, HEX);
}
Serial.println();
```

### Step 2: Collect real data with known physical conditions

Run the sensor in a stable environment and collect 5-10 raw byte readings alongside the WRONG calculated values. Note the actual physical conditions (room temp ~20°C, humidity ~50%, etc.) so you have ground truth.

### Step 3: Derive the formula in Python

```python
# Template — replace with actual byte positions and sensor data
readings = [
    # (b0, b1, b2, b3, obs_temp, obs_humidity)
    (0x7D, 0x64, 0xD6, 0x37, 20.0, 49.0),
    # ... more readings
]

# Test humidity formula candidates
# Candidate A: b0 and upper nibble of b1 form humidity
hum_A = lambda b0, b1: ((b0 << 8) | (b1 >> 4))  # wrong
hum_B = lambda b0, b1: (((b0 << 12) | (b1 << 4)) & 0x0FFFFF)  # try this
hum_C = lambda b0, b1: ((b0 << 8) | (b1 & 0xF0))  # another variant

# Test temperature formula candidates
# Temperature is typically spread across multiple bytes
# b1 lower nibble + b2 + b3 upper nibble often form temp[19:0]
temp_A = lambda b1, b2, b3: (((b1 & 0x0F) << 16) | (b2 << 8) | (b3 & 0xF0))
temp_B = lambda b1, b2, b3: (((b1 & 0x0F) << 16) | (b2 << 4) | (b3 >> 4))  # wrong nibble

for b0, b1, b2, b3, obs_t, obs_h in readings:
    hum = hum_B(b0, b1) / 1048576.0 * 100.0
    temp = (temp_A(b1, b2, b3) / 1048576.0) * 165.0 - 45.0
    print(f"hum={hum:.1f}% obs={obs_h}% | temp={temp:.1f}°C obs={obs_t}°C")
```

### Step 4: Iterate formula variants until all readings match

Look for the formula where every reading matches the observed ground truth. The correct formula will give 0.0 error across all readings.

### Step 5: Verify in Arduino, then strip debug output

Once the formula works, verify on the actual hardware, then remove the raw byte debug prints.

---

## Known Corrected Sensor Formulas

### AHT10 / AHT20 (verified with real sensor, address 0x38)

**Data packet:** `[status][b1][b2][b3][b4][crc]`
- `b1` = humidity[19:12]
- `b2` upper nibble = humidity[11:8]; lower nibble = temperature[19:16]
- `b3` = temperature[15:8]
- `b4` upper nibble = temperature[7:4]; lower nibble = status/CRC bits (ignore)

```cpp
// Humidity: 20-bit from b1 (upper 8 bits) + b2 upper nibble (lower 4 bits)
uint32_t hum_raw = (((b1 << 12) | (b2 << 4)) & 0x0FFFFF);
float humidity = (hum_raw / 1048576.0) * 100.0;

// Temperature: 20-bit from b2 lower nibble + b3 + b4 upper nibble
uint32_t temp_raw = (((b2 & 0x0F) << 16) | ((b3) << 8) | (b4 & 0xF0));
float temperature = ((temp_raw / 1048576.0) * 165.0) - 45.0;
```

**Init sequence:**
1. Soft reset: `Wire.write(0xBA)`, delay 20ms
2. Init: `Wire.write(0xA8)`, delay 10ms
3. Trigger measurement: `Wire.write(0xAC)`, `Wire.write(0x33)`, `Wire.write(0x00)`, delay 80ms

**Notes:**
- Calibration bit (status & 0x08) confirms sensor is calibrated
- Busy bit (status & 0x80) — wait if set
- Status byte varies: 0x1C = calibrated and idle (confirmed on real AHT10)

---

## Pitfalls

- **b4 lower nibble:** The lower nibble of the 4th data byte contains status/CRC bits, NOT temperature data. Always mask with `& 0xF0`.
- **b2 lower vs upper nibble for temperature:** Temperature starts in the LOWER nibble of b2, NOT the upper. This is the most common mistake in AHT10 implementations.
- **Wire.write ordering:** Always call `Wire.endTransmission()` after the measurement trigger before calling `Wire.requestFrom()`.
- **Wrong formulas in tutorials:** Many Arduino AHT10 libraries use formulas that work for one batch of sensors but not others. If humidity is correct (~48-50%) but temperature is wrong (e.g., -40°C or 90°C), the bit layout is definitely swapped.
- **I2C cable length:** For extended cable runs (>20cm), add 4.7kΩ pull-up resistors between SDA and 5V, and SCL and 5V. Without them, I2C communication becomes marginal and readings will jump around or become inconsistent even with correct formulas.

## Verified Working AHT10 Init Sequence (18/04/2026)

```cpp
// Step 1: Soft reset
Wire.beginTransmission(AHT10_ADDRESS);
Wire.write(0xBA);
Wire.endTransmission();
delay(20);

// Step 2: Initialize
Wire.beginTransmission(AHT10_ADDRESS);
Wire.write(0xE1);
Wire.write(0x08);
Wire.write(0x00);
Wire.endTransmission();
delay(10);

// Step 3: Trigger first measurement to activate sensor
Wire.beginTransmission(AHT10_ADDRESS);
Wire.write(0xAC);
Wire.write(0x33);
Wire.write(0x00);
Wire.endTransmission();
delay(80);

// Step 4: Verify calibration bit (status & 0x08)
Wire.requestFrom(AHT10_ADDRESS, (uint8_t)1);
if (Wire.available() > 0) {
    byte s = Wire.read();
    if (s & 0x08) {
        Serial.println("[AHT10] Calibrated and ready");
    }
}
```

**Confirmed status bytes from real AHT10:**
- `0x1C` = calibrated and ready (normal idle after init)
- Busy flag: `s & 0x80` — if set, wait and retry the measurement
