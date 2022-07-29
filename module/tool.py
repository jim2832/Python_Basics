name = "Jim"
age = 87

num = [10, 20, 30, 5, 43, 100]
def max_num(num):
    max = 0
    for i in range(len(num)):
        if max < num[i]:
            max = num[i]
    return max