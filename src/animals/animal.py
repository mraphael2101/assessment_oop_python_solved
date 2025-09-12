from __future__ import annotations


class Animal:
    def __init__(self, name: str | None = None) -> None:
        self.age: int = 0
        self.name: str | None = None

        if name is None:
            print("An animal now exists without a name")
        else:
            print(f"A animal now exists and was given the {name}")
            self.name = name

    # Abstract-like method (Python doesn't enforce abstract without using the package abc.ABC))
    def calculate_random_age(self) -> int:
        raise NotImplementedError("Subclasses must implement calculate_random_age")

    # Protected-like method by convention (single underscore)
    def _generate_security_code(self) -> int:
        return 0

    # Encapsulation via property
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("age must be an int")
        if value < 0:
            raise ValueError("age cannot be negative")
        self._age = value

    # Use backing attributes (_age/_name) in properties to avoid recursive self-access
    @property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, value: str | None) -> None:
        if value is not None and not isinstance(value, str):
            raise TypeError("name must be a string or None")
        self._name = value
