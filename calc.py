#calculator  program
operation=input("please choose which operation do you want to do? summation,minus,multiplication,fraction or squareroot or power? ")
while operation=="squareroot":
            number=float(input("please enter  the number : "))
            result=number **.5
            print (result);                            quit()
            
while operation=="power":
                 number=float(input("please enter the number : "))
                 result=number**2
                 print (result);                        # quit()
                 
first_num=float(input("please enter the first number : " ) )
second_num=float(input("please enter the second number : "))

if operation=="summation":
            result=first_num+second_num
if operation== "minus":
            result=first_num-second_num
if  operation=="multiplication" :
            result=first_num*second_num
if operation=="fraction" :
            result=first_num/second_num
print (result)
exit()
