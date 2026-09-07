# ShellJAM 3000 - Main Hub
import start
import weather

if __name__ == "__main__":
    print("==================================")
    print("  SHELLJAM 3000: ALL SYSTEMS BOOTING")
    print("==================================")
    
    # 1. Run the time and date sequence
    start.run_clock()
    
    print("-" * 34)
    
    # 2. Run the live weather report
    weather.get_weather()
    
    print("==================================")
    print("  Mission Status: Ready for Action")
