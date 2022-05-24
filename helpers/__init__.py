from datetime import datetime

## HELPER FUNCTION
def get_time_str() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def is_active(page, element):
    return "active" if page == element else ""