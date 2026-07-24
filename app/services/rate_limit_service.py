from pathlib import Path
import json
import time

from fastapi import HTTPException

from app.core.config import settings


class RateLimitService:
    def __init__(self):
        self.file = Path("data/rate_limit.json")

        self.file.parent.mkdir(exist_ok=True)

        if not self.file.exists():
            self.file.write_text("{}")

    def check(self, ip: str):

        with open(self.file, "r") as f:
            data = json.load(f)

        now = time.time()

        requests = data.get(ip, [])

        requests = [
            t
            for t in requests
            if now - t < settings.rate_limit_window
        ]

        if len(requests) >= settings.rate_limit_requests:
            raise HTTPException(
                status_code=429,
                detail="Too many requests"
            )

        requests.append(now)

        data[ip] = requests

        with open(self.file, "w") as f:
            json.dump(data, f)