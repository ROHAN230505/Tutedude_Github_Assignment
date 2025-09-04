def sort_tuples(lst):
    return sorted(lst, key=lambda x: x[1])

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_tuples(sample_list))  # Output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]