scores = [90, 70, 80, 10, 50]
friends = ["Amy", "John", "Sam"]
things = [90, "Jim", True]
print(scores, friends, things)

#index
print(scores[0], scores[1], scores[-1]) #-1代表倒數第一

#取得連續index
print(scores[0:2]) #取得0到1的data(不包含2)
print(scores[1:]) #從1取到結束
print(scores[:4]) #取4往前取
print(scores[::-1]) #從最後一個每次往前取到開頭
print(scores[0:5:2]) #取得0到4的data且間隔為2(不包含5)

#string的index
word = "Hello World"
print(word[1:5])

#assignment
scores[0] = 30

"""
list的函式
"""
#extend
scores.extend([1,3])
print(scores)

#append
scores.append(5)
print(scores)

#insert
scores.insert(3,100)
print(scores)

#remove
scores.remove(100)
print(scores)

#pop
scores.pop() #移除最後一個元素
print(scores)

#sort
scores.sort()
print(scores)

#reverse
scores.reverse() #反轉list
print(scores)

#index
print(scores.index(30)) #找到30的index

#count
print(scores.count(1)) #數1有幾個

#clear
scores.clear() #全部清空
print(scores)