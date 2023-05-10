"""Task - List intersection
You are given two lists with an unknown amount of elements. Both of those lists may have some elements in common. Implement a method intersection that takes those two lists as arguments and returns a third list only with the elements they have in common.

Input:
list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
Output:
> intersection(list_1, list_2)

[9, 10, 4, 5]"""

# Solution 1



def intersection(list_1, list_2):
    # Convert the input lists to sets
    set_1 = set(list_1)
    set_2 = set(list_2)
    
    # Find the intersection of the sets
    common_elements = set_1 & set_2
    
    # Convert the intersection set back to a list
    result = list(common_elements)
    
    # Return the resulting list
    return result

list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
result = intersection(list_1, list_2)
print(result)

print("_______________________________________________")

# Solution 2
def intersection(list_1, list_2):
    common_elements = []
    
    # Iterate over each element in list_1
    for element in list_1:
        # Check if the element is present in list_2 and not already in common_elements
        if element in list_2 and element not in common_elements:
            common_elements.append(element)
    
    return common_elements

list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
result = intersection(list_1, list_2)
print(result)
