while True:

    password = input("enter your password : ").strip()
    confirmpw = input ("confirm your pasword: ").strip()

   
    if confirmpw == password:
       print("Password Confirmed")
       break
    else:
       print("password does not match, try again!")
       continue
       

       
       
