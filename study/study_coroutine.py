import time


def count():
    while True:
        t: int = yield
        print(f"sleeping for {t} seconds...")
        time.sleep(t)
        print("1111")
        print(f"{t} done")


co = count()
next(co)

co.close()


a = {'name': 'a', 'name': 'b'}
print(list(a.keys()))