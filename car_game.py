option =""
started = False
stopped = False
while True:
    option = input().capitalize()
    if(option == "Start"):
        if started:
            print ("Car is already started")
        else:
            started = True
            print("Starting the car")
    elif(option == "Stop"):
        if stopped:
            print("Car is already stopped")
        else:
            stopped = True
            print("Stopping the car")
    elif (option == "Help" ):
        print("""Start- to start the car
Stop - to stop the car
Quit - to exit""" )
    elif(option == "Quit"):
        break
    else:
        print("Invalid option")


