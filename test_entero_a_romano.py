from main import *


def test_romano_336():
    assert romanos(336) == 'CCCXXXVI'

def test_romano_3999():
    assert romanos(3999) == 'MMMCMXCIX'

def test_romano_3999():
    assert romanos(1713) == 'MDCCXIII'