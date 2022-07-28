hungry = False
rainy = True

if hungry:
    print("吃飯")
else:
    print("不吃飯")

#多個判斷式
if hungry and not(rainy):
    print("出門吃飯")
elif hungry and rainy:
    print("不出門吃飯")
elif not(hungry) and not(rainy):
    print("出門但不吃飯")
else:
    print("在家")

#判斷最大數
num = [10, 20, 30, 5, 43, 100]
def max_num(num):
    max = 0
    for i in range(len(num)):
        if max < num[i]:
            max = num[i]
    return max

print(max_num(num))