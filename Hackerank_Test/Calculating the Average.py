# Problem Statement: Calculating the Average
# You need to implement a function that calculates the average of a list of integers and prints the result formatted to two decimal places.
#
# Function Description:
#
# Function Name: avg
# Parameters: A variable number of integer arguments.
# Return Value: The average of the passed integers as a float.
# Requirements:
#
# Reading Input:
#
# The input will be a single line containing space-separated integers.
# Processing:
#
# Calculate the average of the provided integers.
# Output:
#
# Print the average rounded to exactly two decimal places.
# Example:
#
# Input: 1 2 3
# Output: 2.00



def avg(*args):
    total = sum(args)
    count = len(args)
    average = total / count
    return average

def alpha():
    nums = list(map(int, input().strip().split()))
    res = avg(*nums)
    print(f'{res:.2f}')
if __name__ == '__main__':
    alpha()
