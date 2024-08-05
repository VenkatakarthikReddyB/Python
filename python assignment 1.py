import json
# 1.

with open("Downloads/cruise_ship_schema.json", 'r' ) as Json_file_1:
    data_1=json.load(Json_file_1)
print(data_1["crew"])


#2.

Json_File=[]
with open("Downloads/sample-data.json", 'r' ) as Json_file_2:
    for eachLine in Json_file_2:
        Json_File.append(json.loads(eachLine))
    
for i in Json_File:
    print(i['firstName'])


list_a = [0,1,2,3,4,5,6]

# 3. Print 5th element

print("Printing 5th element:", list_a[4])

# 4. Last three elements

print("Print last 3 elements :", list_a[-3:])

# 5. Print Len of the list

dict_a = {'a':1,'b':2}

print("Length of dict_a :",len(dict_a))

# 6. Print keys of the the dictionary dict_a
print("Printing the keys of the dict:",list(dict_a.keys()))

# 7. Print values of the dictionary dict_a
print("Printing Values of the dict :", list(dict_a.values()))

# 8. Print value of the key = b

print("Value of the Key 'b':",dict_a['b'])


