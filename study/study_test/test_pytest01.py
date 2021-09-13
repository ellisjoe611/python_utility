from typing import List


def average(a: List) -> float:
    return sum(a) / len(a)


def get_mapped_array(x: int) -> list:
    return [x*i for i in range(1, 6)]


def test_avg():
    assert average([3, 2, 4]) == 3
    assert average([3, 2, 5]) == 3.3333333333333335


def test_generator():
    assert get_mapped_array(2) == [2,4,6,8,10]
