from aggregatelog import aggregatelog

returneddic = aggregatelog('access.log')       # Calles a function with the file path as an argument and stores the returned nested dictionary in a variable.

sorted_ips = sorted(returneddic['IPaddress'].items(), key = lambda kv : kv[1])  # Stores the IP dictionary sorted in a variable.
the_ip = sorted_ips[-1]     # Stores the first pair from the sorted dictionary in a variable, as it has the highst value.

sorted_paths = sorted(returneddic['Path'].items(), key = lambda kv : kv[1])     # Stores the path dictionary sorted in a variable.
the_path = sorted_paths[-1]     # Stores the first pair from the sorted dictionary in a variable, as it has the highst value.

sorted_methods = sorted(returneddic['Method'].items(), key = lambda kv : kv[1])     # Stores the method dictionary sorted in a variable.
the_method = sorted_methods[-1]     # Stores the first pair from the sorted dictionary in a variable, as it has the highst value.

sorted_months = sorted(returneddic['Month'].items(), key = lambda kv : kv[1])       # Stores the month dictionary sorted in a variable.
the_month = sorted_months[-1]       # Stores the first pair from the sorted dictionary in a variable, as it has the highst value.

# Prints the wnted values in the wanted format.
print('Number of unique IP-addresses:', len(returneddic['IPaddress']))
print('    Most popular value is:', the_ip[0], '({} times)'.format(the_ip[1]))

print('Number of unique paths:', len(returneddic['Path']))
print('    Most popular value is:', the_path[0], '({} times)'.format(the_path[1]))

print('Number of unique HTTP methods:', len(returneddic['Method']))
print('    Most popular value is:', the_method[0], '({} times)'.format(the_method[1]))

print('Number of unique months:', len(returneddic['Month']))
print('    Most popular value is:', the_month[0], '({} times)'.format(the_month[1]))
