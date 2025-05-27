def build_profile(first, last, **other_info):
    user_info = {}
    user_info['first'] = first
    user_info['last'] = last
    for key, value in other_info.items():
        user_info[key] = value

    return user_info

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}