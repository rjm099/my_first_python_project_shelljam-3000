# utils.py

# Dictionary of pastel RGB codes
PASTEL_COLORS = {
    "pink": "\033[38;2;255;182;193m",
    "mint": "\033[38;2;152;255;152m",
    "lavender": "\033[38;2;230;230;250m",
    "blue": "\033[38;2;135;206;235m",
    "yellow": "\033[38;2;255;253;208m"
}

RESET_COLOR = "\033[0m"

def print_pastel(text, color="pink"):
    """Prints text in a specified pastel shade to the terminal."""
    selected_code = PASTEL_COLORS.get(color.lower(), PASTEL_COLORS["pink"])
    print(f"{selected_code}{text}{RESET_COLOR}")