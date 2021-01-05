print("welcome user to our calcultor \n we provide only four options sorry for that")
x =input("enter your name ")
print(x)
print("lets start the calcultor " ,x)
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. divsion")
print("5. exit")

while True:
    
    
    choice =int(input("enter your choice"))
    
    if choice>=1 and choice<=4:
        num1 =int(input("enter no1"))
        num2 = int(input("enter no2"))
        
        if choice ==1:
            res = num1+num2
            print("result =" , res)
            
        elif choice ==2:
            res = num1-num2
            print("result =" , res)
            
        elif choice ==3:
            res = num1*num2
            print("result =" , res)
            
        elif choice ==4:
            res = num1//num2
            print("result =" , res)
            
    elif choice ==5:
        exit()
            
    else:
        print("wrong input")


        
            
        