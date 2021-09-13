import gc
import sys
import tracemalloc


class Foo():
    def __init__(self, new_greetings: str = None) -> None:
        self.__greetings: str = new_greetings is None and "Hello, world!" or new_greetings
    
    def set_greetings(self, new_greetings: str) -> None:
        self.__greetings = new_greetings
    
    def get_greetings(self) -> str:
        return self.__greetings

if __name__ == '__main__':
    tracemalloc.start()
    snapshot_start: tracemalloc.Snapshot = tracemalloc.take_snapshot()

    a: Foo = Foo()
    b: Foo = Foo("파이썬 ㅎㅇ")
    print(a.get_greetings())
    print(b.get_greetings())


    snapshot_status01 = tracemalloc.take_snapshot().compare_to(snapshot_start, 'lineno')
    for stat in snapshot_status01:
        print(str(stat))