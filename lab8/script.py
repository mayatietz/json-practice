import requests

url = "https://github.com/nmagee/ds2002-course/blob/main/labs/data/schacon.repos.json"

response = requests.get(url)
fields = ['name', 'html_url', 'updated_at', 'visibility']
  
with open('chacon.csv', 'w') as csv_file:
    csv_file.write(','.join(fields) + '\n')
    for i in response.json():
        values = [str(i[field]) for field in fields]
        csv_file.write(','.join(values) + '\n')