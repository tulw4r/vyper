from itertools import (
    chain,
)
from typing import (
    Any,
    List as ListTyping,
)

from vyper.exceptions import (
    CompilerPanic,
)


class VyperNode:
    __slots__ = ('node_id', 'source_code', 'col_offset', 'lineno')
    ignored_fields = ['ctx', ]
    only_empty_fields: ListTyping[Any] = []

    @classmethod
    def get_slots(cls):
        return chain.from_iterable(
            getattr(klass, '__slots__', [])
            for klass in cls.__class__.mro(cls)
        )

    def __init__(self, **kwargs):

        for field_name, value in kwargs.items():
            if field_name in self.get_slots():
                setattr(self, field_name, value)
            elif value:
                raise CompilerPanic(
                    f'Unsupported non-empty value field_name: {field_name}, '
                    f' class: {type(self)} value: {value}'
                )

    def __eq__(self, other):
        if isinstance(other, type(self)):
            for field_name in self.get_slots():
                if field_name not in ('node_id', 'source_code', 'col_offset', 'lineno'):
                    if getattr(self, field_name, None) != getattr(other, field_name, None):
                        return False
            return True
        else:
            return False


class Module(VyperNode):
    __slots__ = ('body', )


class Name(VyperNode):
    __slots__ = ('id', )


class Subscript(VyperNode):
    __slots__ = ('slice', 'value')


class Index(VyperNode):
    __slots__ = ('value', )


class arg(VyperNode):
    __slots__ = ('arg', 'annotation')


class Tuple(VyperNode):
    __slots__ = ('elts', )


class FunctionDef(VyperNode):
    __slots__ = ('args', 'body', 'returns', 'name', 'decorator_list', 'pos')


class arguments(VyperNode):
    __slots__ = ('args', 'defaults', 'default')
    only_empty_fields = ['vararg', 'kwonlyargs', 'kwarg', 'kw_defaults']


class Import(VyperNode):
    __slots__ = ('names', )


class Call(VyperNode):
    __slots__ = ('func', 'args', 'keywords', 'keyword')


class keyword(VyperNode):
    __slots__ = ('arg', 'value')


class Str(VyperNode):
    __slots__ = ('s', )


class Compare(VyperNode):
    __slots__ = ('comparators', 'ops', 'left', 'right')


class Num(VyperNode):
    __slots__ = ('n', )


class NameConstant(VyperNode):
    __slots__ = ('value', )


class Attribute(VyperNode):
    __slots__ = ('attr', 'value',)


class Op(VyperNode):
    __slots__ = ('op', 'left', 'right')


class BoolOp(Op):
    __slots__ = ('values', )


class BinOp(Op):
    pass


class UnaryOp(Op):
    __slots__ = ('operand', )


class List(VyperNode):
    __slots__ = ('elts', )


class Dict(VyperNode):
    __slots__ = ('keys', 'values')


class Bytes(VyperNode):
    __slots__ = ('s', )


class Add(VyperNode):
    pass


class Sub(VyperNode):
    pass


class Mult(VyperNode):
    pass


class Div(VyperNode):
    pass


class Mod(VyperNode):
    pass


class Pow(VyperNode):
    pass


class In(VyperNode):
    pass


class Gt(VyperNode):
    pass


class GtE(VyperNode):
    pass


class LtE(VyperNode):
    pass


class Lt(VyperNode):
    pass


class Eq(VyperNode):
    pass


class NotEq(VyperNode):
    pass


class And(VyperNode):
    pass


class Or(VyperNode):
    pass


class Not(VyperNode):
    pass


class USub(VyperNode):
    pass


class Expr(VyperNode):
    __slots__ = ('value', )


class Pass(VyperNode):
    pass


class AnnAssign(VyperNode):
    __slots__ = ('target', 'annotation', 'value', 'simple')


class Assign(VyperNode):
    __slots__ = ('targets', 'value')


class If(VyperNode):
    __slots__ = ('test', 'body', 'orelse')


class Assert(VyperNode):
    __slots__ = ('test', 'msg')


class For(VyperNode):
    __slots__ = ('iter', 'target', 'orelse', 'body')


class AugAssign(VyperNode):
    __slots__ = ('op', 'target', 'value')


class Break(VyperNode):
    pass


class Continue(VyperNode):
    pass


class Return(VyperNode):
    __slots__ = ('value', )


class Delete(VyperNode):
    __slots__ = ('targets', )


class stmt(VyperNode):
    pass


class ClassDef(VyperNode):
    __slots__ = ('class_type', 'name', 'body')


class Raise(VyperNode):
    __slots__ = ('exc', )


class Slice(VyperNode):
    only_empty_fields = ['lower']


class alias(VyperNode):
    __slots__ = ('name', 'asname')


class ImportFrom(VyperNode):
    __slots__ = ('module', 'names')
