from re import search, match

def aggregatelog(log_file) :
    with open(log_file, 'r') as file :      # Opens the log file.
        contents = file.readlines()     # Reades the lines and stores them in a variable.
    dic = {'IPaddress' : {}, 'Path' : {}, 'Method' : {}, 'Month' : {}}      # Initiates an organized nested dictionary.
    for item in contents :      # Loops through the file containing the lines.
        item = item.rstrip()        # Removes blank lines.
        if len(item) == 0 :         # Removes blank lines.
            continue                # Skippes the rest of the code in the loop and begines with the next lopp object.

        ip = match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", item).group()     # Regular expression mating IPv4 addresses.
        try :
            dic['IPaddress'][ip] = dic['IPaddress'][ip] + 1     # Try to add 1 to the value of a key.
        except KeyError :
            dic['IPaddress'][ip] = 1       # If previous failes then it addes a new key with 1 as a value.

        path = search(r" (?P<path>(([.]+)|[http]|[/])(.+)?) HTTP/", item).group("path") # Regular expression searching for page pathes.
        try :
            dic['Path'][path] = dic['Path'][path] + 1     # Try to add 1 to the value of a key.
        except KeyError :
            dic['Path'][path] = 1       # If previous failes then it addes a new key with 1 as a value.

        method = search(r'(?P<method>((([A-Z]|[a-z])(([a-z])+|([A-Z])+)?))) (([.]+)|[http]|[/])(.+)? HTTP/', item).group("method")    # Regular expression searching for HTTP methods.
        try :
            dic['Method'][method] = dic['Method'][method] + 1     # Try to add 1 to the value of a key.
        except KeyError :
            dic['Method'][method] = 1       # If previous failes then it addes a new key with 1 as a value.

        month = search(r"[/](?P<month>[A-Z][a-z][a-z])[/]", item).group("month")        # Regular expression searching for monthes.
        try :
            dic['Month'][month] = dic['Month'][month] + 1     # Try to add 1 to the value of a key.
        except KeyError :
            dic['Month'][month] = 1       # If previous failes then it addes a new key with 1 as a value.

    return dic      # Returnes the dictionary.
