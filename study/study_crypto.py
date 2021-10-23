import os
import sys

key_bytes: bytes = os.urandom(16)
key: str = key_bytes.hex()
print(key_bytes)
print(key)
print(key.encode(encoding="utf-8"))

print(sys.getrefcount(key_bytes))
print(sys.getrefcount(key))
