#開啟檔案
file = open("test.txt", mode = "r", encoding="UTF-8")
file2 = open("file/test2", mode = "w", encoding="UTF-8")
file3 = open("file/test2", mode = "a", encoding="UTF-8") #a模式表示在原本的檔案上再加寫

#讀取整個檔案
print(file.read())

#用for迴圈印出每一行
for line in file:
    print(line)

#讀取單行
print(file.readline())
#放到列表裡面
print(file.readlines())

#複寫
file2.write("Hello")

file3.write("\nPython")

#關閉檔案
file.close()
file2.close()
file3.close()

#用這個方法就不用特別關閉檔案
with open("test.txt", mode = "r", encoding="UTF-8") as file:
    file.read()