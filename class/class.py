class Phone:
    def __init__(self, os, number, is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

    def is_iOS(self):
        if self.os == "iOS":
            return True
        else:
            return False

    def add(self, num1, num2):
        return num1 + num2

    def call(self, phone_number):
        print("正在撥打給" + str(phone_number) + "...")

iPhone_12 = Phone("iOS", "091232132", True)
iPhone_4 = Phone("iOS", "09123123", False)
print(iPhone_12.os)

print(iPhone_12.is_iOS())
iPhone_12.call("0921312321")