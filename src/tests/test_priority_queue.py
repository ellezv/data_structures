""""""

import pytest

def test_insert():
    """"""
    q = Priority_Queue()
    q.insert(('a', 1))
    assert q._container[1][0] == 'a'

def test_insert_none():
    """"""
    q = Priority_Queue()
    with pytest.raises(ValueError, message='Must insert with tuple!'):
        q.insert()
    
def test_insert_wrong_value():
    """"""
    q = Priority_Queue(5)
    with pytest.raises(ValueError, message='Must insert with tuple!'):
        q.insert()

def test_insert_wrong_value():
    """"""
    q = Priority_Queue(('a', 1))
    
    with pytest.raises(ValueError, message='Must insert with tuple!'):
        q.insert()