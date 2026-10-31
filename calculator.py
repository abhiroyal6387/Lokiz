import ast
import operator


OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def calculate(expr):
    """Safe evaluation of basic arithmetic expressions only."""
    if not isinstance(expr, str) or len(expr) > 80:
        raise ValueError("Invalid expression")

    def _eval(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in OPS:
            return OPS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
            return OPS[type(node.op)](_eval(node.operand))
        if isinstance(node, ast.Expr):
            return _eval(node.value)
        raise ValueError("Only basic arithmetic is allowed")

    tree = ast.parse(expr, mode="eval")
    return _eval(tree.body)
