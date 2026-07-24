from pathlib import Path
import json


class StatsRepository:
    def __init__(self):
        self.file = Path("data/stats.json")
        self.file.parent.mkdir(exist_ok=True)

        if not self.file.exists():
            self.file.write_text(
                json.dumps(
                    {
                        "total_requests": 0,
                        "positive": 0,
                        "neutral": 0,
                        "negative": 0,
                        "unknown": 0,
                    },
                    indent=4,
                )
            )

    def get(self) -> dict:
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data: dict):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def increment(self, sentiment: str):
        stats = self.get()

        stats["total_requests"] += 1

        if sentiment in stats:
            stats[sentiment] += 1
        else:
            stats["unknown"] += 1

        self.save(stats)