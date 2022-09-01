import re


def main():
    #mail =input()
    special_char = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    mail1=re.search('@gmail.com',mail)
    mail2=re.findall('\w*@gmail.com',mail)

    for i in special_char:
        if i and mail2 and mail1:
            print("email is valid.")
            break
        else:
            print("email invalid !!")
            break


# Driver Code
mail=input()
main()