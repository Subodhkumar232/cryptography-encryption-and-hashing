import hashlib

message = "Hello World"

hash_object = hashlib.sha256(message.encode())

hashed_value = hash_object.hexdigest()

print("Original Message:", message)
print("SHA-256 Hash:", hashed_value)
