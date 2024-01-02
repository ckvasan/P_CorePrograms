def unique_elements(input_list):
    '''
    Write a Python function that takes a list as input and returns a new list containing only the unique elements of the input list. The order of elements in the output list should be the order in which they first appear in the input list
    '''
    f = input_list[0]
    li = [f]
    for e in input_list[1:]:
        if e in li:
            pass
        else:
            li.append(e)

    return li


input_list = [1, 2, 3, 2, 4, 5, 6, 7]
print(unique_elements(input_list))
