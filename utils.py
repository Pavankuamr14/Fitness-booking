from datetime import datetime
import pytz

def ist_to_timezone(ist_datetime: datetime, to_tz: str = "UTC") -> datetime:
    ist = pytz.timezone("Asia/Kolkata")
    target = pytz.timezone(to_tz)
    return ist.localize(ist_datetime).astimezone(target)
