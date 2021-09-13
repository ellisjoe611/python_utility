import time
import typing as T


def time_decorator(func):
    def __wrapper(*args, **kwargs):
        start: float = time.time()
        res: T.Any = func(*args, **kwargs)
        end: float = time.time()
        print(f'function {func.__name__} took {end - start} seconds.')

        return res

    return __wrapper


@time_decorator
def binary_search(arr: T.List[int], target: int) -> int:
    if len(arr) == 0:
        return -1
    
    arr.sort()
    
    first, last = 0, len(arr)
    while first <= last:
        cursor: int = (first + last) // 2
        if arr[cursor] == target:
            return cursor
        elif arr[cursor] > target:
            last = cursor - 1
        else:
            first = cursor + 1

    return -1


@time_decorator
def find_index(arr: T.List[int], target: int) -> int:
    try:
        return arr.index(target)
    except ValueError as e:
        return -1


if __name__ == '__main__':
    arr: T.List[int] = list(i for i in range(1, 100000000) if i % 3 == 0)

    print(binary_search(arr, 840))
    print(binary_search(arr, 445))
    print(binary_search(arr, 180))

    print(find_index(arr, 840))
    print(find_index(arr, 445))
    print(find_index(arr, 180))
