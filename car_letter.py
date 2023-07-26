import random
import string
import sys

def get_random_alphabet():
    return random.choice(string.ascii_uppercase)

if __name__ == "__main__":
    try:
        while True:
            input("Press Enter to get a random alphabet: ")
            random_alphabet = get_random_alphabet()
            print(f"Random Alphabet: {random_alphabet}")
    except KeyboardInterrupt:
        print("\nExiting the program.")
        sys.exit(0)
