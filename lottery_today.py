import random

def get_random_lottery_numbers():
    return random.sample(range(1, 53), 6)

if __name__ == "__main__":
    try:
        while True:
            input("Press Enter to get lottery numbers for today: ")
            for i in range(8):
                lottery_numbers = get_random_lottery_numbers()
                print(f"Combination {i+1}: {lottery_numbers}")
    except KeyboardInterrupt:
        print("\nExiting the program.")

