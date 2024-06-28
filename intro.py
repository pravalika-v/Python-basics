weight = input("Weight: ")
type = input("(K)g or (L)bs: ")
if type == "L" or type== "l":
    print ("Your weight in kgs:"+str(float(weight)*0.45))
elif type == "K" or type== "k":
    print("Your weight in pounds:"+str(float(weight)/0.45))
