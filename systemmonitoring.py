from systemd import journal
from datetime import datetime,timedelta
from socket import create_connection
from contextlib import closing
from subprocess import check_output

def recentlogmessages(service, l='WARNING') :
    returnlist = []     # Initiates an empty list to be returned.

    units = check_output("systemctl list-unit-files", shell = True).decode().split(" ")     # Graps all the unit files on the system
    l = "\n"    # Initiates a variable
    if l+service not in units :     # If a specific string exists
        returnlist.append("No shuch unit exists!")     # A string a appended to the returnlist
        return returnlist   # The list gets returned

    x = datetime.now() - timedelta(hours=24, minutes=30)    # Stores what the time was 24h and 30min ago.
    j = journal.Reader()    # Reades the jornal and stores it in a variable.
    j.seek_head()   # Sortes the read journal from latest to oldest.
    
    # Defines the wanted prority according to an optional argument that can be sent in with the function call.
    if l == 'INFO' :
        j.log_level(journal.LOG_INFO)
    elif l == 'WARNING' :
        j.log_level(journal.LOG_WARNING)
    elif l == 'ERR' :
        j.log_level(journal.LOG_ERR)
    elif l == 'EMERG' :
        j.log_level(journal.LOG_EMERG)
    elif l == 'ALERT' :
        j.log_level(journal.LOG_ALERT)
    elif l == 'CRIT' :
        j.log_level(journal.LOG_CRIT)
    elif l == 'NOTICE' :
        j.log_level(journal.LOG_NOTICE)
    elif l == 'DEBUG' :
        j.log_level(journal.LOG_DEBUG)

    j.add_match(_SYSTEMD_UNIT=service)      # Defines the sevice which the loges belong to according to an argument sent in with the function call.

    lst = []        # Initiates an empty list.
    for entry in j:     # Loops through the filtered loges.
        lst.append(entry)   # Appendes them to the previous list.
    y = 1   # Initiates an int variable.
    z = 0   # Initiates an int variable.
    try :
        while y < 11 :      # Limits the number of messages to 10.
            dic = lst[z]    # Stores a log entry in a variable.
            if dic['__REALTIME_TIMESTAMP'] >= x:    # Compares the time stamp of the entry to the time 24h and 30min ago.
                returnlist.append(dic['MESSAGE'])   # If the previous condition is true then it appendes the message to the return-list.
            else :      # Otherwise the loop breakes.
                break
            y += 1  # Increases the variable by 1.
            z += 1  # Increases the variable by 1.
    except IndexError :     # If the previous failes then it passes.
        pass
    #if returnlist == [] :   # If the reuturn-list containes no log messages then it returnes a message letting the user know.
    #    print('There are no logs for this unit!')
    return returnlist   # Returnes the return-list.




def probetcpport(ip, port) :
    try :
        with closing(create_connection((ip, port), timeout=2)) :    # Tries to open a socket connection that would be closed afterwards.
            pass
    except :
        success = False     # If it failes that gets recorded in a boolean variable.
    else :
        success = True      # If it succeedes that gets recorded in a boolean variable.
    return success      # The boolean variable gets returned.
