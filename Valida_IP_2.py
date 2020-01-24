def valid_ip(s):
    a = s.split(".")
    if len(a) != 4:
        return False
    for x in a:
        if x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

# test
#s = ['asdasdsa', '12323.343122.2342434.324432', '10.1.1.1/32', '192.10.82.40']
s = '192.10.82.40'
#s = 'abcdf'
print(valid_ip(s))