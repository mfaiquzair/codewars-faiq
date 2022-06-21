def sum_of_intervals(intervals): #define function
    numbers = set()

    for start, stop in intervals: #for loop utk start stop
        current = start
        while current < stop:
            numbers.add(current)
            current += 1

    return len(numbers) #len return number