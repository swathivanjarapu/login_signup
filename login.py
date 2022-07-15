# def sign():
#     user=input("choose signup/login  " )
#     if user=="signup":
#         a=input("enter user name  ")
#         b=input("enter pass word ")
#         c=input("enter mail ")
#         d=int(input("ur ph  "))
#         print("finish ur signup ",a)
#     else:
#         m=input("enter user name  ")
#         x=input("enter user name  ")
#         if m==x:
#             pass
#         else:
#             print("wrong user name")
#         n=input("enter pass")
#         y=input("enter pass")
#         if n==y:
#             pass
#         else:
#             print("wrong password")   
# sign()

# import json
# a=input("u want login ,enter login , u want sign up ,enter  signup  ")
# if a=="signup":
#     name=input("enter name ")
#     pass_word=input("enter password ")
#     email= input("enter ur email ")
#     print("finish ur signup")
#     b={"c":[name,pass_word,email]}
#     with open("abc.json",'w')as f:
#         d=json.dump(b,f)
#     print(d)
# elif a=="login":
#     pass

# from curses.ascii import islower, isupper
# from string import digits


# from curses.ascii import isalpha, isupper
# from lib2to3.pygram import Symbols
# from unicodedata import digit


# from cProfile import Profile
# from click import password_option

# import json
# def pess():
#     glbl()
#     user=input("enter u want sing up ,enter signup, u want login, enter login  ") 
#     password=" "
#     u=input("enter chra ")
#     l=input("enter  charc ")
#     s=input("enter symbo ")
#     d=input("enter digit ")

#     if u.upper():
#         password+=u
#     if  l.lower():
#         password+=l
#     if "s":
#         password+=s
#     if  "d":
#         password+=d
#         print(password)
#     a=input("enter password ")
#     if a==password:
#         print("ur password correct")

# def glbl():
#     global name
#     global password
#     global Profile
#     user=input("enter ur name")
#     password=input("enter ur password")
# def sign():
#     pess()
#     dict={}
#     with open("abc.json","w")as f:
#         a=json.dump(dict,f)

#     despiction=input("enter ur despication" )
#     hobble=input("enter hobbies")
#     phone=input("enter ur phone number")
#     email=input("enter ur email")
#     birth=input("enter ur date birth")
#     gender=input("enter ur gender")
#     print("ur signup complete suceefull")
# def login():
#     print("ur login succeful")
    


# def main():
#     user=input("enter signup/ login")j
#     if user=="signup":
#         sign()
#     elif user=="login":
#         login()
# main()


# user=input("enter u want sing up ,enter signup, u want login, enter login  ")
# if user=="signup":
#     name=input("enter name")
#     password=" "
#     u=input("enter chra ")
#     l=input("enter  charc ")
#     s=input("enter symbo ")
#     d=input("enter digit ")

#     if u.upper():
#         password+=u
#     if  l.lower():
#         password+=l
#     if "s":
#         password+=s
#     if  "d":
#         password+=d
#         print(password)
#     a=input("enter password ")
#     if password==a:
#         print("ur password correct")
#     else:
#         print("try again")
#     ph=input("enter ph number"
#     email=input("enter ur e


# def password():
#     confom_password=input("enter ur password")
#     u=input("enter chra ")
#     l=input("enter  charc ")
#     s=input("enter symbo ")
#     d=int(input("enter digit "))

#     if True:
#         confom_password+=u.upper()
#     if  True:
#         confom_password+=l.lower()
#     if True:
#         confom_password+=s
#     if  d>=0 and d<=9:
#         confom_password+=str(d)
#         print(confom_password)
#     if confom_password==password:
#         print("ur password correct")


# def sign():
#     name=input("enter ur name" )
#     password()
#     profile=input("enter descripes")
#     hobies=input("enter ur hobiess")
#     birth=input("enter ur date birth")
# def main():
#     user=input("enter signup/ login  ")
#     if user=="signup":
#         sign()
#     # elif user=="login":
# main()


def pss():
    glbl()
    confirm_password=input("conform password :")
    capital_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letter="abcdefghijklmnopqrstuvwxyz"
    dgt="123456789"
    special_character="@#$%^&*!"
    
    if user_password!=confirm_password:
        print("both p are not equal")
        print("try again")
        login_signup()

    if len(user_password)<6:
        print("lenght of p must be more than 6 digits")
        print("try again")
        login_signup()

    sum=0
    c1=0;c2=0;c3=0;c4=0
    i=0
    while i<len(user_password) :  
        if user_password[i] in capital_letter:
            c1=1
        if user_password[i] in small_letter:
            c2=1
        if user_password[i] in dgt:
            c3=1 
        if user_password[i] in special_character:
            c4=1
        i=i+1
    sum=c1+c2+c3+c4            
    if sum==4:
        print("your pssword is correct")
        print("your password is Confirm password")
                                    
    else:
        print("at least password must contain one capital letter,small letter,digit,special character" )
        login_signup()


def glbl():
    global user_name
    global data
    global user_password
    global profile
    user_name=input("enter your name : ")
    user_password=input("enter your password : ")



def signup():
    pss()
    dic={}
    