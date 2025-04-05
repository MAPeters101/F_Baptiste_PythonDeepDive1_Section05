
def add_item(name, quantity, unit, grocery_list):
    grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
    return grocery_list

store1 = []
store2 = []

add_item('banana', 2, 'units', store1)
add_item('milk', 1, 'liter', store1)
print(store1)

add_item('python', 1, 'medium-rare', store2)
print(store2)
print('.'*80)





