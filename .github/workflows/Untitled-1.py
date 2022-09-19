def range_sum(*numbers):
    if len(numbers) == 1:
        return sum(range(0, numbers[0]))
    if len(numbers) == 2:
        return sum(range(numbers[0], numbers[1]))
    if len(numbers) == 3:
        return 0

print(range_sum(1, 2))