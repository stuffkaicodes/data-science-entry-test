def find_first_negative(lst):
    count = 0
    while count < len(lst): 
        if lst[count] < 0:
            print(count, lst[count])
            return lst[count]
        count += 1 
    return "No negatives"
    


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]
