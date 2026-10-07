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
        obj = decode_bytes(obj, encoding)
        # Non-ASCII chars are kept as they are, not escaped.
        ensure_ascii = False

    return json.dumps(obj, ensure_ascii=ensure_ascii, indent=indent)


def decode_bytes(o, encoding):
    if isinstance(o, bytes):
        return o.decode(encoding)

    if isinstance(o, dict):
        rst = {}
        for k, v in o.items():
            rst[decode_bytes(k, encoding)] = decode_bytes(v, encoding)

    elif isinstance(o, (list, tuple)):
        rst = []
        for v in o:
            rst.append(decode_bytes(v, encoding))
    else:
        rst = o

    return rst


def load(s, encoding=None):
    if s is None:
        return None
    if isinstance(s, bytes):
        if encoding is None:
            s = s.decode("utf-8")
        else:
            s = s.decode(encoding)
    rst = json.loads(s)

    return rst
