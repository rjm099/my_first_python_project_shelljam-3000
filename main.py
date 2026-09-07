import datetime

def run_clock():
    current_time = datetime.datetime.now()
    clock_display = current_time.strftime("%I:%M %p")
    print(f"COMPOWDER SYSTEM ONLINE. Local Time: {clock_display}")

if __name__ == "__main__":
    run_clock()

