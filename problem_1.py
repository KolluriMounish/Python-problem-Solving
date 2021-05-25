#TODO: Given an array containing unsorted positive or negative integers with repeated
# values, you must arrange the array in such a way that all non-zeroes should be on the left-
# hand side of an array, and all zeroes should be on the right side of the array. Order of non-
# zero elements does not matter. You are not allowed to use any sorting approach.

def ordering_array(input_list):
    final_list=[]
    for value in input_list:
        if value == 0:      # if the given element is "ZERO" append it at the end of the list
            final_list.append(value)
        else:               # if the given element is "non_zero" value then insert it in the front side of the list
            final_list.insert(0,value)        
    return final_list

input_list = [1, 2, -4, 0, -1, 0, 3, 7, 0, 5, 0, 1, -1, 0]
resulted_list = ordering_array(input_list)
print(resulted_list)