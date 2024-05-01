import json

fields = ['name','html_url','updated_at','visibility']

with open('/workspace/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
    csv_file.write(','.join(fields) + '\n')
    for i in data[:5]:
        values = [str(i[field]) for field in fields]
        csv_file.write(','.join(values) + '\n')