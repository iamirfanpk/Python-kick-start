import requests
import json


print('Loading.......API')
print('''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░█▀▀░█░█░█▀█░█▄█░░░█▀█░█▀█░█▀█░░░
░░░░█▀▀░▄▀▄░█▀█░█░█░░░█▀█░█▀▀░█▀▀░░░
░░░░▀▀▀░▀░▀░▀░▀░▀░▀░░░▀░▀░▀░░░▀░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
+----------------------------------+
| Author: Irfan  |  version: 2.0   |
+----------------------------------+
    ''')


response = requests.get('https://tinkerhubfc-results-api.herokuapp.com/results/')
data = response.text
results = json.loads(data)


reg_no = input('Register number : ')
password  = input('Password        : ')

print()

if reg_no == password:
    
    result = results[reg_no]

    name = result['Name']
    dept = result['Department']
    scores = result['scores']
    total = 0

    for value in scores.values():
        total = total + value

    Spga = total / 50    


    print('+----------------------------------+')
    print(f'   Name       : {name}          ')
    print(f'   Department : {dept}          ')
    print('+----------------------------------+')
    print('|           Score List             |')
    print('+----------------------------------+')


    for key,value in scores.items():
        print(f'{key} :  {value}')

    print('+----------------------------------+')    

        
    print(f'| SPGA      :          {Spga}        |')
    print('+----------------------------------+')

else:
    print('Register number or password incorrect')          
          