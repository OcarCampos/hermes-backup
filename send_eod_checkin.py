import asyncio
import os
import sys

sys.path.insert(0, os.path.expanduser('~/.hermes/hermes-agent'))

from tools.send_message_tool import _send_to_platform
from gateway.config import Platform, PlatformConfig

token = os.getenv('TELEGRAM_BOT_TOKEN')
print("Token:", token[:10] + "..." if token else None)

pconfig = PlatformConfig(
    enabled=True,
    token=token,
    extra={},
)

async def send():
    result = await _send_to_platform(
        platform=Platform.TELEGRAM,
        pconfig=pconfig,
        chat_id='1565773783',
        message="Hey O'car -- EOD check-in. Do you want to do the daily summary log for today? Reply with any additions or corrections to tasks/meetings, and I'll archive it and update TASKS.md.",
        thread_id=None
    )
    print("Result:", result)

asyncio.run(send())