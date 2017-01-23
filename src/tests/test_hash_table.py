"""Test file for hash table."""

import pytest


@pytest.fixture
def empty_ht():
    """An empty hash_table."""
    from hash_table import HashTable
    ht = HashTable(20)
    return ht


@pytest.fixture
def pop_ht():
    """A populated hash table."""
    from hash_table import HashTable
    ht = HashTable(5)
    ht.set('apple', 0)
    ht.set('three', 1)
    ht.set('vw', 2)
    ht.set('zero', 3)
    ht.set('cake', 4)
    return ht


def test_init_size(empty_ht):
    """Test that the init function properly sets the size value."""
    assert empty_ht._size == 20


def test_init_table(empty_ht):
    """Test that the init function creates a table of the proper length."""
    assert len(empty_ht._table) == 20


def test_init_nothing_given():
    """Test that a hashtable created with no argument is given a size of 10."""
    from hash_table import HashTable
    ht = HashTable()
    assert ht._size == 10


def test_init_non_int_given():
    """Test that nothing but an int is excepted."""
    from hash_table import HashTable
    message = 'Size must be a positive integer greater than zero.'
    with pytest.raises(TypeError, message=message):
        HashTable('yo')


def test_hash(empty_ht):
    """Test the hash method returns the apropriate table index."""
    assert empty_ht._hash('apple') == 530 % empty_ht._size


def test_set_empty_bucket(empty_ht):
    """Test that set puts the value in the apropriate bucket."""
    empty_ht.set('a', 1)
    assert empty_ht._table[17] == [1]


def test_set_populated_bucket(pop_ht):
    """Test that set puts a value in the next index of a populated bucket."""
    pop_ht.set('seattle', 'second index')
    assert pop_ht._table[4] == [4, 'second index']


def test_set_non_string_key_given(pop_ht):
    """Test that the key argument must be a string."""
    assert pop_ht.set(12, 'wrong') == 'Key must be a string.'


def test_get_single_item_in_bucket(pop_ht):
    """Test that get retrives the value paired with the given key."""
    assert pop_ht.get('vw') == 2
