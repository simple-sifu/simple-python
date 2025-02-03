x = 10
y = 10
z = x

print("Memory location of x is: ", id(x))
print("Memory location of y is: ", id(y))
print("Memory location of z is: ", id(z))
print("Does x and y represent same object?: ", (x is y))
print("Does x and z represent same object?: ", (x is z))
print("Does x and y represent different object?: ", (x is not y))
print("Does x and z represent different object?: ", (x is not z))