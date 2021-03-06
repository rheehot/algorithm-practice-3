from sys import stdin

def tree_insert(tree, new_value) -> tuple:
    if tree is None:
        return (new_value, None, None)

    value, left, right = tree
    return (
        (value, tree_insert(left, new_value), right)
        if new_value < value else
        (value, left, tree_insert(right, new_value))
    )

def dfs_postorder(tree: tuple):
    if tree is not None:
        value, left, right = tree
        yield from dfs_postorder(left)
        yield from dfs_postorder(right)
        yield value

tree = None
for line in stdin:
    num = int(line)
    tree = tree_insert(tree, num)
for value in dfs_postorder(tree):
    print(value)
