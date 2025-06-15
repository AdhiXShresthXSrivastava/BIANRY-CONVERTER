def binary_to_text(binary_str):
    binary_values = binary_str.split()
    
    # Check if all inputs are valid binary numbers
    if all(set(b) <= {"0", "1"} for b in binary_values):  # Ensures each chunk only has 0s and 1s
        return ''.join(chr(int(b, 2)) for b in binary_values)
    else:
        return "Error: Input contains non-binary characters. Please enter only binary values."

print("Choose an option:")
print("1: Binary to Number")
print("2: Number to Binary")
print("3: Text to Binary")
print("4: Binary to Text")

option = int(input("Enter the option number: "))

if option == 1:
    binary_str = input("Enter binary number: ")
    print("Decimal:", int(binary_str, 2))

elif option == 2:
    num = int(input("Enter a decimal number: "))
    print("Binary:", bin(num)[2:])

elif option == 3:
    text = input("Enter text: ")
    print("Binary:", ' '.join(format(ord(char), '08b') for char in text))

elif option == 4:
    binary_str = input("Enter binary string (separate characters with spaces): ")
    print("Text:", binary_to_text(binary_str))

else:
    print("Invalid option! Please choose a valid number.")