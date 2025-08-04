def check_divisibility(num, divisor):
    if isinstance(num, int) and isinstance(divisor, int): 
        if num % divisor == 0:
            return True 
        else:
            return False
    return


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
