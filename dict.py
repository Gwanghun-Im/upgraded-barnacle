city_dict = {}
while True:
    try:
        name, code = input().split('\t')
        city_dict[name] = code
    except:
        break

print(city_dict)