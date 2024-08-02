
# Sort the given elements in descending order based on the number of factors of each element
def count_factors(num):
    factors = 0
    for i in range(1, num //2+1):
        if num % i == 0:
            factors += 1
    return factors

def sort_by_factors(arr):
    return sorted(arr, key=count_factors, reverse=True)

def main():
    arr = [100, 57, 60, 89, 36]
    print("Original array:", arr)
    sorted_arr = sort_by_factors(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()
