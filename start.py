import datetime

# 1. Ask your computer for the exact time right now
current_time = datetime.datetime.now()

# 2. Format it to look like a normal digital clock (e.g., 07:28 PM)
clock_display = current_time.strftime("%I:%M %p")

# 3. Print it to the screen
print(f"COMPOWDER SYSTEM ONLINE. Local Time: {clock_display}")

