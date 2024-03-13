"""
    Variables in python:
        variables are the containers for storing data values.


    Creating variable:
        python has no command to create variable
        * the variable is created at the moment you assign a value to it.

        Ex: a = 'a'
"""

x = 10  # variable created

"""
    Variable don't need to be declared with any particular type.
    when you assign value to variable the dynamically change it's type related value.

"""

integer_type = 3   # converted to an integer type
float_type = 3.14  # converted to a float type
string_type = "Habibi"  # converted to a string type


"""
    Type Casting:
        Type casting means that convert one type to another.
        like convert integer type to float type.
        
        converting type:
            by using this method you can convert to related type:
                to sting    srt()
                to integer  int()
                to float    float
"""

float_to_integer = int(float_type)
integer_to_float = int(integer_type)
float_to_string = str(float_type)

"""
    how to get the type of the variable:
        by using the type() function you can get the type of any variable.
"""

print(type(integer_type))
print(type(float_type))
print(type(string_type))  # we will talk about the print function later.

"""
    Single quote or Double quotes:
        string variables can declare with either by single quote and double quotes.
"""

name_single_quote = 'habibi'
name_double_quotes = "habibi"   # this variable value is the same as the above variable.

"""
    Case-sensitive:
        variable names are case-sensitive.
        a = 10 and A = 10 are the two different variables.
"""

A = 10  # is not the same with
a = 10  # we can't reference this variable with letter A. so Case sensitivity is important.

"""
    variable name:
        A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
        Rules for Python variables:
        A variable name must start with a letter or the underscore character
        A variable name cannot start with a number
        A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        Variable names are case-sensitive (age, Age and AGE are three different variables)
        A variable name cannot be any of the Python keywords
"""

#Legal variable names:
myvar = "Habibi"
my_var = "Habibi"
_my_var = "Habibi"
myVar = "Habibi"
MYVAR = "Habibi"
myvar2 = "Habibi"   # remember that variables are case sensitve

"""
    Illegal variable names:
        2myvar = "Habibi"
        my-var = "Habibi"
        my var = "Habibi"
"""

"""
    Multiword variables :
        variable should be readable and there are sevral methods for that.
        Camel Case: except first work first letter of all words is capital: myVar = 'Habibi'
        Poscal Case: each word first letter is capital: MyVar  = 'Habibi'
        Snake Case: each word is separated by underscore: my_var 
"""

myName = "Habibi"
MyName= "Habibi"
my_name = "Habibi"  # used most in python

"""
    Assign Multiple values to variables:
        by using comma we can declare and initialize multiple variables at the same time.
            x, y, z  = 10, "Strings", 3.14
            
            # sequence is important and the number of variables and the number of the value should be the same.
"""

x, y, z = 10, "Strings", 3.14
# let's print that
print("Values in sequence is: ", x, y, z)

"""
    Assign one value to multipe variables:
        we can assign the same value to multiple variables.
        x, y, z = 10

"""

# if you born in the capital of the countery and you like that you can create variables for that like this:
capital = hometwon = best_province = "Kabul"

"""
    Also, if a variable have more that one value or list of the values how can get that.
        single value variables can get by there names.
        so, geting values from the variable that has multip values is called uppacking.
"""

fruits = ['banana', 'apple', 'cherry', 'pear']

# get the values like this
w, x, y, z = fruits
print(w, x, y, z) # it will print all the values one by one


"""
    How to print variables: 
        in programming we use the word output for print 
        by using th print() we could print the variables when we write the name of the variable inside of the prantheses
"""

# we used a lot print function above
print(w)  # one value
print(x, y, z)  # multiple values
print("Hello, ", z)  # value and variable

"""
    NOTE: inside string the space in python is matter but, in programming side in ide or text editor python will ignor
        whitespace.
        string = "python    is  awsome"  # this will print exactly the same.
        x = "Python"
        y = "is"
        z = "awesome"
        

"""

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  # it will print "pythonisawesome"    # the space is matter

x = "Python "
y = "is "
z = "awesome"
print(x, y, z)  # it will print "python is awesome"    # the space is added so give space if you need.

"""
    Also, you could use the '+' operator to output multiple variables 
    
    * but the variables should be the same type other wise it will through an error which is type error

"""

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  # it will print "python is awesome"

"""
    also, the print function with numbers will preform the mathemathical operation. like add, sub, multi, div
"""

x = 10
y = 20

print(x + y)
print(x - y)
print(x * y)
print(x / y)

"""
    To print multipe variable in print function you the ',' sparator.
    
    * this suppourt different variables type and will not trough an error
"""

print(x, y, z)

"""
    Global variable:
        till now we showed you the variable all important part but on thing that is really important.
        that is the scope of the variable. scope is when we can use the variable somewhere.
        
        variable at the top or outside of the function is called global. we can use it anywhere.
        
        but inside of the fucttion if we create the same variable with the same name the will create new variable.
        and the old one will be work outside but inside of the function the new variable wrok and used.
        
        to prevent that problum we have in python the global keyword.

"""

a = 10 # global variable we can use it anywhere

def global_var():
    # if I user here a variable this is note the above
    # to reference that use the global keyworkd
    global a  # now you have acces to the a variable.
    print(a)

"""
    at the same time one variable with the same name  inside of the function not work the outside variable 
    to use it we should use the global variable. 
    
    * we use the global keywork to create a global variable inside the function.

"""
