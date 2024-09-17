d = {'a': 40, 'b': 20, 'c': 40, 'w': 50}
nd = {}
import re
for i in set(d.values()):
    obj = re.findall(rf"'(\w+)'(?=: {i})", str(d))
    nd[i] = obj if len(obj) > 1 else obj[0]

print(nd)
