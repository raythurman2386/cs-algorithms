'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr, cache={}):
    # Your code here
    # use dict to keep track of each number
    # track how many times that number is seen
    # return the number from the dict whose value is 1
    # INITIAL IMPLEMENTATION
    for num in arr:
        if num not in cache:
            cache[num] = 1
        else:
            cache[num] += 1

    for k, v in cache.items():
        if v == 1:
            return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
