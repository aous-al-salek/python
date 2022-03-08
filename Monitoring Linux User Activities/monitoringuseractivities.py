from pwd import getpwall, getpwuid      # Imports functions from the pwd modoul.
from systemd import login               # Imports functions from the systemd modoul.
from subprocess import check_output     # Imports functions from the subprocess modoul.


def listusers() :
    allofmyusers = getpwall()       # Gets all entries from the pw database and stores it in a variable.
    listofallofmyusers = []         # Initiates an empty list.
    for i in allofmyusers :         # Initiates a loop through the previous variable.
        oneofmyusers = i            # Stores an entry from the pw database in a variable.
        userids = login.uids()                  # Gets the userids of the loggedin users.
        status = oneofmyusers[2] in userids      # Initiates a boolean variable that is true when the value of 'userid' key in the returned list is loggedin.
        if status :             # If the user is logged in.
            loggedin = '*'
        else :                  # If the user is not logged in.
            loggedin = ' '

        dic = {'userid':oneofmyusers[2],'username':oneofmyusers[0],'shell':oneofmyusers[6], 'loggedin':loggedin}     # Extracts specific values and stores them in a dictionary.
        listofallofmyusers.append(dic)      # Appends previous dictionary to a list.
        
    listofallofmyusers = sorted(listofallofmyusers, key = lambda i : i['userid'])       # Sorts the list of dictionary according to a specific value.
    return listofallofmyusers       # Returns the stored list.


def diskusagehome(uid) :
    homedir = getpwuid(uid).pw_dir   # Graps a specific value from the pw database entry of a specific user.
 
    usage = check_output('sudo du -BM -c '+homedir+' | grep total', shell = True)       # Runs a Linux bash command and stores the output.
    usage = usage.decode().split('M')       # Decodes the output and splits it into a list.
    
    return usage[0]     # Returns the first item from the previous list.
