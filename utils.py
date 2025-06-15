from pytz import timezone as pytz_timezone
import pytz

def ist_to_timezone(dt_ist, to_tz: str = "UTC"):
    ist = pytz_timezone("Asia/Kolkata")
    target = pytz_timezone(to_tz)
    dt_localized = ist.localize(dt_ist) if dt_ist.tzinfo is None else dt_ist.astimezone(ist)
    return dt_localized.astimezone(target)
