def weight_average(my_list=[]):
    if not my_list:
        return 0
    return sum(map(lambda x: x[0] * x[1], my_list)) / sum(map(lambda x: x[1], my_list))
