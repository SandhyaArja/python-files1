set_a = {"a", "b", "c", "a"}
print(set_a)
-----
set_a = set((1, 2, 1))
print(set_a)
------
set_a = {1, 3, 6, 2, 9}
set_a.add(7)
print(set_a)
------
et_a = {1, 3, 9}
set_a.update([2, 3])
print(set_a)
------
set_a = {1, 3, 9}
set_a.discard(3)
print(set_a)
-------
set_a = {1, 3, 9}
set_a.remove(5)
print(set_a)
-------
set_a = {4, 2, 8}
set_b = {1, 2}
union = set_a | set_b
print(union)
----
set_a = {4, 2, 8}
list_a = [1, 2]
union = set_a.union(list_a)
print(union)
------
set_a = {4, 2, 8}
list_a = [1, 2]
union = set_a.union(list_a)
print(union)
-------
set_a = {4, 2, 8}
list_a = [1, 2]
union = set_a.union(list_a)
print(union)
-------
set_a = {4, 2, 8}
set_b = {1, 2}
symmetric_diff = set_a ^ set_b
print(symmetric_diff)
------
set_a = {4, 2, 8}
set_b = {1, 2}
symmetric_diff = set_a ^ set_b
print(symmetric_diff)
------
et_1 = {'a', 1, 3, 5}
set_2 = {'a', 1}
is_superset = set_1.issuperset(set_2)
print(is_superset)
------
set_1 = {4, 6}
set_2 = {2, 6}
is_superset = set_1.issuperset(set_2)
print(is_superset)
------
set_a = {1, 2}
set_b = {3, 4}
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)
