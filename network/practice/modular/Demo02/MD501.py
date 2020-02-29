import hashlib
md = hashlib.md5()
md.update("这是常识".encode("UTF-8"))
print(md.hexdigest())