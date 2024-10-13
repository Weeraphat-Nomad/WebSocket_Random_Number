# myapp/consumers.py
import random
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class RandomNumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # ยอมรับการเชื่อมต่อจาก client

        # สุ่มตัวเลขและส่งไปยัง client แบบเรียลไทม์
        while True:
            random_number = random.randint(1, 100)
            await self.send(text_data=json.dumps({
                'number': random_number
            }))
            await asyncio.sleep(1)  # ส่งตัวเลขทุกๆ 1 วินาที

    async def disconnect(self, close_code):
        pass
