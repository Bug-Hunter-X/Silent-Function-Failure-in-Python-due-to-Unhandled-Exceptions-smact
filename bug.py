def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid type of input")
        return None

#This is a common error but often missed
#it will return None if there is an error which is not always desired
result = function_with_uncommon_error(10, 0)  #this will print the error but the value of result will be None
print(result) #prints None
result = function_with_uncommon_error(10, "hello")
print(result) #prints None
result = function_with_uncommon_error(10, 2)
print(result) #prints 5.0