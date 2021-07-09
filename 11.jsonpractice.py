import json

person1 = {'first':'sabi','last':None}
person2 = {'first':'kani','last':'kapoor'}
person3 = {'first':'mutharasi','last':'k'}

family = {'members':[person1,person2,person3]}

make_json = json.dumps(family)
print(make_json)

print()
print()

result = json.loads(make_json)

for item in result['members'] :
    if item['last'] != None:
        print('First ' + item['first'])
        print('last ' + item['last'])

