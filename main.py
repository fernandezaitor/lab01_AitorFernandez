
# Requirement 1 - Reading Data from the Keyboard

#Read a sequence of numbers
numbers = input("Enter a sequence of numbers separated by spaces: ")
sequence = [float(number) for number in numbers.split()]

#Read an array of numbers
size = int(input("Enter the number of elements in the array: "))

array = []

for i in range(size):
    number = float(input(f"Enter number {i + 1}: "))
    array.append(number)

#Display the results
print("\n--- Results ---")
print("Sequence:", sequence)
print("Array:", array)


#Requirement 2 - Reading Numbers from a File

filename = input("\nEnter the text file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        file_numbers = [float(number) for number in content.split()]

    print("Numbers read from file:", file_numbers)

except FileNotFoundError:
    print("Error: The file does not exist.")

except ValueError:
    print("Error: The file contains invalid numbers.")