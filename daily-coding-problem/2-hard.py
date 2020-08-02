# Given an array of integers, return a new array such that each element at index i of the new array is
# the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?


def with_division(array):
    total_product = 1
    for item in array:
        total_product *= item
    return [total_product / item for item in array]


def without_division(array):
    product_from_the_left = [1]
    for index, item in enumerate(array[1:]):
        product_from_the_left.append(item * product_from_the_left[index-1])

    array.reverse()
    product_from_the_right = [1]
    for index, item in enumerate(array[1:]):
        product_from_the_right.append(item * product_from_the_right[index - 1])

    return [left * right for left, right in zip(product_from_the_left, product_from_the_right)]


def main():
    assert with_division([1, 2, 3, 4, 5]) == without_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert with_division([3, 2, 1]) == without_division([3, 2, 1]) == [2, 3, 6]


if __name__ == '__main__':
    main()
