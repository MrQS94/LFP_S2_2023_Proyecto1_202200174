from abc import ABC, abstractmethod

class Expresion(ABC):
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    @abstractmethod
    def operacion(self, arbol):
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
    
    def operacion(self, arbol):
        return self.lexema
    
    def get_row(self):
        return super().get_row()
    
    def get_column(self):
        return super().get_column()
    
class Error(Expresion):
    def __init__(self, lexema, row, column):
        self.lexema = lexema
        super().__init__(row, column)
        
    def operacion(self, arbol):
        llave_iniciales = '\t\t{\n'
        no = f'\t\t\t"No": {arbol},\n'
        descripcion_incial = '\t\t\t"descripcion": {\n'
        lexema = f'\t\t\t\t"lexema": "{self.lexema}",\n'
        tipo = '\t\t\t\t"tipo": "ERROR LEXICO",\n'
        column = f'\t\t\t\t"columna": {self.column},\n'
        fila = f'\t\t\t\t"fila": {self.row}\n'
        descripcion_final = '\t\t\t}\n'
        llaves_finales = '\t\t}'
        return llave_iniciales + no + descripcion_incial + lexema + tipo + column + fila + descripcion_final + llaves_finales
    
    def get_column(self):
        return super().get_column()
    
    def get_row(self):
        return super().get_row()
    
class Valor(Expresion):
    def __init__(self, valor, row, column):
        self.valor = valor
        super().__init__(row, column)
        
    def operacion(self, arbol):
        return self.valor

    def get_column(self):
        return super().get_column()
    
    def get_row(self):
        return super().get_row()