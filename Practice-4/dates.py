# dates.py

# Import required classes
from datetime import datetime, timedelta
import pytz  # library for working with time zones

# Get current date and time
now = datetime.now()
print("Current date and time:", now)

# Format date into readable string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted)

# Create two specific date objects
date1 = datetime(2026, 1, 1)
date2 = datetime(2026, 2, 25)

# Calculate difference between two dates
difference = date2 - date1
print("Difference between dates:", difference.days, "days")

# Add 7 days to current date
future = now + timedelta(days=7)
print("Date after 7 days:", future)

# Work with specific timezone (Asia/Almaty)
timezone = pytz.timezone("Asia/Almaty")

# Get current time in that timezone
local_time = datetime.now(timezone)
print("Current time in Asia/Almaty:", local_time)
