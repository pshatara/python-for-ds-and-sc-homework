import pylab as plb

A = {
    'a': None,
    'b': None,
    'c': None,
    'd': None,
    'e': None
}

def assign_values(dict):
    for key in dict:
        dict[key] = plb.randint(0, 11)
    return dict

B = assign_values(A)

def reassign_values(dict):
    for key in dict:
        if dict[key] < 5:
            dict[key] = plb.normal(2, 3, 256)
            plb.hist(dict[key], density=True, bins=24)
            plb.pause(1)
            plb.close()
    return dict

C = reassign_values(B)

C['a'] = C.pop('b')

C['c'] = C['d']
del C['d']

print('A == B == C: ', A == B == C)