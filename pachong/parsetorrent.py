# -*- coding: utf-8 -*-

import os

def decode_int(x, f):
    f += 1
    newf = x.index('e', f)
    n = int(x[f:newf])
    if x[f] == '-':
        if x[f + 1] == '0':
            raise ValueError
    elif x[f] == '0' and newf != f+1:
        raise ValueError
    print("pos %d, int:%d" % (f, n))
    return (n, newf+1)

def decode_string(x, f):
    colon = x.index(':', f)
    n = int(x[f:colon])
    if x[f] == '0' and colon != f+1:
        raise ValueError
    colon += 1
    print("pos %d str:%s" % (colon, x[colon:colon+n]))
    return (x[colon:colon+n], colon+n)

def decode_list(x, f):
    r, f = [], f+1
    while x[f] != 'e':
        v, f = decode_func[x[f]](x, f)
        r.append(v)
    return (r, f + 1)

def decode_dict(x, f):
    r, f = {}, f+1
    while x[f] != 'e':
        k, f = decode_string(x, f)
        r[k], f = decode_func[x[f]](x, f)
    return (r, f + 1)

decode_func = {}
decode_func['l'] = decode_list
decode_func['d'] = decode_dict
decode_func['i'] = decode_int
decode_func['0'] = decode_string
decode_func['1'] = decode_string
decode_func['2'] = decode_string
decode_func['3'] = decode_string
decode_func['4'] = decode_string
decode_func['5'] = decode_string
decode_func['6'] = decode_string
decode_func['7'] = decode_string
decode_func['8'] = decode_string
decode_func['9'] = decode_string

def bdecode(x):
    r=dict()
    l=0
    try:
        r, l = decode_func[x[0]](x, 0)
    except (IndexError, KeyError, ValueError):
        print("not a valid bencoded string")
    if l != len(x):
        print("invalid bencoded value (data after valid prefix)")
    print(r)
    return r

#from types import StringType, IntType, LongType, DictType, ListType, TupleType

#
#class Bencached(object):
#
#    __slots__ = ['bencoded']
#
#    def __init__(self, s):
#        self.bencoded = s
#
#def encode_bencached(x,r):
#    r.append(x.bencoded)
#
#def encode_int(x, r):
#    r.extend(('i', str(x), 'e'))
#
#def encode_bool(x, r):
#    if x:
#        encode_int(1, r)
#    else:
#        encode_int(0, r)
#        
#def encode_string(x, r):
#    r.extend((str(len(x)), ':', x))
#
#def encode_list(x, r):
#    r.append('l')
#    for i in x:
#        encode_func[type(i)](i, r)
#    r.append('e')
#
#def encode_dict(x,r):
#    r.append('d')
#    ilist = x.items()
#    ilist.sort()
#    for k, v in ilist:
#        r.extend((str(len(k)), ':', k))
#        encode_func[type(v)](v, r)
#    r.append('e')
#
#encode_func = {}
#encode_func[Bencached] = encode_bencached
#encode_func[int] = encode_int
##encode_func[long] = encode_int
#encode_func[str] = encode_string
#encode_func[list] = encode_list
#encode_func[tuple] = encode_list
#encode_func[dict] = encode_dict
#
#try:
#    from types import BooleanType
#    encode_func[BooleanType] = encode_bool
#except ImportError:
#    pass
#
#def bencode(x):
#    r = []
#    encode_func[type(x)](x, r)
#    return ''.join(r)

def GetContent(file):
    lens = os.path.getsize(file)
    ff = open(file,"rb")
    tt = ff.read(lens)
    ff.close()
    tt = repr(tt)
    return tt

def main():
    
    file = "fe7e1b90fc7a311ca89fc945c6aea62686799cef.torrent"
    content = GetContent(file)
    content = content[2:]
    bdecode(content)
    print("ok")
    
if (__name__ == "__main__"):
    main()
