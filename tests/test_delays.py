import time
from humani_py.delays import random_delay

def test_random_delay():
    start = time.time()
    random_delay(1, 2)
    end = time.time()
    assert 1 <= (end - start) <= 2
