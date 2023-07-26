def decimal_to_binary(decimal_num):
    binary_str = format(int(decimal_num), 'b')
    return binary_str

if __name__ == "__main__":
    try:
        while True:
            decimal_num = int(input("Enter a decimal number (Ctrl+C to exit): "))
            binary_num = decimal_to_binary(decimal_num)
            print(f"The binary value of {decimal_num} is: {binary_num}")
    except KeyboardInterrupt:
        print("\nExiting the program.")

