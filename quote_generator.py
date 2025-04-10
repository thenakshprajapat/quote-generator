import random
import time

# Dictionary containing different categories of quotes
quotes = {
    "sad": [
        "It's okay to feel down.\nThe sun will shine again.",
        "Tough times never last,\nbut tough people do.",
        "Crying doesn't make you weak.\nIt's a sign that you're human.",
        "Even the darkest night will end\nand the sun will rise.",
        "You’re not alone.\nBrighter days are ahead."
    ],
    "happy": [
        "Smile, it’s a good day to be alive!",
        "Happiness is not out there,\nit’s inside you.",
        "Every moment is a fresh beginning.",
        "You radiate positivity—\nkeep shining!",
        "Enjoy the little things,\nfor one day you'll look back and realize they were the big things."
    ],
    "motivational": [
        "Push yourself,\nbecause no one else is going to do it for you.",
        "Success doesn't come from what you do occasionally.\nIt comes from what you do consistently.",
        "Discipline is the bridge between goals\nand accomplishment.",
        "Wake up with determination,\ngo to bed with satisfaction.",
        "If you want it,\nwork for it. It's that simple."
    ],
    "inspiring": [
        "Believe you can\nand you're halfway there.",
        "Your story is still being written.\nDon’t give up now.",
        "Small steps every day\nlead to big results.",
        "Dream big.\nStart small. Act now.",
        "You were born\nto make an impact."
    ]
}

print("🌟 Welcome to the Quote Generator 🌟\n")

# Main loop
while True:
    # Show available categories
    print("Available categories:", ', '.join(quotes.keys()))
    ch = input("Enter the category you want [or type 5 to exit]: ").lower()

    if ch == "5":
        print("\n👋 Exiting... Stay inspired and keep hustling!")
        break
    elif ch in quotes:
        print("\nLoading your quote...\n")
        time.sleep(1.5)  # Simulate loading delay
        print(f"👉 {random.choice(quotes[ch])}\n")  # Randomly select and print a quote
    else:
        print("❗ Invalid input. Please choose a valid category.\n")
