import json

# expected behavior to dump '我':
#           source             encoding=None  encoding='utf-8'
# str       '我'               '"\\u6211"'    '"我"'
# bytes    b'\xe6\x88\x91'     TypeError      '"我"'


def dump(obj, encoding="utf-8", indent=None):
    # With an encoding, bytes in obj are first decoded to str with it.
    if encoding is None:
        ensure_ascii = True

    else:
        obj = encode_str(obj, encoding)
        # Non-ASCII chars are kept as they are, not escaped.
        ensure_ascii = False

    return json.dumps(obj, ensure_ascii=ensure_ascii, indent=indent)


def ensure_str(o):
    if isinstance(o, bytes):
        raise TypeError(f"string({o} {type(o)}) must be str if ensure_ascii is True")

    if isinstance(o, dict):
        for k, v in o.items():
            ensure_str(k)
            ensure_str(v)

    elif isinstance(o, (list, tuple)):
        for v in o:
            ensure_str(v)


def encode_str(o, encoding):
    if isinstance(o, bytes):
        return o.decode(encoding)

    if isinstance(o, dict):
        rst = {}
        for k, v in o.items():
            rst[encode_str(k, encoding)] = encode_str(v, encoding)

    elif isinstance(o, (list, tuple)):
        rst = []
        for v in o:
            rst.append(encode_str(v, encoding))
    else:
        rst = o

    return rst


def load(s, encoding=None):
    if s is None:
        return None
    if isinstance(s, bytes):
        if encoding is None:
            s = decode(s, encoding="utf-8")
        else:
            s = decode(s, encoding)
    rst = json.loads(s)

    return rst


def decode(o, encoding):
    if isinstance(o, bytes):
        return o.decode(encoding)

    if isinstance(o, dict):
        rst = {}
        for k, v in o.items():
            rst[decode(k, encoding)] = decode(v, encoding)

    elif isinstance(o, list):
        rst = []
        for v in o:
            rst.append(decode(v, encoding))
    else:
        rst = o

    return rst
