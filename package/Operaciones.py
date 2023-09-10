import sys
import os

ruta_actual = os.path.dirname(__file__)
ruta_proyecto = os.path.abspath(os.path.join(ruta_actual, '..'))
if ruta_proyecto not in sys.path:
    sys.path.append(ruta_proyecto)
    
from package.Metodos import Expresion
import math

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
            
        if self.valor.operacion(arbol) == 'suma':
            return left_valor + right_valor
        elif self.valor.operacion(arbol) == 'resta':
            return left_valor - right_valor
        elif self.valor.operacion(arbol) == 'multiplicacion':
            return left_valor * right_valor
        elif self.valor.operacion(arbol) == 'division':
            return left_valor / right_valor
        elif self.valor.operacion(arbol) == 'potencia':
            return left_valor ** right_valor
        elif self.valor.operacion(arbol) == 'raiz':
            return left_valor ** (1 / right_valor)
        elif self.valor.operacion(arbol) == 'inverso':
            return (1 / left_valor)
        elif self.valor.operacion(arbol) == 'mod':
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
        
        if self.left is not None:
            left_valor = self.left.operacion(arbol)
        if self.valor.operacion(arbol) == 'seno':
            op_ = math.sin(math.radians(left_valor))
            return round(op_, 2)
        elif self.valor.operacion(arbol) == 'coseno':
            op_ = math.cos(math.radians(left_valor))
            return round(op_, 2)
        elif self.valor.operacion(arbol) == 'tangente':
            op_ = math.tan(math.radians(left_valor))
            return round(op_, 2)
        else:
            return None
        
    def get_column(self):
        return super().get_column()
    
    def get_row(self):
        return super().get_row()