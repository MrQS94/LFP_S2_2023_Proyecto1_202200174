from abc import ABC, abstractmethod
import math

class Expresion(ABC):
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    @abstractmethod
    def operacion(self, tree):
        pass

    @abstractmethod
    def get_row(self):
        return self.row

    @abstractmethod
    def get_column(self):
        return self.column
    
class Lexema(Expresion):
    def __init__(self, lexema, row, column):
        self.lexema = lexema
        super().__init__(row, column)
    
    def operacion(self, tree):
        return self.lexema
    
    def get_row(self):
        return super().get_row()
    
    def get_column(self):
        return super().get_column()
    
class Error(Expresion):
    def __init__(self, lexema, row, column):
        self.lexema = lexema
        super().__init__(row, column)
        
    def operacion(self, tree):
        llave_inicial = '\t\t{\n'
        no = f'\t\t\t"No": {tree},\n'
        descripcion_incial = '\t\t\t"descripcion": {\n'
        lexema = f'\t\t\t\t"lexema": "{self.lexema}",\n'
        tipo = '\t\t\t\t"tipo": "ERROR LEXICO",\n'
        column = f'\t\t\t\t"columna": {self.column},\n'
        fila = f'\t\t\t\t"fila": {self.row}\n'
        descripcion_final = '\t\t\t}\n'
        llave_final = '\t\t}'
        return llave_inicial + no + descripcion_incial + lexema + tipo + column + fila + descripcion_final + llave_final
    
    def get_column(self):
        return super().get_column()
    
    def get_row(self):
        return super().get_row()
    
class Valor(Expresion):
    def __init__(self, valor, row, column):
        self.valor = valor
        super().__init__(row, column)
        
    def operacion(self, tree):
        return self.valor

    def get_column(self):
        return super().get_column()
    
    def get_row(self):
        return super().get_row()
    
class Analisis(Expresion):
    def __init__(self, lexema, tipo, row, column):
        self.lexema = lexema
        self.tipo = tipo
        super().__init__(row, column)
    
    def operacion(self, tree):
        llave_inicial = '\t\t{\n'
        no = f'\t\t\t"No": {tree},\n'
        descripcion_incial = '\t\t\t"descripcion": {\n'
        lexema = f'\t\t\t\t"lexema": "{self.lexema}",\n'
        tipo = f'\t\t\t\t"tipo": "{self.tipo}",\n'
        column = f'\t\t\t\t"columna": {self.column},\n'
        fila = f'\t\t\t\t"fila": {self.row}\n'
        descripcion_final = '\t\t\t}\n'
        llave_final = '\t\t}'
        return llave_inicial + no + descripcion_incial + lexema + tipo + column + fila + descripcion_final + llave_final
    
    def get_column(self):
        return super().get_column()
    
    def get_row(self):
        return super().get_row()
    
class Arit(Expresion):
    def __init__(self, left, right, valor, row, column):
        self.left = left
        self.right = right
        self.valor = valor
        super().__init__(row, column)
        
    def operacion(self, arbol):
        left_valor = ''
        right_valor = ''
        
        if left_valor is not None:
            left_valor = self.left.operacion(arbol)
        
        if right_valor is not None:
            right_valor = self.right.operacion(arbol)
        
        if self.valor.operacion(arbol) == 'Suma':
            return left_valor + right_valor
        elif self.valor.operacion(arbol) == 'Resta':
            return left_valor - right_valor
        elif self.valor.operacion(arbol) == 'Multiplicacion':
            return left_valor * right_valor
        elif self.valor.operacion(arbol) == 'Division':
            return left_valor / right_valor
        elif self.valor.operacion(arbol) == 'Potencia':
            return left_valor ** right_valor
        elif self.valor.operacion(arbol) == 'Raiz':
            return left_valor ** (1 / right_valor)
        elif self.valor.operacion(arbol) == 'Inverso':
            return (1 / left_valor)
        elif self.valor.operacion(arbol) == 'Mod':
            return left_valor % right_valor
        else:
            return None
        
    def get_column(self):
        return super().get_column()
    
    def get_row(self):
        return super().get_row()
    
class Trigo(Expresion):
    def __init__(self, left, valor, row, column):
        self.left = left
        self.valor = valor
        super().__init__(row, column)
    
    def operacion(self, arbol):
        left_valor = ''
        
        self.valor.operacion(arbol).lower()
        if self.left is not None:
            left_valor = self.left.operacion(arbol)
        if self.valor.operacion(arbol) == 'Seno':
            op_ = math.sin(math.radians(left_valor))
            return round(op_, 2)
        elif self.valor.operacion(arbol) == 'Coseno':
            op_ = math.cos(math.radians(left_valor))
            return round(op_, 2)
        elif self.valor.operacion(arbol) == 'Tangente':
            op_ = math.tan(math.radians(left_valor))
            return round(op_, 2)
        else:
            return None
        
    def get_column(self):
        return super().get_column()
    
    def get_row(self):
        return super().get_row()