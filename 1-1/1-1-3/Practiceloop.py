# Range examples
# Note: list(range_values) converts the range_values into a list

# using the stop parameter to generate
# a range of numbers from 0 to 10
one_through_ten = range(7)
print(list(one_through_ten))

# using the start and stop parameters to
# generate a range of numbers from 1 to 15
one_through_fifteen = range(1,8)

print(list(one_through_fifteen))
# using the start, stop, and step parameters to
# generate a range of five even numbers starting at 2
ten_evens = range(2,42,3)
print(list(ten_evens))