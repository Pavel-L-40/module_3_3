def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print()

print_params(b = 25)
print_params(c = [1,2,3])
print()

values_list = [True, 555, 'Text']

values_dict = {'a': 'Text', 'b': True, 'c': 555}

print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = ['int', 555]
print_params(*values_list_2, 42)
