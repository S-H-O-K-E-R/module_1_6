my_dict ={'Nikolay' : 2007, 'Olga' : 1986, 'Nikita' : 1991}
print('Dict:',my_dict)
print('Existing value:',my_dict['Olga'])
print('Not existing value:',my_dict.get('Igor'))
my_dict.update({'Frodo' : 2007,'Max' : 2011})
del_nikita = my_dict.pop('Nikita')
print('Deleted value:',del_nikita)
print('Modified dictionary:',my_dict)

my_set = {4,4,False,8,8,9.9,5,"Hi",6,7,"Hi"}
print('Set:',my_set)
my_set.add(100)
my_set.add((99,11,12))
my_set.discard(False)
print('Modified set:',my_set)