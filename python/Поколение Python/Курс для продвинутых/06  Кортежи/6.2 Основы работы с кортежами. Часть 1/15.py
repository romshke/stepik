tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [_ for _ in tuples if len(_) > 0]

print(non_empty_tuples)
