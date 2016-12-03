import ijson

def f3(seq):
	# Not order preserving
	keys = {}
	for e in seq:
		print('item is ' + e)
		keys[e] = 1
	return keys.keys()

#filename = 'C:\\Users\\andrew.henze\\Documents\\GitHub\\JSONMapInfo\\JSON\\MMR_adm3.json'
filename = 'C:\\Users\\andrew.henze\\Documents\\GitHub\\JSONMapInfo\\JSON\\MMR_adm3_pretty.json'

jsonpath = 'features.item.properties.NAME_1'

with open(filename, 'r') as f:
	objects = ijson.items(f, jsonpath)
	columns = f3(list(objects))

for column in columns:
	print(column)