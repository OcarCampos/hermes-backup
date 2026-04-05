Sudo password for Silo (Fedora): stored in /home/ocarjohann/.hermes/.env as SUDO_PASSWORD. This means sudo works in terminal sessions (sudo -S reads from stdin). Use subprocess with input='password\n' when Python needs sudo.
§
Working style: single DM on Telegram for all contexts. No topic/thread separation — Hermes connects dots across work, home, Silo, and general. URL ref: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram#private-chat-topics-bot-api-94 (threads supported but not used for context separation).
§
Pending task: Check why Arduino is not updating ThingSpeak channel 2785218 (SmartPlant). Last automated reading was ~Apr 1-2. Plant (Lemon Haze, Day 44/50 VEG) is fine - ThingSpeak manual pulls still work, so the hardware/ThingSpeak API is fine. Issue likely on Arduino side or automated cron/daily-log script. Garden/ThingSpeak monitoring also needs to be resumed.
§
Samba fix (Apr 2026): `force group = +ocarjohann` caused `canonicalize_connect_path failed` on hermes-workspace share. Also `/mnt/data` SELinux context was `unlabeled_t` — fixed with `semanage fcontext` + `restorecon`. Root cause: `+` prefix in `force group` triggers group lookup during path canonicalization pre-auth.
§
Raindrop list: O'car (not Francisca) has the Raindrop.io list. The "francisca" folder in workspace was a mistake — O'car moved fidget-models.md to /mnt/data/Developing/hermes-workspace/3dprinting/clinical/.