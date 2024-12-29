def function_with_uncommon_error_solution(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        raise  # Re-raise the exception for the calling function to handle
    except TypeError:
        raise  # Re-raise the exception for the calling function to handle

#This is how to handle exceptions gracefully
try:
    result = function_with_uncommon_error_solution(10, 0) 
    print(result) #This line will not execute because the function will raise the exception
except ZeroDivisionError:
    print("Error: Division by zero handled gracefully")
try:
    result = function_with_uncommon_error_solution(10, "hello")
    print(result)
except TypeError:
    print("Error: Invalid type of input handled gracefully")
result = function_with_uncommon_error_solution(10, 2)
print(result) #prints 5.0