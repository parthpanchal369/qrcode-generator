# str1 = "helloworld"
#
# str2 = ["Hello World"]

# def count_occurence(string):
#
#     num = {}
#
#     for x in string:
#         if x in num:
#             num[x] += 1
#
#         else:
#             num[x] = 1
#
#     for key,value in num.items():
#         print(f"{key} = {value}")
#
# string = "http"
# count_occurence(string)

# def is_palindrome(number):
#
#     str_number = str(number)
#
#     for i in str_number:
#         return str_number == str_number[::-1]
#
# number = (input("enter your value for check: "))
# if is_palindrome(number):
#     print(f"your {number} is palindrome")
#
# else:
#     print(f"your {number} is not a palindrome")


# def prime_number(number):
#
#     if number <2:
#         return False
#
#     for i in range(2,number):
#         if number % i == 0:
#             return False
#
#     else:
#         return True
#
# num = int(input())
# for x in range(1,num):
#     if prime_number(x):
#         print(x)


# def fectorial(num):
#
#     if num < 0:
#         return "not possible"
#
#     elif num ==1:
#         return 1
#
#     else:
#         return (num * fectorial(num-1))
#
# num1 = int(input())
# result = fectorial(num1)
# print(result)

# import qrcode as qr
# img = qr.make("Hello my name is parth panchal")
# img.save("my name.png")






