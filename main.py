from hash_table import HashTable, hash_function1, hash_function2

NUM_TESTING_PRODUCTS = 15

TEST_NAMES = [
    "apples",
    "apricots",
    "soup",
    "milk",
    "tofu",
    "poptarts",
    "lightbulbs",
    "soda",
    "chips",
    "cheese",
    "cheetos",
    "ice cream",
    "strawberries",
    "carrots",
    "peanut butter"

]

TEST_INVENTORIES = [
    7,
    6,
    6,
    3,
    1,
    2,
    0,
    5,
    24,
    12,
    7,
    5,
    11,
    20,
    17
]


def main() -> None:
    array_size = 32
    ht = HashTable(array_size)

    # ---------------------------------------------------------
    # FIRST: Test using hash_function1
    # ---------------------------------------------------------
    for i in range(NUM_TESTING_PRODUCTS):
        ht.add(TEST_NAMES[i], TEST_INVENTORIES[i], hash_function1)

    num_col1 = ht.collisions()
    print('Task 1: collision function')
    print(f"Found {num_col1} collisions for hash_function1()")

    ht.display()

    ht.reset()

    # ---------------------------------------------------------
    # SECOND: Test using hash_function2
    # ---------------------------------------------------------
    for i in range(NUM_TESTING_PRODUCTS):
        ht.add(TEST_NAMES[i], TEST_INVENTORIES[i], hash_function2)

    num_col2 = ht.collisions()
    print('Task 2: updated hash function with fewer collisions')
    print(f"Found {num_col2} collisions for hash_function2()")

    ht.display()

    print('Task 3: remove() method')
    print(f"Here is the final hash table with '{TEST_NAMES[9]}' removed\n")
    ht.remove(TEST_NAMES[9], hash_function2)
    ht.display()

    

if __name__ == "__main__":
    main()
