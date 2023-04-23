class Empty:

    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())

    def inorder(self):
        return []


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self

    def inorder(self):
        if self.is_leaf():
            return [self.value]
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()

    def min_item(self):
        if self.left.is_empty():
            return self.value
        else:
            return self.left.min_item()

    def max_item(self):
        if self.right.is_empty():
            return self.value
        else:
            return self.right.max_item()

    def balance_factor(self):
        return self.right.height() - self.left.height()

    def balanced_everywhere(self):
        if self.is_leaf():
            return True
        else:
            if self.balance_factor() not in [-1, 0, 1]:
                return False
            else:
                return (self.left.balanced_everywhere()
                        and self.right.balanced_everywhere())

    def add_to_all(self, n):
        self.value += n
        if not self.left.is_empty():
            self.left.add_to_all(n)
        if not self.right.is_empty():
            self.right.add_to_all(n)

    def path_to(self, n):
        if not self.contains(n):
            return None

        if self.value == n:
            return [n]
        if self.value > n:
            return [self.value] + self.left.path_to(n)
        if self.value < n:
            return [self.value] + self.right.path_to(n)


if __name__ == "__main__":
    bst = Empty().insert(42).insert(10).insert(15).insert(63).insert(23)
    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
    print(bst.inorder())
    print(f"The min is {bst.min_item()}")
    print(f"The max is {bst.max_item()}")
    print(f"The balance factor is {bst.balance_factor()}")
    print(f"Balance every where? {bst.balanced_everywhere()}")
    print(f"Path to {23} {bst.path_to(23)}")
    bst.add_to_all(3)
    print(bst.inorder())
