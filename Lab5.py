# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    while n == n:
        result += "*" * n
        result += "\n"
        for i in range(n - 2):
            result += "*" + " " * (n - 2) + "*"
            result += "\n"
        if n == 1:
            return result.strip()
            break
        result += "*" * n
        return result.strip()
        if n == n:
            break


# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    row = 1
    numbers = 1
    while n == n
        while row <= n:
            while numbers <= row:
                result += str(n - (n - numbers))
                numbers += 1
            result += "\n"
            numbers = 1
            row += 1
            return result.strip()
        if n == n:
            break

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = ""
    count = 0
    summation = 0
    while count < n:
        summation += (n - count)
        count += 1
    result += str(summation)
    return result

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    row = 1
    i = 1
    while row <= n:
        result += " " * (n - row) + "*" * i
        if row == n:
            break
        result += "\n"
        row += 1
        i += 2
    return result