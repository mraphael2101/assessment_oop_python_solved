from animals.bird import Bird
from animals.bird_types.eagle import Eagle
from animals.bird_types.penguin import Penguin
from animals.behaviours.hop import Hop

"""
The purpose of this exercise is to demonstrate a few of the key concepts
of Object-Oriented Programming in Python.

Using the sample classes provided in the animals package,
complete the exercise by writing code to implement the following:
1) Multi-Level Inheritance using Interfaces
2) Method Overriding with Abstract classes
3) Method Overloading
4) Encapsulation
5) Polymorphism */
"""


def main():
    print("=== Overridden method (Bird overrides Animal.calculate_random_age) ===")
    # Animal.calculate_random_age would raise NotImplementedError,
    # Bird implements it, Eagle inherits from Bird, so this works:
    Eagle().calculate_random_age()

    print("\n=== Method 'overloading' (simulated) ===")
    # In Python, we simulate overloading with a separate method name:
    Eagle().calculate_random_age_with_val(5)

    print("\n=== Encapsulation via properties ===")
    b = Bird()
    _ = b.age            # get
    b.age = 3            # set
    print("Bird age now:", b.age)

    print("\n=== Polymorphism ===")

    # A) Everything is an object in Python; no cast needed
    penguin1 = Penguin()
    bird1 = penguin1   # treat as Bird (polymorphic assignment)
    bird1_obj = bird1  # also an object
    print("A) bird1 is Penguin:", isinstance(bird1, Penguin), "| also an object:", isinstance(bird1_obj, object))

    # B) Upcast (implicit in Python): assign subtype to supertype reference
    penguin_bird = Penguin()  # using as Bird
    penguin_bird.calculate_random_age()
    print("B) penguin_bird used as Bird, isinstance(Bird):", isinstance(penguin_bird, Bird))

    # C) Downcast (not a thing in Python; you can check and use)
    bird_ref = Penguin()  # dynamic type is Penguin
    if isinstance(bird_ref, Penguin):
        penguin_ref = bird_ref
        print("C) safely treating bird_ref as Penguin:", isinstance(penguin_ref, Penguin))

    print("\n=== Default-like method from mixin (Hop) ===")
    # Java used an anonymous class to reach a default method. In Python,
    # just instantiate Hop or use a class that mixes it in (e.g., Eagle).
    hop = Hop()
    print("Hop.get_max_hop_height():", hop.get_max_hop_height())

    # Or via Eagle, which mixes in Hop:
    eagle = Eagle()
    print("Eagle.get_max_hop_height():", eagle.get_max_hop_height())


if __name__ == "__main__":
    main()