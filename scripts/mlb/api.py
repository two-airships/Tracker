from zoneinfo import ZoneInfo

import requests
from datetime import datetime
from config import BASE_URL, LIVE_DATA_BASE_URL

def get_schedule(date: str | None = None) -> dict:
    """
    Fetch MLB schedule for a given date (YYYY-MM-DD).
    If no date is provided, use today's date.
    """
    if date is None:
        date = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d")

    url = f"{BASE_URL}/schedule"
    params = {
        "sportId": 1,  # MLB
        "date": date,
    }

    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()

    return response.json()