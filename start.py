# ShellJAM 3000 - Main System Hub
import datetime

def boot_sequence():
    print("==================================")
    print("  SHELLflip 3000: SYSTEM ONLINE    ")
    print("  Agent Gadget v1.0         ")
    print("==================================")

def display_status():
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%A, %B %d, %Y")
    
    print(f"Current Date: {date_str}")
    print(f"System Time:  {time_str}")
    print("Status:       All spy systems nominal. Ready for upgrade.")

if __name__ == "__main__":
    boot_sequence()
    display_status()