"""Test file for hash table."""

import io
import pytest


file = io.open("/etc/dictionaries-common/words")
word_file = file.read()
WORDS = word_file.split("\n")


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
    ht = HashTable(5, 'bernstein')
    ht.set('d', 0)
    ht.set('e', 1)
    ht.set('a', 2)
    ht.set('b', 3)
    ht.set('c', 4)
    return ht


@pytest.fixture
def get_test_ht():
    """A hash table filled from /usr/share/dict/words."""
    from hash_table import HashTable
    ht = HashTable(10000)
    for i in WORDS:
        ht.set(i, i)
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


def test_init_no_hash_type(empty_ht):
    """Set the hash type to additive if none is given."""
    assert empty_ht._hash_type == 'additive'


def test_init_with_hash_type(pop_ht):
    """Set hash type to the given type."""
    assert pop_ht._hash_type == 'bernstein'


def test_init_with_bad_hash_type():
    """Test that init throws a value error if something other than additive and bernstein is given."""
    from hash_table import HashTable
    message = 'The second argument of hash type must be either additive or bernstein.'
    with pytest.raises(TypeError, message=message):
        HashTable(2, 'Manitoba')


def test_additive(empty_ht):
    """Test the hash method returns the appropriate table index."""
    assert empty_ht._additive('apple') == 530 % empty_ht._size


def test_bernstein(empty_ht):
    """Test that bernstein returns the appropriate table index."""
    assert empty_ht._bernstein('apple') == 119184914 % empty_ht._size


def test_set_empty_bucket(empty_ht):
    """Test that set puts the value in the appropriate bucket."""
    empty_ht.set('a', 1)
    assert empty_ht._table[17] == [('a', 1)]


def test_set_populated_bucket(pop_ht):
    """Test that set puts a value in the next index of a populated bucket."""
    pop_ht.set('seattle', 'second index')
    assert pop_ht._table[1] == [('e', 1), ('seattle', 'second index')]


def test_set_non_string_key_given(pop_ht):
    """Test that the key argument must be a string."""
    assert pop_ht.set(12, 'wrong') == 'Key must be a string.'


def test_get_single_item_in_bucket(pop_ht):
    """Test that get retrives the value paired with the given key."""
    assert pop_ht.get('a') == 2


def test_get_multiple_items_in_bucket(pop_ht):
    """Test that get retrives the value paired with the given key."""
    pop_ht.set('seattle', 1234567890)
    assert pop_ht.get('seattle') == 1234567890


def test_hash_additive(empty_ht):
    """Test that hash returns additive hash when additive is the hash type."""
    assert empty_ht._hash('yo') == 12


def test_hash_bernstein(pop_ht):
    """Test that hash returns bernstein hash when bernstein is the hash type."""
    assert pop_ht._hash('yo') == 4


@pytest.mark.parametrize('word', WORDS)
def ultimate_get_test(get_test_ht, word):
    """Test the get method for a giant hash table of words."""
    assert get_test_ht(word) == word
