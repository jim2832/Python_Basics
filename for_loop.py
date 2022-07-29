#依序印出字串內容
for letter in "這是一段文字":
    print(letter)

#迴圈用於列表
for num in [1, 2, 3, 4, 5]:
    print(num)

#range
for i in range(5):
    print(i)

#有初始和結束範圍
for i in range(2, 7):
    print(i) #印出2~6

#間隔為2
for i in range(2, 80, 2): 
    print(i)

#用迴圈實作次方
def power(base, pow):
    sum = 1
    for i in range(pow):
        sum *= base
    return sum

print(power(2,10))