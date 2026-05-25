Google Calendar conventions: personal → main calendar. Work/SC/dam project → Reuniones UBIM CHEC calendar. House + Francisca → Family calendar.
§
Working style: single DM on Telegram for all contexts. No topic/thread separation — Hermes connects dots across work, home, Silo, and general. URL ref: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram#private-chat-topics-bot-api-94 (threads supported but not used for context separation).
§
Finance workflow (learned May 2026): Income file = ONLY salary/freelance (Fintual transfers/investment returns/transfers between accounts NOT here). Expenses file = money leaving O'car's control. Budget file = 50% of household bills (electricity, water, internet, gas) — O'car pays 100%, Francisca reimburses 50% via Tricount. Fintual savings logged as Savings expense in budget+expenses. Mach/MercadoPago = storage only. Load = transfer, NOT expense. Budget philosophy: inflated categories create flexibility margins — actual spending typically under budget. Priority is Fintual savings retention over cash buffer.
§
Raindrop list: O'car (not Francisca) has the Raindrop.io list. The "francisca" folder in workspace was a mistake — O'car moved fidget-models.md to /mnt/data/Developing/hermes-workspace/3dprinting/clinical/.
§
Google Workspace email access (ocarnork138@gmail.com) via `/usr/bin/python3 ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py` — can search gmail with `gmail search` and retrieve with `gmail get`. Useful for tracking: bank transfers (Santander, BCI, Banco Estado), card purchases (MercadoPago, Mach), order confirmations (mechatronicstore, afel), and general financial reconciliation. Token at ~/.hermes/google_token.json.
§
Hermes dashboard: started as background process at PID 247548 on Apr 14. Runs on 127.0.0.1:9119.
§
"The Hell" (garden/hell/): ThingSpeak Tenvironment channel 2781694, read API: SKWN0AM0TEWZQJ5H. Fields: Temperature(°C), Humidity(%), Light(lux). Data: 992 readings May 14–24 2026 — avg 14.4°C (too cold for warm crops), max 177 lux (far too dark). Currently not viable for vegetables without supplemental light+heat.