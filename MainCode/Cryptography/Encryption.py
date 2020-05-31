from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Hello I'm Ashish Chaurasia")
print(token)
print(f.decrypt(token))