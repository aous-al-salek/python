from systemmonitoring import probetcpport
from systemmonitoring import recentlogmessages

# Calles the function and sends (an) argumnet(s), loops through the returned list and then prints the log messages.
for i in recentlogmessages('systemd-logind.service', 'INFO') :
    print(i)
for i in recentlogmessages('systemd-logind.service') :
    print(i)

for i in recentlogmessages('ssh.service', 'ALERT') :
    print(i)
for i in recentlogmessages('ssh.service',) :
    print(i)

for i in recentlogmessages('nosuchservice.service', 'EMERG') :
    print(i)
for i in recentlogmessages('nosuchservice.service',) :
    print(i)

for i in recentlogmessages('networking.service', 'ERR') :
    print(i)
for i in recentlogmessages('networking.service') :
    print(i)




# ips = ['10.208.10.142', '10.208.10.141', '127.0.0.1', 'mail.his.se', 'google.com', 'localhost']     # Initiates a list of IPs, hostnames and domain names.
# ports = [22, 80, 25, 993, 443, 21]      # Initiates a list of port numbers.
# for ip, port in zip(ips, ports) :       # Loops through the previous lists and zipes them together.
#     probe = probetcpport(ip, port)      # Calles a function with items from the previous lists as arguments and stores the returned value in a variable.
#     # Deppending on the returned value an appropriate message gets printed.
#     if probe :
#         print("Probing {:<15} on port {:<5} : success".format(ip, port))
#     else :
#         print("Probing {:<15} on port {:<5} : fail".format(ip, port))
