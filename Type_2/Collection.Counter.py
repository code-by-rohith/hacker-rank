from collections import Counter
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())
shoe_inventory = Counter(shoe_sizes)

total_earnings = 0

for _ in range(num_customers):
    size, price = map(int, input().split())

    if shoe_inventory[size] > 0:
        shoe_inventory[size] -= 1
        total_earnings += price
print(total_earnings)