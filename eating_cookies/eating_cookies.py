'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache=None):
    # Your code here
    # if there are less than 3 cookies
    # return the base case of combos
    # tests show 1, 1, 2 for less than three cookies
    # Cookie monster can only eat up to 3 cookies at a time
    base = [1, 1, 2]

    if n < 3:
        return base[n]

    # After the base case
    # f(n) = f(n-3) + f(n-2) + f(n-1)
    # USING RECURSION
    # Right answers, not efficient
    # else:
    #     return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)

    f1 = base[0]
    f2 = base[1]
    f3 = base[2]

    for _ in range(3, n):
        f3, f2, f1 = f1 + f2 + f3, f3, f2

    return f1 + f2 + f3


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
