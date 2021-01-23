# Exploring Dictionary
print(help(dict))
print(dir(dict))

# Declare and Initialize
dict1 = {}
dict1 = {'id':1,'name':'Rajan'}
dict1 = {1:'Apple', 2:'Banana'}
dict1 = {1:'Apple', 2:'Banana', 'list1':[1,2,3,4]}
dict1 = dict({1:'Apple', 2:'Banana'})

print(type(dict1))
print(id(dict1))
print(len(dict1))

dict1 = {'id':1,'name':'Rajan'}
print(dict1)
print(dict1['id'])
print(dict1['name'])

dict1['id']=2
print(dict1)

person={}
person['id']=1
person['full_name']='Rajan Thapa'
person['contact_address']='KTM, Nepal'
person['email']=['rajan@yahoo.com','rjan@gamil.com']
person['mobile']=['123456789','456789123']
print(person)
print(len(person))
print(max(person))
print(min(person))

print(person.get('id'))
print(person.items())
print(person.keys())
print(person.values())
print(person.clear())

dict1 ={}
dict2 ={}
dict1['id']=1
dict2['full_name']='Rajan Thapa'
dict1.update(dict2)
print(dict1)

dict3 = dict1
print(dict3)

dict3 = dict1.copy()
print(dict3)

print("Details %s"%(list(dict3)))
print("Details %s"%(list(dict3.items())))

for key, value in dict3.items():
    print(key, " : ", value, end=";")

countries = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
            'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
            'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
            'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'}

print('\n\n')
for key, value in countries.items():
    print(key," -> ", value)

# Nested Dictionary
countries = {'France':{'Capital':'Paris','Language':'French'},'Spain':{'Capital':'Madrid','Language':'Spanish'},
             'United Kingdom':{'Capital':'London','Language':'English'},
            'United States':{'Capital':'Washington DC','Language':'English'},
            'Italy':{'Capital':'Rome','Language':'Italian'}
            }
