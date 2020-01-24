# Convert Nested Dict into Flattened Dict
def flatten(d):
    out = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                deeper = flatten(subdict).items()
                out.update({key + '_' + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out

# Test
d = {'dict1':{'door': '3', 'table': '2'}, 'dict2':{'door': '5', 'light': '4'}}
print(flatten(d))