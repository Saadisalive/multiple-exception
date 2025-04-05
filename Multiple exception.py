try:
    num1,num2 = eval(input("enter two numbers,seperated by comma :"))
    result = num1 / num2
    print("result is",result)
#usingmultiple except block for different type of error

except ZeroDivisionError:
    print("division by zero is erro !!")
    
except SyntaxError:
    print("Comma is missing.Enter numbers seperated by comma like this 1,2")
    
except:
    print("wrong input")
else:
    ("No exception")
finally:
    print("This will execute no matter what")