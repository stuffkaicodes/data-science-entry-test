def find_and_replace(lst, find_val, replace_val):
    lst_copy = lst
    if isinstance(lst,list): 
        for i in lst_copy:
            if i == find_val:
                ind = lst_copy.index(i)
                lst[ind] = replace_val
    return lst
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    return


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"
