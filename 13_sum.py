# def replacing(word):
#     length=len(word)
#     letter_2=""
#     for char in word:
#         num=ord(char)
#         num_1=chr(num+1)
#         letter_2=letter_2+num_1
#         if num_1=="!":
#             letter_2=letter_2+" "
#             letter_2=letter_2.replace("!","")
#     return letter_2
# word= input()
# rep=replacing(word)
# print(rep)
def resv(res1):
    res=""
    for i in res1:
        
        res=i+res
    return res
res1=input()
print(resv(res1))