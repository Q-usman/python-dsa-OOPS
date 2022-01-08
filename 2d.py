d_list = [1,2,3,4,5,6,4,2,4]
uniques = []
for items in d_list:
    if items not in uniques:
        uniques.append(items)
print(uniques)

# unpacking this can be used in tuples and list


tuple = (1,2,3)
a,b,c = tuple
print('this is varaiable',a,b,c,'this is tupele : ', tuple)

#dictionary 
dict = {
    "name": "usman",
    "age": 20,
    "profession": 'engineer'
}
print(dict['name'])
print(dict.get('name','furqan'))

#function
''' 1. positional arguement
    2.keyword arguement : parameter = arguement
    3. we shoudl give positional agruement after the keyword agruement
'''
#try and execpt
try :
    x = int(input('enter the value'))
except ValueError:
    print('invalid input')
