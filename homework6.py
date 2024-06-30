# Словари и множества

my_dict = {'Russia':'Moscow', 'Italy':'Rome', 'Georgia':'Tbilisi' }
print('Dict:', my_dict)
print('Existing value:', my_dict['Russia'])
print('Not existing value:', my_dict.get("Australia"))
my_dict.update({'Hungary':'Budapest', 'Belarus':'Minsk'})
print('Deleted value:', my_dict.pop('Italy'))
print('Modified dictionary:', my_dict)

my_set = {False,'1',2.0,3,4,5,6,7,6,5,4,3,2,1}
print('Set:', my_set)
my_set.update({8,9})
my_set.remove('1')
print('Modified set:', my_set)
