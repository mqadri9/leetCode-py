
def num_steps(steps_left, comb_array):
    if steps_left == 0:
        return 1
    elif steps_left < 0:
        return 0
    else:
        sum = 0
        for i in comb_array:
            sum += num_steps(steps_left - i, comb_array)
        return sum
    
print(num_steps(3, [1,2]))  # returns 3
print(num_steps(3, [1, 2, 3])) # return 4
