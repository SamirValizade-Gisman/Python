#we want to enter circle diameter
d=input("Circle diameter: ")
#Using the diameter information given by the user
#Let's calculate the #radius. Here is the int() function
r=int(d)/2
# our pi number is fixed
pi = 3.14159
# Using the information above, now
#we can calculate the area of the circle
#Let's convert the result from cm2 to m2
S=pi*pow(r,2)/10000
# Finally, we print the calculated area
print("Diameter",d,"area of circle in cm: ",int(S),"m2")

#GISMAN_first_code