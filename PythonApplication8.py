import ipaddress

def int32_to_ip(int32):
    addr = ipaddress.ip_address(int(int32))
    return addr

print(int32_to_ip(input()))