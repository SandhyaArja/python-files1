import re
num=input("Give an num starts with +91")
check_num1=re.search(".\w{2} [6-9][0-9]{9}",num) #\wReturns a match where the string contains any word characters
# ( digits from 0-9, and the underscore _ character)
check_num=re.findall('.\d{2} \d{10}',num)#herefind all checks all the Returns a list containing all matches
#check1=re.search(check_num,check_num1)
if check_num and check_num1:
    print("Is valid")
else:
    print("Invalid")