
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
