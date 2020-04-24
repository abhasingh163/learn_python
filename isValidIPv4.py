def isValidIPv4(ipAddr):
    ip_parts = ipAddr.split('.')
    if len(ip_parts) != 4:
        return False
    for x in ip_parts:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

ipAddr="1001.148.184.23"
print(isValidIPv4(ipAddr))