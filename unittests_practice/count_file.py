def num_to_digits(num):
    digits = list(str(int(num)))
    return digits


def is_there_two_identical_adjacent_digits(digits):
    count = 0
    index = 0
    while index < len(digits) - 1:
        if digits[index] == digits[index + 1]:
            if index == 0:
                count += 1
            elif digits[index] != digits[index - 1]:
                count += 1
            if count >= 2:
                return True
        index += 1
    return False


def is_never_decreasing(digits):
    index = 0
    while index < len(digits) - 1:
        if digits[index] > digits[index + 1]:
            return False
        index += 1
    return True


def might_be_password(num):
    digits = num_to_digits(num)

    if not is_there_two_identical_adjacent_digits(digits):
        return False
    if not is_never_decreasing(digits):
        return False
    return True


count = 0
for num in range(372 ** 2, (809 ** 2) + 1):
    if might_be_password(num):
        count += 1
print(f"There have to checked {count} numbers to find the right password.")
