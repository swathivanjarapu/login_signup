dic={}
def pess():
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
    global list
    user_name=input("enter your name : ")
    user_password=input("enter your password : ")


def signup():
    pess()
    dict={}
    dsptn=input("enter dsptn : ")
    hobbies=input("enter your hobbies : ")
    dob=input("enter your dob : ")
    gender=input("enter your gender : ")
    profile={"dsptn":dsptn,"hobbies":hobbies,"dob":dob,"gender":gender,}
    user={"name":user_name,"password":user_password,"profile":profile}
    list.append(user)
    dic["user"]=list
def login_signup():
    user_input=input("signup / login : ")
    if user_input=="signup":
        signup()
        print("congrats",user_name,"you are signed up successfu")
    else:
          print("wrong login / signup")
login_signup()


import json,os
list=[]
def password():
    g()
    l,u,p,d=0,0,0,0
    if (len(passwrd) >= 6): 
        for i in passwrd:  
            if (i.islower()): 
                l+=1 
            if (i.isupper()): 
                u+=1			 
            if (i.isdigit()):
                d+=1
            if i.isalnum():		
                p+=1	
        if (l>=1 and u>=1 and p>=1 and d>=1 or l+p+u+d==len(passwrd)): 
            confirm_password=input("confirm password:  ")
            if passwrd==confirm_password:
                print("matched")
            else:
                print("not same")
                password()
        else:
            print("your password must have atleast one uppercase, digit,and alnum ")
            password()
    else:
        print("password must be more tha 6 characters")
        password()
def g():
    global list
    global passwrd
    global name
    global file_name
    name=input("enter you name   ")
    passwrd=input("enter password   ")
    file_name="account.json"


def sign_up():
    password()
    if(os.path.isfile("account.json")):
        file=open(file_name,"r")
        dic2=json.load(file)
        for  i in dic2["user"]:
            if i["name"]==name and i["password"]==passwrd:
                print("acount already exist")
                sign_up()
        else:
            descriptions=["dob:  ","gender:  ","address:  ","designation:  ","bio:  "]
            i=0
            dic={}
            d={}
            while i<len(descriptions):
                d[descriptions[i]]=input(descriptions[i])
                i+=1
            dic["name"]=name
            dic["password"]=passwrd
            dic["profile"]=d
            x=dic2["user"]
            x.append(dic)
            with open(file_name,"w+") as file1:
                json.dump(dic2,file1,indent=4)
               
    
                            
    else:
        descriptions=["dob:  ","gender:  ","address:  ","designation:  ","bio:  "]
        j=0
        d1={}
        dic={}
        list=[]
        d={}
        while j<len(descriptions):
            d[descriptions[j]]=input(descriptions[j])
            j+=1
        dic["name"]=name
        dic["password"]=passwrd
        dic["profile"]=d
        list.append(dic)
        d1["user"]=list
        with open(file_name,"w+") as file1:
            json.dump(d1,file1,indent=4)
    
        
    
def log_in():
    g()
    a=open("account.json","r")
    f=json.load(a)
    for i in f["user"]:
        if i["name"]==name:
            if i['password']==passwrd:
                print("Login successful")
                print(i)
                break
            else:
                print("incorrect password")
        else:
            print("incorrect username")
    else:
        print("Your enter wrong input ")
        print("pliz check ")


def main():
    option=int(input("enter 1 for log-in \n& 2 for sign-up\t"   ))
    if option==1:
        log_in()
        print(name,"log in success")
    elif option==2:
        sign_up()
        print(name,"sign up success")
    else:
        print("please try again")
        main()
main()





    

