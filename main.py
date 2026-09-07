# ShellJAM 3000 - Main Hub
from utils import print_pastel
import start
import weather

if __name__ == "__main__":
    print_pastel("==================================", "lavender")
    print_pastel("  SHELLJAM 3000: ALL SYSTEMS BOOTING", "pink")
    print_pastel("==================================", "lavender")
    
    # 1. Run the time and date sequence
    start.run_clock()
    
    print_pastel("-" * 34, "blue")
    
    # 2. Run the live weather report
    weather.get_weather()
    
    print_pastel("==================================", "lavender")
    print_pastel("  Mission Status: Ready for Action", "mint")