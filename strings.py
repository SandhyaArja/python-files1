#reverse the entire string
def string_reverse(word):
    rev_word=word[::-1]
    return rev_word
#converts the string into lower case
def string_lower(word):
    word_lower=word.lower()
    return word_lower
#converts the string into upper case
def string_upper(word):
    word_upper=word.upper()
    return word_upper
#converts the string's first letter into upper  case
def string_capitalize(word):
    word_capitalize=word.capitalize()
    return word_capitalize
#checking if the string's first letter is in upper case if its is in upper case istitle method will give true
def string_is_title(word):
    word_is_title=word.istitle()
    return word_is_title
#common elements in both in inputs
def common_items(word, m):
        l = []
        for i in word:
            if i in m:
                l.append(i)
        return l
# alternate words coversion into upper case
def alternative_words(word):
        result=""
        for i in range(len(word)):
            if i%2==0:
                result+=word[i].upper()
            else:
                result+=word[i].lower()
        return result
#after every 3 letter the word will convert into uppercase

def alternative_words2(word):
    result = ""
    for i in range(len(word)):
        if i % 3 == 0:
            result += word[i].upper()
        else:
            result += word[i].lower()
    return result
#replacing the give words
def replacing_word(word):
    replacing=word.replace(" ","a")
    return replacing
#swapcase is like vice versa is the string contains lower case word the swap case ,method will convert the string into upper case by use swap case method
def swapcase_word(word):
    swap=word.swapcase()
    return swap
#count the vowels
def count_vowels(word):
    vowels="aieouAeiou"
    count=0
    for i in word:
        if i in vowels:
            count+=1
    return count
#checking that given string is in lowercase
def checking_lowercase(word):
    checking_lower=word.islower()
    return checking_lower
# cheching tat given string is in upper case
def checking_uppercase(word):
    checking_upper=word.isupper()
    return checking_upper
#strip method that remove the spaces
def removing_spaces(word):
    remove_space=word.strip()
    return remove_space
#adding 2 inputs by using __add__ method
def adding(word,m):
    add_word=word.__add__(m)
    return  add_word
# cheching the string by using contain methods it will return the boolean value if the string1 contains the same value in string2
def contains(word,m):
    contains=word.__contains__(m)
    return contains
#
word=input()
m=input()
print("*reverse","*lower","*upper","*capitalize","*istitle","*common","*alternative_words","alternative_words2","*swapcase","replacing",
           "*vowels","*lowercase","*uppercase","*removing_spaces","*adding","*contains")

while True:
    M=input()
    dict_word = {"reverse":string_reverse(word) , "lower": string_lower(word), "upper": string_upper(word),
                      "capitalize": string_capitalize(word), "istitle": string_is_title(word), "common":common_items(word,m) ,
                      "alternative_words": alternative_words(word),"alternative_words2":alternative_words2(word),"swapcase":swapcase_word(word),"replacing":replacing_word(word),"vowels":count_vowels(word),
                      "lowercase":checking_lowercase(word),"uppercase":checking_uppercase(word),"removing_spaces":removing_spaces(word),"adding":adding(word,m),"contains":contains(word,m)}

    if M in dict_word:
        print(dict_word[M])

