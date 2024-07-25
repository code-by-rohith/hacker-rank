def find_trips(arr, weight):
    arr.sort()
    trips = 0
    i = 0
    j = len(arr) - 1

    while i <= j:
        if arr[i] + arr[j] <= weight:
            i += 1
        j -= 1
        trips += 1

    return trips


# Example usage
arr = [10, 20, 30, 40, 50]
k = 60
trips = find_trips(arr, k)
print("Minimum trips required:", trips)
