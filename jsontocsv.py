import json

import csv
with open('salonsbyjc.json') as json_file:
    json_data = json.load(json_file)

# Step 1: Parse the JSON array into a Python list of dictionaries


# Step 2: Loop through each dictionary and modify all fields (replace 'o' with 'X')
for item in json_data:
    for key, value in item.items():
        if isinstance(value, str):  # Check if the value is a string
            item[key] = value.replace('\u2013', '-')

# Step 3: Convert the modified list of dictionaries back to a JSON string





 

 
data_file = open('salonsbyjcV2.csv', 'w', newline='',encoding='utf-8')
csv_writer = csv.writer(data_file)
 
count = 0
for data in json_data:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
 
data_file.close()




