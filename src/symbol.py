# Symbol Implementation by fabiommendes
class Symbol:
    """
    Representa um símbolo Lisp.

    Diferentemente de strings, símbolos com o mesmo valor possuem a mesma identidade.
    """

    data : str
    CACHE = {}

    def __new__(cls, data):
        if isinstance(data, Symbol):
            return data
        try:
            return cls.CACHE[data]
        except KeyError:
            cls.CACHE[data] = new = super().__new__(cls)
            new._data = data
            return new

    def __str__(self):
        return self._data

    def __repr__(self):
        return self._data

    def __hash__(self):
        return id(self._data)

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self._data == other._data
        return NotImplemented

# Tipos padrões da linguagem
Symbol.INT = Symbol('int')
Symbol.LINT = Symbol('Lint')
Symbol.UINT = Symbol('Uint')
Symbol.ULINT = Symbol('ULint')
Symbol.SINT = Symbol('Sint')
Symbol.USINT = Symbol('USint')

Symbol.FLOAT = Symbol('float')
Symbol.LFLOAT = Symbol('Lfloat')

Symbol.CHAR = Symbol('char')
Symbol.STRING = Symbol('string')
Symbol.BOOL = Symbol('bool')
Symbol.ARRAY = Symbol('Array')

Symbol.VOID = Symbol('void')

class _Var:
    def __getattr__(self, attr):
        return Symbol(attr)

    def __repr__(self):
        return 'var'

var = _Var()