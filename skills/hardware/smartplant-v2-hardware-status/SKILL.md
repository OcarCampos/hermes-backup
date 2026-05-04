---
name: smartplant-v2-hardware-status
description: SmartPlant v2 hardware inventory, "The Hell" deployment candidate, ThingSpeak conventions, and Lemon Haze deployment notes
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [smartplant, arduino, thingspeak, garden, cannabis, vegetables]
---

# SmartPlant v2 — Hardware & Deployment Status

## Hardware Inventory (as of May 2026)

| Component | Qty Owned | Status |
|---|---|---|
| Arduino Nano V3 CH340 | 2 | ✅ Have |
| ESP-01S WiFi | 2 | ✅ Aliexpress arrived Apr 20 |
| Mini560 DC-DC | 2 | ✅ |
| Capacitive soil sensor | 2 | ✅ |
| AHT10 temp/humidity | 2 | ✅ |
| TEMT6000 light | 2 | ✅ |
| ABS junction box | 2 | ✅ |
| Cable AWG 22 | ~1m | ⚠️ Dispute ongoing — only 1m received |

**Unit #1**: Assembled and deployed in vegetable tent (ThingSpeak channel active).
**Unit #2**: Spare — available for Hell deployment or replacement.

## "The Hell" — Winter Deployment Candidate

Polycarbonate-covered patio. Summer 38-39°C (useless). Winter conditions:
- Nights: 12–15°C
- Days: 20–25°C on sunny winter days
- Light: Natural diffuse via polycarbonate (excellent for leafy greens, no burning)
- Humidity: Ambient coastal ~50–65%
- Ventilation: Passive via ~90×60cm window
- Electronics risk: Condensation on electronics from morning dew; polycarbonate overhang protects top but sides exposed

**Why it's interesting**: Acts as passive solar trap in winter. Stays warmer than outside on cold nights. Could support coriander, lettuce, and larger plants moved from tent.

**Before permanent deployment**: 2–4 week characterization run with SmartPlant v2 to validate:
- Day/night temp swing inside vs outdoor
- Humidity behavior (condensation on polycarbonate?)
- Soil temp in planting medium
- Light levels at plant height
- Power availability confirmation needed

**Enclosure note**: ABS junction box is NOT IP-rated. Position under polycarbonate overhang. Add silica gel packet inside for condensation protection.

## ThingSpeak Monitoring — Key Convention

**vegetable-tent.md soil moisture field = Lemon Haze pot only**
Seed tray has NO sensor. Always clarify which metric when discussing readings.

## Lemon Haze Deployment

- Day 52 of life (flowering) as of May 2, 2026
- Sensor was stir+reinserted May 2 (moisture pooling below probe observed — redistribution effect on ThingSpeak expected)
- Nutrient feed May 2: 3ml/L Terra Flores, ~200ml surface + ~100ml sensor area
- Expect ThingSpeak soil spike then stabilization over 24–48h post-feed
