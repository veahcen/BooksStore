import hashlib

myHash = input('Введите пароль ')

hasgobj = hashlib.md5(myHash.encode())
print(hasgobj.hexdigest())


inputhash = hasgobj.hexdigest()
print(inputhash)
