greek_list = ['alpha', 'beta', 'gamma', 'eta', 'alpha', 'omega', 'zeta']
address = ('123 Elm Street', 'Toledo', 'Ohio')
greek_dict = {'alpha': 5, 'beta': 10, 'gamma': 15}
greek_set = {'alpha', 'beta', 'gamma', 'eta', 'zeta'}

print(f"{greek_list[0] = }")
print(f"{address[0] = }")
print(f"{greek_dict['alpha'] = }")
print(f"{greek_list[-1] = }")
print(f"{greek_list[:3] = }")
print(f"{greek_list[3:] = }")
print(f"{greek_list[2:5] = }")
print(f"{greek_list[-2:] = }")
print(f"{'alpha' in greek_list = }")
print(f"{'gamma' in greek_list = }")
print(f"{'zeta' in greek_set = }")
print(f"{len(greek_list) = }")
print(f"{len(address) = }")
print(f"{len(greek_dict) = }")
print(f"{len(greek_set) = }")
print(f"{greek_list.count('alpha') = }")
