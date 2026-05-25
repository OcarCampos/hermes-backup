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

## Channel Registry

| Channel | ID | Purpose | Fields |
|---------|-----|---------|--------|
| SmartPlant (tent) | 2785218 | Vegetable tent monitoring | Temp, Hum, Lux, Soil Moisture |
| Tenvironment (Hell) | 2781694 | Polycarbonate hell space monitoring | Temperature, Humidity, Light Level |

**Tenvironment (Hell) channel:**
- **Channel ID:** 2781694
- **API Key (read):** SKWN0AM0TEWZQJ5H
- **Fields:** field1=Temperature, field2=Humidity, field3=Light Level
- **Live data:** https://thingspeak.mathworks.com/channels/2781698

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

## Standard Query (Single Result)

```bash
curl -s "https://api.thingspeak.com/channels/<CHANNEL_ID>/feeds.json?results=1"
```

## Query N Recent Results

```bash
curl -s "https://api.thingspeak.com/channels/<CHANNEL_ID>/feeds.json?results=<N>"
```

## Query Date Range (historical data pull)

Use `start=` to fetch data from a specific date onwards:
```bash
curl -s "https://api.thingspeak.com/channels/<CHANNEL_ID>/feeds.json?api_key=<KEY>&results=20000&start=2026-05-10%2000:00:00"
```
The `api_key` parameter is required for private channels. For public channels it's optional.

## Pitfalls

- **Field order is not guaranteed.** If SmartPlant v2 channel configuration changes (e.g., sensor moves to a different field), always re-fetch metadata before reporting values.
- **SmartPlant v2 uses calibrated percentage for soil moisture** (field4), not a raw ADC value.
- **Timestamps** are UTC in `created_at`. Convert to Chile local time (UTC-4) for context.

## Garden File Paths

Always use absolute paths when referencing garden files:

- Lemon Haze log: `/mnt/data/Developing/hermes-workspace/garden/lemon-haze.md`
- Vegetable Tent log: `/mnt/data/Developing/hermes-workspace/garden/vegetable-tent.md`
- Garden folder readme: `/mnt/data/Developing/hermes-workspace/garden/readme.md`
- SmartPlant v2: `/mnt/data/Developing/hermes-workspace/3dprinting/smartplant-v2.md`
- Hell (polycarbonate space) ThingSpeak data:
  - `/mnt/data/Developing/hermes-workspace/garden/hell/temperature.csv`
  - `/mnt/data/Developing/hermes-workspace/garden/hell/humidity.csv`
  - `/mnt/data/Developing/hermes-workspace/garden/hell/lux.csv`
  - Data range: 2026-05-14 to 2026-05-24 (992 readings per file)

## Tent Setup Reference (vegetable-tent.md)

- **Light:** Purple LED panel — switches: VEG / FULL SPECTRUM / BLOOM
- **Extractor Fan:** Synced to light timer
- **Circulation Fan:** 24/7
- **Light Cycle:** 20/4 for cannabis (vegetables share tent)
- **ThingSpeak:** Channel 2785218 — Field 1=Temp, Field 2=Hum, Field 3=Lux, Field 4=Soil Moisture (%)
- **Soil moisture sensor:** Capacitive soil moisture v1.2, calibrated % (not raw ADC)
- **Current tent conditions (May 2026):** ~21°C avg, 51% hum, 414 lux avg, 58% soil moisture
- **Lemon Haze:** Harvested Day 108 (25/05/2026) — grow log ended

## Cronjob Debugging & Fixing Workflow

When a cronjob fails to find files or produces wrong output:

1. **Cron prompts are stored in two places (always check both):**
   - `~/.hermes/cron/jobs.json` — truncated prompt (may be cut off)
   - `~/.hermes/sessions/session_cron_<JOB_ID>_<TIMESTAMP>.json` — full prompt with tool calls and tool results

2. **Find the right session:** Look for `session_cron_<job_id>_*` files sorted by timestamp. The most recent run has the full prompt that was actually executed.

3. **Key session file locations:**
   - Cron session logs: `~/.hermes/sessions/session_cron_<JOB_ID>_<TIMESTAMP>.json`
   - Cron output logs: `~/.hermes/cron/output/<JOB_ID>/<DATE>.md`
   - Cron job definitions: `~/.hermes/cron/jobs.json`

4. **Common cronjob file-finding failure:** Cronjobs that use bare filenames (`lemon-haze.md`) will fail when `OBSIDIAN_VAULT_PATH` is unset, because the agent looks in skill directories and home directory. Always use full absolute paths in cron prompts.

5. **Day counting off-by-one:** When creating cron prompts that compute day numbers (e.g., "Day N since sow date"), remember the formula is `(today - start_date + 1)`. Verify with concrete dates before finalizing the prompt.

## Relevant Files

- SmartPlant v2: `/mnt/data/Developing/hermes-workspace/3dprinting/smartplant-v2.md`
- Garden folder: `/mnt/data/Developing/hermes-workspace/garden/`
- Lemon Haze: `/mnt/data/Developing/hermes-workspace/garden/lemon-haze.md`
- Vegetable Tent: `/mnt/data/Developing/hermes-workspace/garden/vegetable-tent.md`
