"""Tests for our Trie tree implementation."""


import pytest


@pytest.fixture
def empty_tt():
    """Empty trie tree."""
    from trie_tree import TrieTree
    tt = TrieTree()
    return tt


@pytest.fixture
def pop_tt():
    """Populated trie tree."""
    from trie_tree import TrieTree
    tt = TrieTree()
    tt.insert('there')
    tt.insert('their')
    return tt


@pytest.fixture
def tea_trie():
    """Populated trie tree."""
    from trie_tree import TrieTree
    tt = TrieTree()
    tt.insert("teapot")
    tt.insert("teabags")
    tt.insert("teabag")
    return tt


def test_insert(empty_tt):
    """Test the insert method adds a string to the tree that is not already in it."""
    empty_tt.insert('their')
    assert empty_tt._root == {'t': {'h': {'e': {'i': {'r': {'$': {}}}}}}}


def test_insert_populated_tree(pop_tt):
    """Test the insert on a tree that already has words in it."""
    pop_tt.insert('they\'re')
    assert pop_tt._root == {'t': {'h': {'e': {'y': {'\'': {'r': {'e': {'$': {}}}}}, 'r': {'e': {'$': {}}}, 'i': {'r': {'$': {}}}}}}}


def test_insert_word_already_in_tree(pop_tt):
    """Test that if a word already in the tree isn't added again."""
    pop_tt.insert('they\'re')
    pop_tt.insert('they\'re')
    assert pop_tt._root == {'t': {'h': {'e': {'y': {'\'': {'r': {'e': {'$': {}}}}}, 'r': {'e': {'$': {}}}, 'i': {'r': {'$': {}}}}}}}


def test_insert_not_string(empty_tt):
    """Test a type error is raised if anything but a string is inserted."""
    message = 'Please enter a string.'
    with pytest.raises(TypeError, message=message):
        empty_tt.insert(None)


def test_contains_true(pop_tt):
    """Test that the contains method returns true if the word is in the tree."""
    assert pop_tt.contains('there') is True


def test_contains_false(empty_tt):
    """Test that the contains method returns false if the word is not in the tree."""
    assert empty_tt.contains('their') is False


def test_contains_wrong_type(pop_tt):
    """Test that the contains method called with the wrong type returns false."""
    assert pop_tt.contains(4) is False


def test_remove_exisiting_word(tea_trie):
    """Test remove method on existing word in trie tree."""
    tea_trie.remove("teabag")
    assert tea_trie.size() == 2
    assert tea_trie._root == {'t': {'e': {'a': {'b': {'a': {'g': {'s': {'$': {}}}}}, 'p': {'o': {'t': {'$': {}}}}}}}}


def test_remove_word_not_in_trie(tea_trie):
    """Test remove method on a non-existing word in trie tree."""
    with pytest.raises(KeyError):
        tea_trie.remove("tea")


def test_remove_word_in_empty_trie(empty_tt):
    """Test you can't remove a word in an empty trie."""
    with pytest.raises(KeyError):
        empty_tt.remove("word")


def test_remove_word_in_pop_trie_changes_size(pop_tt):
    """."""
    pop_tt.remove("their")
    assert pop_tt.size() == 1


def test_remove_word_in_pop_trie_changes_root(pop_tt):
    """Test remove function removes parts of the word from root."""
    pop_tt.remove("their")
    assert pop_tt._root == {'t': {'h': {'e': {'r': {'e': {'$': {}}}}}}}
