#TODO : Given a list/array of integers, arrange the list in descending order according to repetition
# frequency of item.
# In case where many integers have same repetition frequency, then put the smaller
# number first.

def ordering_array(input_list):
    # initially sorting is to sort and secondary sorting is to arrange it descending order and smaller number first
    
    output_list = sorted(sorted(input_list), key= input_list.count, reverse=True)
    return output_list

input_list = [1,4,5,6,6,5,3,5,1,6,4,6]
resulted_list = ordering_array(input_list)
print(resulted_list)