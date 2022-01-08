#syntax 
# lambda parameters :expression

print(lambda x: x*2)
#this returns a function object 
# so lets assign it to a variable
double = lambda x:x*2
print(double(5))
age_check = lambda age:True if age>18 else False
print(age_check(20))