import pickle
import hashlib

def hash_pickle(obj):
    return hashlib.sha256(pickle.dumps(obj)).hexdigest()

def test_basic_objects():
    obj = [1, 2, 3, 'a', 'b', 'c']
    assert hash_pickle(obj) == hash_pickle(obj)

def test_nested_structures():
    obj = {'a': [1, 2, 3], 'b': {'x': 'y'}}
    assert hash_pickle(obj) == hash_pickle(obj)

def test_recursive_structure():
    obj = []
    obj.append(obj)
    assert hash_pickle(obj) == hash_pickle(obj)

def test_floating_point_accuracy():
    obj = 0.1 + 0.2
    assert hash_pickle(obj) == hash_pickle(obj)
