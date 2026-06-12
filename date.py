from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("Asia/Kolkata"))

print("🇮🇳 India Date:", now.strftime("%d-%m-%Y"))
print("⏰ India Time:", now.strftime("%H:%M:%S"))
