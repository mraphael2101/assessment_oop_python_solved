from .animal import Animal


class Bird(Animal):
    def calculate_random_age(self) -> int:
        return 0

    """
    Signature does not do Method "overloading" in Python
    - Use a single method with default parameter values (so callers can omit them).
    - Use variable arguments (*args and/or **kwargs) and branch logic inside.
    - Use different method names if the behaviors are distinct.
    """
    def calculate_random_age_with_val(self, val: int) -> int:
        return 0
