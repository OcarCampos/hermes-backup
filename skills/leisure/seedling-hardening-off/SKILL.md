---
name: seedling-hardening-off
description: Gradual 7-day outdoor transition protocol for tent seedlings in Concón Chile, with temperature/humidity thresholds for lettuce and coriander
---

# Seedling Hardening Off — Concón Chile

**When:** Seedlings in grow tent ready to move outdoors.  
**Goal:** Gradual 7-day transition to outdoor conditions without transplant shock.

---

## Hardening Off Protocol (7 Days)

| Days | Duration | Time Window | Sun | Notes |
|------|----------|-------------|-----|-------|
| 1–2 | 1–2 hrs | 9–11am | Shade | Acclimate to outdoor air temp |
| 3–4 | 3–4 hrs | 11am–2pm | Filtered/morning sun | Introduce direct light slowly |
| 5–7 | Full day | All daylight | Direct sun if temps OK | Overnight outside if >12°C |
| After day 7 | Permanent | — | Full outdoor | Monitor for wilting |

**Golden rule:** 2–3 true leaves before starting. Earlier = weak roots.

---

## Concón Winter Thresholds (June–August)

Use `curl -s "https://wttr.in/Conc%C3%B3n,Chile?format=j1"` for current forecast.

### Lettuce (Lechuga Morada 4 Estaciones)
- **Germination:** 15–22°C ideal | 10–28°C tolerable
- **Humidity:** 50–70%
- **Soil:** 70–80% moisture
- **Outdoor move:** Safe when outdoor min >10°C
- **Warning:** Heat stress above 24°C → can bolt prematurely

### Coriander (Cilantro)
- **Germination:** 15–25°C | tolerates 10–28°C
- **Humidity:** 60–70% ideal | 40–70% tolerable
- **Soil:** 65–80% moisture
- **Outdoor move:** Safe when outdoor min >8°C
- **Warning:** Dry air (RH <40%) in Concón afternoons stresses young seedlings — use dome or misting
- **Bolting risk:** Hot temps + long days → bolts fast. Move to shade in summer.

---

## Common Problems

| Symptom | Cause | Fix |
|---------|-------|-----|
| Wilting after moving out | Transplant shock | Move back to shade for 1–2 days |
| Slow growth after move | Root disturbance | Phosphorus-rich feed, keep moist |
| Soil still wet 3+ days after watering | Root rot / overwatering | Improve drainage, dry out before next water |
| Leggy seedlings | Not enough light | Move to brighter spot |
| Soil moisture sensor reading wet pocket | Water pooled below probe | Stir soil around probe, reinsert |

---

## File Reference
- `/mnt/data/Developing/hermes-workspace/garden/vegetable-tent.md` — active grow log
- `/mnt/data/Developing/hermes-workspace/garden/readme.md` — general garden reference
- `/mnt/data/Developing/hermes-workspace/3dprinting/smartplant-v2.md` — SmartPlant monitoring hardware

## ThingSpeak Live Data
Channel 2785218, Field 1=Temp, Field 2=Humidity, Field 3=Lux, Field 4=Soil Moisture %
