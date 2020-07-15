'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here
    # if n is less that one
    # return a 1
    if n <= 1:
        return 1

    # Cookie monster can only eat up to 3 cookies at a time
    pass


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
