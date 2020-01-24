import regex as re
def parseIP():
    raw_ip_list = ['abc' '10.1.1.1/32' 'aabbcc']
    for n in raw_ip_list:
        ip = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}/\d{1,2}', n)
        if (ip == ""):
            continue
        else:
            print ip

parseIP()

