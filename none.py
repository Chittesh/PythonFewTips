def method(param1,param2,param3,param4 = None, param5 = None):
    print(f'{param1} {param2} {param3} {param4} {param5}')

method(1,2,3,4,5)   #1 2 3 4 5

#if we didn't use none in parameters
#method(1,2,3)       #TypeError: method() missing 2 required positional arguments: 'param4' and 'param5'
method(1,2,3)       #1 2 3 None None