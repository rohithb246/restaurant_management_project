from datetime import datetime

def format_datetime(dt):
    if dt is None:
        return ""

    if not isinstance(dt, datetime):
        return ""
        
    return dt.strftime("%B %d, %Y at %I:%M %P")
