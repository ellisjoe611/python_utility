import typing as T

m: T.Dict[str, str] = {
    "q": "qwer",
    "a": "asdf",
    "z": "zxcv"
}
l: T.List[str] = {'q', 'a', 'z'}

print(l)
print(*l)

print(m)