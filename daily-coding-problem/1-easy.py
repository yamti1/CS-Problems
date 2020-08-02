# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?


# Sort the list.
# Then, have a pointer at the first item, and a pointer at the last.
# If the some of the two values is too big, decrement the big one.
# If the sum is too small, increment the small one.
# If the values are equal there are no matching values.
def sort_and_optimize(array, target_sum):
    array.sort()

    small, big = 0, -1
    while (current_sum := array[small] + array[big]) != target_sum:
        if array[big] == array[small]:
            return False

        if current_sum > target_sum:
            big -= 1
        else:
            small += 1

    return True


def main():
    array = [2, 8, 6, 8, -5, 6, 6, 4]
    target_sum = 12
    print(sort_and_optimize(array, target_sum))


if __name__ == '__main__':
    main()
