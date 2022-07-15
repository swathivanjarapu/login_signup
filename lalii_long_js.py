import json
name=input("Enter User Name:- ")
print("Welcome To The Login N SignUp Portal---")
Choose=input("Choose Any Portal Below--)\n1.SignUp\n2.LogIn\n")
if Choose=="SignUp":
    Name_User=input("Enter User Name:-")
    password=input("Enter Your Password:-")
    re_enter=input("Re-enter your password:-")
    Date_birth=input("enter  your DOB:")
    Gender=input("Enter your Gender Male/Female:")
    dic={"Name_User":Name_User,"password":password,"person_details":{"Date_birth":Date_birth,"Gender":Gender}}
    if len(password)>=8 and "#" in password or "@" in password or "$" in password:
        if password==re_enter:
            with open("persons_details.json","r") as f:
                data=json.load(f)
                for i in data["Choose"]:
                    if i["Name_User"]==Name_User and i["password"]==password:
                        print("This User Already Have An Account")
                        break
                else:
                    with open("persons_details.json") as file:
                        value=json.load(file)
                        x=value["Choose"]
                        x.append(dic)
                    with open("persons_details.json","w") as y:
                        json.dump(value,y,indent=4)
                    print("Hello",Name_User,"Congratulation Your Acoount has been Successfully Created.")
        else:
            print("Sorry Your Both Passwords Are not same--")
else:
    if Choose=="LogIn":
        print("Hello",name,"Welcome To The LogIn Portal:")
        Name_User=input("Enter Your User Name:-")
        Login_pass=input("Enter LogIn Password")
        with open("persons_details.json","r") as f:
            data=json.load(f)
            for i in data["Choose"]:
                if i["Name_User"]==Name_User and i["password"]==Login_pass:
                    print("Your LogIn Portal is Successfully Completed")
                    break
            else:
                print("\n either password or Name_User is wrong")
    else:
        print("Enter Your Correct Details")