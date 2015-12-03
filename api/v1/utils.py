from hashlib import md5

def encrytovalue(value):
    m = md5()
    if not isinstance(value,bytes):
        value = value.encode()
    m.update(value)
    return m.hexdigest()
