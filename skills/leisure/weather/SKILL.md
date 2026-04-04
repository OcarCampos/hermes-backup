---
name: weather
description: Weather service via wttr.in for current weather and forecasts without API key required. Use when the user asks about weather, temperature, forecasts, or conditions for any location worldwide.
prerequisites:
  commands: [curl]
metadata:
  hermes:
    tags: [weather, forecast, wttr]
---

# Weather (wttr.in)

Weather forecast service accessible via curl. No API key required.

## Basic Usage

- Current weather: `curl "wttr.in/CityName"`
- Concise format: `curl "wttr.in/CityName?format=3"`
- Current only: `curl "wttr.in/CityName?0"`
- Current + today: `curl "wttr.in/CityName?1"`
- Current + 2-day: `curl "wttr.in/CityName?2"`

## View Options

- Plain text (no colors): `curl "wttr.in/CityName?T"`
- Narrow (day/night only): `curl "wttr.in/CityName?n"`
- Quiet: `curl "wttr.in/CityName?q"`
- Superquiet: `curl "wttr.in/CityName?Q"`

## Units

- Metric (SI): `curl "wttr.in/CityName?m"`
- Fahrenheit: `curl "wttr.in/CityName?u"`
- Wind in m/s: `curl "wttr.in/CityName?M"`

## Custom Format

`curl "wttr.in/Berlin?format=%l:+%C,+%t+(feels+like+%f).+Wind:+%w.+Humidity:+%h."`

Key tokens: `%l` location, `%C` condition, `%t` temp, `%f` feels like, `%w` wind, `%h` humidity

## Output Formats

- Terminal/ANSI (default)
- Plain text: `curl "wttr.in/CityName?T"`
- PNG image: `curl "wttr.in/CityName.png"`
- JSON: `curl "wttr.in/CityName?format=j1"`

## Localization

`curl "fr.wttr.in/Paris"` or `curl "wttr.in/Paris?lang=fr"`

## Notes

- No API key required
- Supports city names worldwide
- Default format optimized for terminal display
