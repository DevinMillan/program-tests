print("New Python") # Learn how to add an escape sequence
print("Test program")

int x = 1 # Initialization of integer x

# nested while-loop
while(x<5):
    print("This is a while loop")
    while(x<2):
        print("This is now a nested while loop")

# nested for-loop
y = ["1","2","3","4"]
for x in y:
    for x in y:
        print(x)
        if x == "2":
            break
        if y == "1":
            continue
        
#For-loop with range statement
for x in range(6):
    print("This is range")

#Nested Methods
print(AnotherFunction(x)) #Prints what was returned
def Function():
    y = 5;
    print(x)
    if(y>4):
        print("I made a method with a if statement!")
    else:
        print("Else statanent executed")
    def AnotherFunction(x):
        print("Nested Method")
        String x = "Hello"
        return x;
