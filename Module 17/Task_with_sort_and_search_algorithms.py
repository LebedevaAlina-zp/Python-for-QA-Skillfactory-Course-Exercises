# Write a program that inputs a sequence of numbers separated by a space, and requests any number from the user.
# As an additional task, you can perform a compliance check specified in the data entry condition.
# Next, the program works according to the following algorithm:
# 1. Converts the entered sequence into a list
# 2. Sorts the list in ascending order (by defined sorting function)
# 3. Identifies an index of an element, which is less than the number entered by the user, while the following one is
# greater. (Here use the binary search algorithm)

def merge_ascending(A, B):
    """ Merge function to perform the merge sort algorythm """
    i, j, C = 0, 0, []
    while len(C) < len(A) + len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
            if i == len(A):
                C.extend(B[j:])
        else:
            C.append(B[j])
            j += 1
            if j == len(B):
                C.extend(A[i:])
    return C


def bottom_up_merge_sort(A):
    """ Merge sort function """
    k = 1
    while k < len(A):
        for i in range(0, len(A)-k, 2*k):
            A[i:i+2*k] = merge_ascending(A[i:i+k], A[i+k:i+2*k])
        k *= 2

    return A


def binary_search(array, number, left, right):
    """ This is a function to use in find_between_position(array, x) """
    """ Returns an index of an element in the array which is less than the number while followed by the greater one """
    if left > right:
        return f"No such an element was found. "

    middle = (right + left) // 2
    if array[middle] < number < array[middle+1]:  # check if the middle element meets the condition
        return middle
    elif number < array[middle]:  # if the middle element exceeds the number
        # then we keep searching recursively in the left half
        return binary_search(array, number, left, middle - 1)
    else:  # else (if the middle element is equal to the number or the next middle element is less than the number
        # then we keep searching recursively in the right half
        return binary_search(array, number, middle + 1, right)


def find_between_position(array, x):
    """ Returns an index of an element of a sorted array, that is less than x and the following one is greater """
    if len(array) < 2:
        return "No such an element was found. The sequence must consist of at least 2 elements."
    if array[0] >= x :  # If the user's number is less or equal than the first (the least) element
        return f"No such an element was found. No number in your sequence is less than {x}."
    if array[-1] <= x: # If the user's number exceeds the last (the greatest) element
        return f"No such an element was found."

    return binary_search(array, x, 0, len(array))


while True:
    sequence_string = input("Enter a sequence of numbers separated by spaces: ")
    try:
        num_list = list(map(int, sequence_string.split()))
        break
    except ValueError:
        try:
            num_list = list(map(float, sequence_string.split()))
            break
        except ValueError:
            print("Please, use only digits, decimal point if needed and spaces")

while True:
    number_string = input("Enter a number: ")
    try:
        number = int(number_string)
        break
    except ValueError:
        try:
            number = float(number_string)
            break
        except ValueError:
            print("Please, use only digits and decimal point if needed")

sorted_list = bottom_up_merge_sort(num_list)

print("Your sequence sorted in ascending order: ", sorted_list)
print("Now let's find an index of an element in the sorted sequence that is less than your number and followed by a greater one.")
print(find_between_position(sorted_list, number))
