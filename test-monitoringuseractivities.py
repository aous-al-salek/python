from monitoringuseractivities import listusers, diskusagehome       # Imports functions from the monitoringuseractivities modoul.
from pwd import getpwall                                            # Imports functions from the pwd modoul.
from subprocess import check_output                                 # Imports functions from the subprocess modoul.
from systemd import login                                           # Imports functions from the systemd modoul.

returnedlist = listusers()                      # Calles the listusers() function and takes the returned list into a variable.
for item in returnedlist :                      # Loops through the list.
        print(' {:^1} | {:>7} | {:<25} |'.format(item['loggedin'], item['userid'], item['username']), item['shell'])        # Prints values from the returned list in a specific format.



allofmyusers = getpwall()       # Gets all entries from the pw database and stores it in a variable.
listofallofmyusers = []         # Initiates an empty list.
for i in allofmyusers :         # Loops through the entries from the pw database.
    oneofmyusers = i            # Stores an entry into a variable.
    listofallofmyusers.append(oneofmyusers[2])                          # Appends an item from the previous entry to a list.
listofallofmyusers = sorted(listofallofmyusers[:])                      # Sorts the previous list.
nonexistinguser = listofallofmyusers[len(listofallofmyusers)-1] + 1     # Calculates a none-existing userid by taking the last userid in the system and adding 1 to it.

currentuid = check_output("id -u", shell = True)        # Runs a Linux bash command to get the current user's id and stores the output.
currentuid = int(currentuid.decode())       # Decodes the uid and converts it to an integer.

rootid = 0      # Initiates the rootid variable.

userids = [rootid, currentuid, nonexistinguser]     # A list of three uids.
for id in userids :     # Loops through the list of uids.
    try :                   # Error handling.
        print('Disk usage of user with UID {} : {} MB'.format(id, diskusagehome(id)))           # Calles the diskusagehome() function and prints the returned value in a certain format.
    except KeyError :       # Error handling.
        print('Disk usage of user with UID {} : Could not determine disk usage'.format(id))     # If a KeyError error occures a message letting the user know that the usage could not be determine.
