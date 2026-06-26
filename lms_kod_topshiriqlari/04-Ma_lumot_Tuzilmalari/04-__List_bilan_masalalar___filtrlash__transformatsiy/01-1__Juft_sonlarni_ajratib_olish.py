n = int(input())
numbers = list(map(int, input().split()))

evens = [num for num in numbers if num % 2 == 0]

print(evens)