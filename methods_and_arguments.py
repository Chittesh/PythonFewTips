
def example_method (mandatory_parameter,default_parameter = "Default",
                    *variable_parameter , **keywordArguments):
    print(f'Mandatory Parameter is {mandatory_parameter} \n'
          f'Default Parameter is {default_parameter} \n'
          f'Variable Parameter is {variable_parameter} \n'
          f'Keyword argument is {keywordArguments} \n')

#example_method()        #TypeError: example_method() missing 1 required positional argument: 'mandatory_parameter'
example_method('hello')
#Mandatory Parameter is hello
#Default Parameter is Default
#Variable Parameter is ()   - tuple
#Keyword argument is {}     - dictionary

example_method('hello',5)
#Mandatory Parameter is hello
#Default Parameter is 5
#Variable Parameter is ()
#Keyword argument is {}

example_method('hello',5,'variable 1', 'variable 2','variable 3')
#Mandatory Parameter is hello
#Default Parameter is 5
#Variable Parameter is ('variable 1', 'variable 2', 'variable 3')
#Keyword argument is {}

example_method('hello',5,'variable 1', 'variable 2','variable 3',key1='1',key2='2',key3='3')
#Mandatory Parameter is hello
#Default Parameter is 5
#Variable Parameter is ('variable 1', 'variable 2', 'variable 3')
#Keyword argument is {'key1': '1', 'key2': '2', 'key3': '3'}

#Unpacking
list = [1,2,3,4,5,6,7,8]
example_method(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7])
dict_value = {'a':'1','b':'2'}
# the same above code can be done as unpacking
example_method(*list)
#Mandatory Parameter is 1
#Default Parameter is 2
#Variable Parameter is (3, 4, 5, 6, 7, 8)
#Keyword argument is {}

example_method(*list,**dict_value)
#Mandatory Parameter is 1
#Default Parameter is 2
#Variable Parameter is (3, 4, 5, 6, 7, 8)
#Keyword argument is {'a': '1', 'b': '2'} 