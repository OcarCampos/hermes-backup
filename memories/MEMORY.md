Google Calendar conventions: personal → main calendar. Work/SC/dam project → Reuniones UBIM CHEC calendar. House + Francisca → Family calendar.
§
Working style: single DM on Telegram for all contexts. No topic/thread separation — Hermes connects dots across work, home, Silo, and general. URL ref: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram#private-chat-topics-bot-api-94 (threads supported but not used for context separation).
§
Camera installation: Tue Apr 14 AM — Family calendar event created.
§
Samba fix (Apr 2026): `force group = +ocarjohann` caused `canonicalize_connect_path failed` on hermes-workspace share. Also `/mnt/data` SELinux context was `unlabeled_t` — fixed with `semanage fcontext` + `restorecon`. Root cause: `+` prefix in `force group` triggers group lookup during path canonicalization pre-auth.
§
Raindrop list: O'car (not Francisca) has the Raindrop.io list. The "francisca" folder in workspace was a mistake — O'car moved fidget-models.md to /mnt/data/Developing/hermes-workspace/3dprinting/clinical/.
§
Google Workspace email access (ocarnork138@gmail.com) via `/usr/bin/python3 ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py` — can search gmail with `gmail search` and retrieve with `gmail get`. Useful for tracking: bank transfers (Santander, BCI, Banco Estado), card purchases (MercadoPago, Mach), order confirmations (mechatronicstore, afel), and general financial reconciliation. Token at ~/.hermes/google_token.json.
§
Hermes dashboard: started as background process at PID 247548 on Apr 14. Runs on 127.0.0.1:9119.
§
Session search DB corrupted: "database disk image is malformed" error on session_search. ~/.hermes/sessions.db needs repair or rebuild. Affects ability to recall past conversations.