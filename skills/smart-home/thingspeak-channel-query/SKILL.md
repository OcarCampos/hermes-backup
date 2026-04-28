---
name: thingspeak-channel-query
category: smart-home
description: Query ThingSpeak channels with correct field label discovery — never assume field order.
triggers:
  - "thingspeak"
  - "smartplant"
  - "read thingspeak"
  - "check tent conditions"
---

# ThingSpeak Channel Query

Query live data from a ThingSpeak channel and correctly map field labels.

## Always Fetch Channel Metadata First

ThingSpeak fields are NOT in a fixed order. Do NOT assume field1=temperature, field2=humidity, etc.  
**Always** fetch the channel metadata to get the actual field labels:

```bash
curl -s "https://api.thingspeak.com/channels/<CHANNEL_ID>/feeds.json?results=1" | python3 -c "
import json, sys
d = json.load(sys.stdin)
ch = d['channel']
feeds = d['feeds']
print('Channel:', ch['name'])
print('Fields:')
for f in ['field1','field2','field3','field4','field5','field6','field7','field8']:
    if ch.get(f):
        print(f'  {f}: {ch[f]}')
if feeds:
    print()
    print('Latest feed:')
    for f in ['field1','field2','field3','field4','field5','field6','field7','field8']:
        if feeds[-1].get(f) is not None:
            print(f'  {f} ({ch.get(f,\"\")}): {feeds[-1][f]}')
"
```

## SmartPlant Channel (O'car's)

- **Channel ID:** 2785218
- **URL:** https://thingspeak.mathworks.com/channels/2785218
- **Known field labels (verify against API — do not hardcode):**
  - Field 1 → Temperature (°C)
  - Field 2 → Humidity (%)
  - Field 3 → Lux (light)
  - Field 4 → Soil Moisture (%)

## Standard Query (Single Result)

```bash
curl -s "https://api.thingspeak.com/channels/<CHANNEL_ID>/feeds.json?results=1"
```

## Query N Recent Results

```bash
curl -s "https://api.thingspeak.com/channels/<CHANNEL_ID>/feeds.json?results=<N>"
```

## Pitfalls

- **Field order is not guaranteed.** If SmartPlant v2 channel configuration changes (e.g., sensor moves to a different field), always re-fetch metadata before reporting values.
- **SmartPlant v2 uses calibrated percentage for soil moisture** (field4), not a raw ADC value.
- **Timestamps** are UTC in `created_at`. Convert to Chile local time (UTC-4) for context.

## Relevant Files

- SmartPlant v2: `/mnt/data/Developing/hermes-workspace/3dprinting/smartplant-v2.md`
- Garden folder: `/mnt/data/Developing/hermes-workspace/garden/`
