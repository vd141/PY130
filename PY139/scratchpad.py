def combine_data(data_entries, **kwargs):
    # type checking
    if not isinstance(data_entries, list):
        raise TypeError('data_entries must be a list.')
    for patient_data in data_entries:
        if not isinstance(patient_data, dict):
            raise TypeError('All entries must be dictionaries.')
    
    for patient_data in data_entries:
        for attribute, value in kwargs.items():
            patient_data[attribute] = value
    
    return data_entries

records = [{'name': 'Jane', 'age': 30}, {'name': 'Jake', 'age': 25}]
updated_records = combine_data(records, location='New York', age=35)
print(updated_records)
# Pretty printed for clarity; your code can print everything
# on one long line.
# [
#     {'name': 'Jane', 'age': 35, 'location': 'New York'},
#     {'name': 'Jake', 'age': 35, 'location': 'New York'},
# ]

try:
    combine_data("not a list", name='Charlie')
except TypeError as e:
    print(e) # data_entries must be a list.

try:
    combine_data([{'name': 'Alice', 'age': 30}, 'not a dictionary'],
                 location='New York')
except TypeError as e:
    print(e) # All entries must be dictionaries.