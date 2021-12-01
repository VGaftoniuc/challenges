def freq_digit(num: int) -> int:
    digits = list(str(num))
    result = 0
    base_count = 0
    for digit in digits:
        count = digits.count(digit)
        if count > base_count:
            base_count = count
            result = int(digit)
    return result
