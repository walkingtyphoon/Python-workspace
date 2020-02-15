password_file = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
                 "I": "..", "J": ".---",
                 "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
                 "S": "...",
                 "T": "-", "U": "..-",
                 "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
                 "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                 "6": "-....", "7": "--...", "8": "---..", "9": "----.",
                 ".": ".-.-.-", ":": "---...", ",": "--..--", ";": "-.-.-.", "?": "..--..", "=": "-...-", "'": ".----.",
                 "/": "-..-.", "!": "-.-.--", "-": "-....-", "\"": ".-..-.", "(": "-.--.", ")": "-.--.-",
                 "$": "...-..-", "@": ".--.-.", "+": ".-.-."}
# 这是摩尔斯密码的加密密码本


def encryption(word):
    """
    This method is to encrypt the specified characters
    """
    print("Encrypted ciphertext:", end="")
    for i in word:
        if len(word) <= 0:
            raise Exception("NoneString")
        if i in password_file:
            print(password_file.get(i), end=" ")


def Decrypt(word):
    if "/" in word:
        txt = word.split("/")
    elif " " in word:
        txt = word.split(" ")

    print("Decrypted Original:", end="")
    for i in txt:
        for j, k in password_file.items():
            if i == k:
                print(j.lower(), end="")


choose = input(""" ┏┓   ┏┓
┏┛┻━━━┛┻┓
┃　　　　　　　┃ 　
┃　　　━　　　┃
┃　┳┛　┗┳　┃
┃　　　　　　　┃
┃　　　┻　　　┃
┃　　　　　　　┃
┗━┓　　　┏━┛
　　┃　　　┃　　　　　　　
　　┃　　　┃
　　┃　　　┗━━━┓
　　┃　　　　　　　┣┓
　　┃　　　　　　　┏┛
　　┗┓┓┏━┳┓┏┛
　　　┃┫┫　┃┫┫
　　　┗┻┛　┗┻┛
Welcome to alpaca, this software professional terms Morse password 
encryption and cracking, I wish you a happy use,
Common options: 
             1. Encrypt text 
             2. Decrypt ciphered 
             3. Exit the system
Please input what you need to do:""")
if choose == str(1):
    value = input("Please enter the string you need to encrypt:")
    # 录入一段需要操作的字符串
    text = value.upper()
    # 将输入的字符串转化为大写
    encryption(text)
    # 调用加密的方法
elif choose == str(2):
    value = input("Please enter the string you need to decrypt:")
    # 录入一段需要操作的字符串
    text = value.upper()
    # 将输入的字符串转化为大写
    Decrypt(text)
    # 调用解密的方法
else:
    print("Thank you for your use and have a good time^_^")
    exit(0)