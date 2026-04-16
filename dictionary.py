my_dict = {"name": "Arushi", "age": 18, "city": "Delhi","country":"India"}

print("Dictionary Items:")
print(my_dict) 

print("Name:", my_dict["name"]) 
print("Age:", my_dict["age"]) 

print("City:", my_dict.get("city")) 
print("Country:", my_dict.get("country"))  

my_dict["age"] = 19
print("Updated Age:", my_dict["age"])

print("Number of items in the dictionary:", len(my_dict))



def concatenate_dictionaries(dict1, dict2, dict3):
  result = {}
  result.update(dict1)
  result.update(dict2)
  result.update(dict3)
  return result

dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}

concatenated_dict = concatenate_dictionaries(dict1, dict2, dict3)
print(concatenated_dict)


def remove_key_from_dict(my_dict, key_to_remove):

  new_dict = my_dict.copy()  
  new_dict.pop(key_to_remove, None) 
  return new_dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'

updated_dict = remove_key_from_dict(my_dict, key_to_remove)

print("Original dictionary:", my_dict)
print("Updated dictionary:", updated_dict)

