import sys
import gc

a = "hello world"
b = a
c = b

print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(c))

print(gc.get_threshold())
