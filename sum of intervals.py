def sum_of_intervals(intervals):
    numbers = set()

    for start, stop in intervals:
        current = start
        while current < stop:
            numbers.add(current)
            current += 1

    return len(numbers)