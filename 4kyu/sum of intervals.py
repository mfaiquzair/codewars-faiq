def sum_of_intervals(intervals): #define function
    numbers = set() #to show iterable numbers

    for start, stop in intervals: #for loop utk start stop
        current = start
        while current < stop:
            numbers.add(current) #any number will add from current/start
            current += 1

    return len(numbers) #len return number