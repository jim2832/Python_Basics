answer = 77
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while guess != answer and not(out_of_limit):
    guess_count += 1
    if(guess_count <= guess_limit):
        guess = int(input("請輸入一個數字: "))
        if(guess > answer):
            print("小一點")
        elif(guess < answer):
            print("大一點")
        else:
            print("恭喜答對！")
            break
    else:
        out_of_limit = True
        print("猜測機會用盡！再接再厲！")