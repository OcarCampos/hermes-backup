---
name: eod-checkin-cron
description: Send end-of-day check-in nudges to O'car via Telegram using the hermes cron system. Use when asked to send EOD reminders, daily log prompts, or similar recurring daily messages to O'car.
category: productivity
---

# EOD Check-in Cron Job

## Pattern

When running as a scheduled cron job with `deliver="telegram"` configured, **put the message text directly in the final response**. The cron system auto-delivers to the configured Telegram chat — no need to call `send_message` tool or run separate send scripts.

## Common Prompt Template

```
End-of-day check-in. Ask O'car if he wants to do the daily summary log for today.
If yes, ask for any additions or corrections to the day's tasks and meetings,
then archive to archive/YYYY-MM.md and update TASKS.md.
Keep it brief — this is a nudge, not a meeting.
Deliver to origin (telegram).
```

## What to Do

1. **Just produce the nudge message as your final response** — the cron system delivers it
2. If O'car replies yes, proceed to:
   - Read today's tasks/meetings from TASKS.md
   - Ask if any additions/corrections
   - Archive summary to `archive/YYYY-MM.md`
   - Update TASKS.md with final status

## Why No send_message Tool?

The `send_message_tool` requires a `PlatformConfig` with a bot token loaded via `load_gateway_config()`. This only works when the gateway has Telegram configured in its YAML config. O'car's Telegram runs via env-injected token (`TELEGRAM_BOT_TOKEN`), not YAML config — so `load_gateway_config()` returns no Telegram platform.

**The cron auto-delivery system already knows the Telegram chat** via:
- `HERMES_CRON_AUTO_DELIVER_PLATFORM=telegram`
- `HERMES_SESSION_KEY=agent:main:telegram:dm:<chat_id>`

These are set by the running gateway process and automatically deliver your final response to Telegram. Use this mechanism instead.
