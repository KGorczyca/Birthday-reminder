import pytest

from uniwersary_program import Birthday


''''@pytest.fixture
def person():
    person = Birthday()'''

def test_birthday_initialization():
    person = Birthday('Katarzyna','Kowalska','29.09.1986')
    assert person


'''def test_person_initialization(person):
    assert person'''

'''import pytest

from uniwersary_program import today, Birthday

def test_birthday_initialization():
    person = Birthday('Katarzyna','Kowalska','29.09.1986')
    assert person


def test_first():
    result = '26.10.2020'
    assert today == result

def test_list():
    pass
'''