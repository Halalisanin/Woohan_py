import random
import datetime

def get_random_lottery_numbers():
    random.seed(datetime.datetime.now())  # Set the seed based on the current date and time
    return random.sample(range(1, 53), 6)

if __name__ == "__main__":
    try:
        while True:
            input("Press Enter to get lottery numbers for today: ")
            lottery_combinations = [get_random_lottery_numbers() for _ in range(8)]
            print("Lottery Numbers for today:")
            for i, combination in enumerate(lottery_combinations, 1):
                print(f"Combination {i}: {combination}")
    except KeyboardInterrupt:
        print("\nExiting the program.")

