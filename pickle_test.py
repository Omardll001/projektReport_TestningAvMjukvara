import pickle
import hashlib
import threading

def hash_pickle(obj):
    # Serialize the object with pickle and return its SHA-256 hash.
    pickled_data = pickle.dumps(obj)
    return hashlib.sha256(pickled_data).hexdigest()

def test_basic_types():
    data = [
        123,  # integer
        123.456,  # float
        "hello",  # string
        [1, 2, 3],  # list
        (1, 2, 3),  # tuple
        {1, 2, 3},  # set
        {'a': 1, 'b': 2},  # dictionary
    ]
    for item in data:
        try:
            assert hash_pickle(item) == hash_pickle(item)
            print(f"Test passed for item: {item}")
        except AssertionError:
            print(f"Test failed for item: {item}")

def test_complex_structures():
    data = [
        {'a': [1, 2, 3], 'b': {'x': 'y'}},
        [[1, 2], [3, 4, 5], [6]],
        {"key1": (1, 2), "key2": {3, 4}},
    ]
    for item in data:
        try:
            assert hash_pickle(item) == hash_pickle(item)
            print(f"Test passed for item: {item}")
        except AssertionError:
            print(f"Test failed for item: {item}")

def test_recursive_structure():
    obj = []
    obj.append(obj)
    try:
        assert hash_pickle(obj) == hash_pickle(obj)
        print("Test passed for recursive structure")
    except AssertionError:
        print("Test failed for recursive structure")

def test_floating_point_accuracy():
    obj = 0.1 + 0.2
    try:
        assert hash_pickle(obj) == hash_pickle(obj)
        print("Test passed for basic floating point accuracy")
    except AssertionError:
        print("Test failed for basic floating point accuracy")
    
    obj1 = 0.001 + 0.002
    obj2 = 0.00100 + 0.002000
    try:
        assert hash_pickle(obj1) == hash_pickle(obj2)
        print("Test passed for floating point accuracy")
    except AssertionError:
        print("Test failed for floating point accuracy")

# Testing customized objects
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def print_info(self):
        print(self.name)
        print(self.age)

    def increaseage(self, num):
        self.age += num

class Ahmad:
    pass

class Gubran:
    pass
    
def test_custom_object():
    p1 = Person("Omar", 23)
    try:
        assert hash_pickle(p1) == hash_pickle(p1)
        print("Test passed for custom object (not modified)")
    except AssertionError:
        print("Test failed for custom object (not modified)")

def test_custom_object_mod():
    p1 = Person("Omar", 23)
    p1.increaseage(5)
    try:
        assert hash_pickle(p1) == hash_pickle(p1)
        print("Test passed for custom object (modified)")
    except AssertionError:
        print("Test failed for custom object (modified)")

def test_circular_references():
    a = Ahmad()
    b = Gubran()
    a.b = b
    b.a = a
    try:
        assert hash_pickle(a) == hash_pickle(a)
        print("Test passed for circular references")
    except AssertionError:
        print("Test failed for circular references")

# Testing more complex objects 
def test_binary_data():
    binary_data = bytearray([120, 3, 255, 0, 100])
    try:
        assert hash_pickle(binary_data) == hash_pickle(binary_data)
        print("Test passed for binary data")
    except AssertionError:
        print("Test failed for binary data")


def test_shared_objects():
    shared_obj = {"numbers": [1, 2, 3], "letters": ["a", "b", "c"]}
    hash_values = []

    def pickle_shared_object():
        hash_values.append(hash_pickle(shared_obj))

    threads = [threading.Thread(target=pickle_shared_object) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    try:
        assert all(h == hash_values[0] for h in hash_values)
        print("Test passed for shared objects across threads")
    except AssertionError:
        print("Test failed for shared objects across threads")


def main():
    test_basic_types()
    test_complex_structures()
    test_recursive_structure()
    test_floating_point_accuracy()
    test_custom_object()
    test_custom_object_mod()
    test_circular_references()
    test_binary_data()
    test_shared_objects()


if __name__ == "__main__":
    main()