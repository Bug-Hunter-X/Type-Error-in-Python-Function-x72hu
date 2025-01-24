def function(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return "Error: Operands must be integers or convertible to integers."

result = function(5, '10')
print(result)

result = function(5, 10)
print(result)

result = function('abc', '10')
print(result)