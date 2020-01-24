import re

def validate_ip():
    #ip_str = '2001:0db8:0a0b:12f0:0000:0000:0000:0001'
    ip_str = '192.168.2.10'
    reg = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    if re.match(reg, ip_str):
        print True
    else:
        print False

validate_ip()