#!/usr/bin/env python
def mul(a):
    def helper(b):
        return a * b

    return helper


if __name__ == "__main__":
    print(mul(5)(2))
    new_mul5 = mul(5)
    print(new_mul5)
    print(new_mul5(2))
    print(new_mul5(7))
