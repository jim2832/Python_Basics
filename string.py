#雙引號的字串
print("\"Hello World\"")

string1 = "Hello"
string2 = "World"
string3 = "APPLE"

#字串相連
print(string1 + " " + string2)

#字串函式
print(string1.lower()) #轉成小寫
print(string2.upper()) #轉成大寫
print(string3.islower()) #判斷是否全部是小寫 -> False
print(string3.isupper()) #判斷是否全部是大寫 -> True
print(string1.lower().islower()) #函式疊加
print(string1[0]) #string的index
print(string1.index("H")) #取得某個字元的index
print(string1.replace("ello", "i")) #string替換