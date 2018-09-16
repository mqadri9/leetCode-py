def subsets_in_set(element, index, array_element, permutation_list):
    if index < 0:
        return
    if element not in permutation_list:
        permutation_list.append(element)
    subsets_in_set(set(element), index-1 , array_element, permutation_list)
    element = list(element)
    element.append(array_element[index-1])
    subsets_in_set(set(element), index-1 , array_element, permutation_list)


permutation_list = []
subsets_in_set(set(), 4, [1,2,3,6], permutation_list)
print permutation_list
