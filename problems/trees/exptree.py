from abc import ABC, abstractmethod


class Int:
    def __init__(self, n):
        self.n = n

    def is_const(self):
        return True

    def num_nodes(self):
        return 1

    def eval(self):
        return self.n

    def __str__(self):
        return str(self.n)


class Abs:
    def __init__(self, op):
        self.op = op

    def is_const(self):
        return False

    def num_nodes(self):
        return 2

    def eval(self):
        op_value = self.op.eval()

        return abs(op_value)

    def __str__(self):
        op_str = str(self.op)
        return f"|{op_str}|"


class BinOp:

    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def is_const(self):
        return False

    def num_nodes(self):
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    @abstractmethod
    def eval(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class Plus(BinOp):

    def eval(self):
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value + op2_value

    def __str__(self):
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} + {op2_str})"


class Minus(BinOp):

    def eval(self):
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value - op2_value

    def __str__(self):
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} - {op2_str})"


class Times(BinOp):

    def eval(self):
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value * op2_value

    def __str__(self):
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} * {op2_str})"


class Divide(BinOp):

    def eval(self):
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value / op2_value

    def __str__(self):
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} / {op2_str})"


if __name__ == "__main__":

    # Sample expression tree for (2 + (3 * 5))
    op1 = Int(2)
    op2 = Abs(Times(Int(-3), Int(5)))
    expt = Plus(op1, op2)

    print(f"{expt} = {expt.eval()}")
