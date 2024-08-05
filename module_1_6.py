my_dict = {'Denis': 2000, 'Anton': 2001, 'Max': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Max'))
print('Not existing value:', my_dict.get('Igor'))
my_dict.update({'Igor': 2003, 'Alex': 2004})
del_key = my_dict.pop('Denis')
print('Deleted value:', del_key)
print('Modified dictionary:', my_dict)

print('-' * 20)

my_set = {1, 1, 2, 3, 'alex'}
print('Set:', my_set)
my_set.add(5.5)
my_set.add(77)
my_set.discard('alex')
print('Modified set:', my_set)
