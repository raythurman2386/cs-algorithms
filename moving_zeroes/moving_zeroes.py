'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # See if the array has any zeros
    # FIRST PASS SOLUTION
    if 0 not in arr:
        return arr

    # What is the length of the current array
    length = len(arr)

    # Make a new array with no zeros
    new_arr = [num for num in arr if num != 0]

    # If the original length is less than the new array
    # add zeros to fill in the space
    while length > len(new_arr):
        new_arr.append(0)

    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
