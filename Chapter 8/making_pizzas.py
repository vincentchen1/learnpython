#import pizza
#to import an entire module named module_name.py, each function is avaiable through the syntax, module_name.function_name()
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#importing specific functions

#you can also import a specific function from a module using, from module_name import function_name
#You can import as many functions as you want from a moduule by separating each function's name with a comma: from module_name import function_0, function_1, function_2
#The making_pizzas.py would look like this if we want to import just the function we're going to use

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#using as to give a function an alias

#the general syntax for providing an alias is: from module_name import function_name as fn
#alias' may be used when an existing name in your program already exists or if the function name is long
#make_pizza()'s alias is mp()

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#using as to give a module an alias

#the general syntax for this approach is: import module_name as mn
#giving a module a short alias, like p for pizza allows you to call the module's fuunctions more quickly
#calling p.make_pizza() is more concise than calling pizza.make_pizza()

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#importing all functions in a module

#the general sytax for this approach is: import module_name *
#you can tell python to import every function in a module by using the asterisk (*) operator:
#best not to use this approach when working with larger modules that you didn't write, as it may cause unexpected results
#the best approach is to import the function or functions you want, or import the entire module and use the dot notation

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#styling functions

#if you specify a default value for a parameter, no spaces should be used on either side of the equal sign: def function_name(parameter_0, parameter_1='default value')
#the same convention should be used for keyowrd arguments in function calls: function_name(value_0, parameter_1='value')
#if a set of parameters causes a function's definition to be longer than 79 characters, press ENTER after the opening parenthesis on the definition line
#all import statements should be written at the beginning of a file, the only exception being notes that describe the overall program
