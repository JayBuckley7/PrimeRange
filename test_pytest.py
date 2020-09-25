from PrimeGenerator import PrimeNumberGenerator as p

def test_isPrime_small_true():
    numbers = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 }
    for num in numbers:
        assert  p.is_Prime(p, num) == True
        

def test_isPrime_negative_false():
    numbers = { -2, -3, -5, -7, -11, -13, -17, -19, -23, -29 }
    for num in numbers:
        assert  p.is_Prime(p, num) == True

def test_isPrime_positive_false():
    numbers = { 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25 }
    for num in numbers:
        assert  p.is_Prime(p, num) == False

def test_isPrime_big():
    numbers =  {104677,104681, 104683, 104693, 104701, 104707, 104711, 104717, 104723, 104729 }
    for num in numbers:
        assert  p.is_Prime(p, num) == True


def test_isPrime_0_1():
    numbers = [0, 1]
    for num in numbers:
        assert  p.is_Prime(p, num) == False


def test_generate_0_1():
    numbers = [0,1]
    start = 0
    end = 1
    primes = []
    assert  p.generate(p,start,end) == primes
    assert  p.generate(p,end,start) == primes

def test_generate_small_true():
    numbers = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 ]
    primes = []
    start = 2
    end = 29
    assert  p.generate(p,start,end) == numbers
    assert  p.generate(p,end,start) == numbers
        

def test_generate_negative_false():
    numbers = [ -2, -3, -5, -7, -11, -13, -17, -19, -23, -29 ]
    primes = [-29, -23, -19, -17, -13, -11, -7, -5, -3, -2]
    start = -2
    end = -29
    assert  p.generate(p,start,end) == primes
    assert  p.generate(p,end,start) == primes

def test_generate_positive_false():
    numbers = [ 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25 ]
    primes = [5, 7, 11, 13, 17, 19, 23]
    start = 4
    end = 25
    assert  p.generate(p,start,end) == primes
    assert  p.generate(p,end,start) == primes

def test_generate_big():
    numbers =  [104677,104681, 104683, 104693, 104701, 104707, 104711, 104717, 104723, 104729 ]
    start = 104677
    end = 104729
    assert  p.generate(p,start,end) == numbers
    assert  p.generate(p,end,start) == numbers
    


