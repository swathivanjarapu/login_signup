import json
dic={}
list=[]
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
    
    with open("userdetails.json","w") as file:
        dsptn=input("enter dsptn : ")
        hobbies=input("enter your hobbies : ")
        dob=input("enter your dob : ")
        gender=input("enter your gender : ")
        profile={"dsptn":dsptn,"hobbies":hobbies,"dob":dob,"gender":gender,}
        user={"name":user_name,"password":user_password,"profile":profile}
        list.append(user)
        dic["user"]=list
        a=dic
        dic1=json.dump(dic,file,indent=4)
        print(dic1)
        
    with open("userdetails.json","r") as file:
        dic2=json.load(file)
        i=0
        while i<len(dic2):
            j=0
            while j<len(a):
                if a == dic2:
                    print("user already exists.Try again")
                    signup()
                else:
                    with open("userdetsils.json","w")as file:
                        dic1=json.dump(a)
                j=j+1
            i=i+1
    
def login():
    dic3={}
    dic4={}
    pss()
    with open("userdetails.json") as file: 
        dic3=json.load(file)
        if dic4==dic3:
            print("you are successfully login")
        else:
            print()
            biodata=input("bio : ")
            date_of_birth=input("dob : ")
            gender=input("gender : ")
            hobbies=input("hobbies : ")
            print()
            print("-------------------*****-------------------")
            print("profile")
            print("user_name :", user_name)
            print("gender :", gender)
            print("bio :", biodata)
            print("dob :", date_of_birth)
            print("hobbies :", hobbies)


def login_signup():
    user_input=input("signup / login : ")
    if user_input=="signup":
        signup()
        print("congrats",user_name,"you are signed up successfully")
    
    elif user_input=="login":
        login()
        print("congrats",user_name,"you are logged in successfully")

    else:
        print("wrong login / signup")
login_signup()