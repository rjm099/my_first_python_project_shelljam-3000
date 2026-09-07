# ShellJAM 3000 🐚✨

Welcome to the **ShellJAM 3000**, a custom-built, *Totally Spies!*-inspired gadget that turns a sleek vintage seashell compact into a functional smart tool. Built as a portfolio project for school transfers, it combines modular Python scripts with live data fetching.

## Features
- **Real-Time Clock:** Displays local system time to keep secret operatives on schedule.
- **Live Weather Feed:** Integrates the Open-Meteo API to pull current temperature and weather conditions without requiring API keys.
- **Compact Form Factor:** Designed to fit inside a portable physical shell housing.
- **Modular Python Architecture:** Built using clean, independent scripts for easy maintenance and hardware migration.

## Project Structure
- `start.py`: Initializes the core system clock and startup sequence.
- `weather.py`: Handles live weather data retrieval using Open-Meteo.
- `main.py`: The central hub that executes core processes and links modules together.
- `README.md`: Project documentation and mission logs.

## Future Missions
- [ ] Connect a 1.28-inch round LCD screen (GC9A01 driver) for visual output.
- [ ] Port the script to a Raspberry Pi Pico W for standalone, wireless hardware operation.
- [ ] Add a portable 3.7V battery pack for on-the-go field use.
