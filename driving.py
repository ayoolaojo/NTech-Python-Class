Command = ""
Started = False
while True:
    Command = input ("Enter a command >>>> ").lower()
    if Command == "start":
        if Started:
            print("Car already started!")
        else: 
            Started = True
            print("Car Starts...")
        
    elif Command == "stop":
        if not Started:
            print("Car is already Stopped!")
        else:
            Started = False
            print("Car stopped.")
        
    elif Command == "help":
        print("""
Start -  to start the car
Stop - to stop the  car
Quit - to exit
              
              """)
    elif Command =="quit":
        break
       
    else:
        print(" Sorry! I don't understand that")
        
        