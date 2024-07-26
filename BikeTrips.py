# Given an array of values persons[], each represents the weight of the persons.
# There will be infinite bikes available.
# Given a value K which represents the maximum weight that a bike accommodates.
# Along with that one more condition, a bike can carry two persons at a time.
# You need to find out the least number of times, the bike trips are made.

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

arr = [10, 20, 30, 40, 50]
k = 60
trips = find_trips(arr, k)
print("Minimum trips required:", trips)
