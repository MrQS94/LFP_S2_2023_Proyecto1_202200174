import sys
import os

ruta_actual = os.path.dirname(__file__)
ruta_proyecto = os.path.abspath(os.path.join(ruta_actual, '..'))
if ruta_proyecto not in sys.path:
    sys.path.append(ruta_proyecto)

from package.Abstract import Error, Lexema, Valor
from package.Operaciones import Aritmetica, Trigonometria

global pos_column
global pos_row

pos_row = 1
pos_column = 0

class Analizar():
    def __init__(self):
        pass
    
    def graphviz(self):
        global list_graphviz
        
        title = str(list_graphviz[0])
        body = 'digraph G {\n'
        if title == '':
            title = 'Graphviz'
        
        for i in range(len(list_tokens)):
            token = list_tokens[i]
            body += self.opciones_config(i, 0, '', token)
        
        body += f'''
        label = "{title}";
        '''
        body += '}'
        title = title.replace(' ', '_')
        with open(f'Resultados_202200174_{title}.dot', 'w', encoding='UTF-8') as archivo:
            archivo.write(body)
        os.system(f"dot -Tpng Resultados_202200174_{title}.dot -o Resultados_202200174_{title}.png")

    def operacion_valores(self):
        global list_lexemas
        global list_tokens
        operacion = ''
        valor1 = ''
        valor2 = ''
        while list_lexemas:
            lexema = list_lexemas.pop(0)
            if lexema.operacion(None) == 'operacion':
                operacion = list_lexemas.pop(0)
            elif lexema.operacion(None) == 'valor1':
                valor1 = list_lexemas.pop(0)
                if valor1.operacion(None) == '[':
                    valor1 = self.operacion_valores()
            elif lexema.operacion(None) == 'valor2':
                valor2 = list_lexemas.pop(0)
                if valor2.operacion(None) == '[':
                    valor2 = self.operacion_valores()
            if operacion and valor1 and valor2:
                return Aritmetica(valor1, valor2, operacion, f'Inicio: {operacion.get_row()} - {operacion.get_column()}', f'Fin: {valor2.get_row()}: {valor2.get_row()}')
            elif operacion and valor1 and (operacion.operacion(None) == 'seno' or operacion.operacion(None) == 'coseno' or operacion.operacion(None) == 'tangente'):
                return Trigonometria(valor1, operacion, f'Inicio: {operacion.get_row()} - {operacion.get_column()}', f'Fin: {valor1.get_row()}: {valor1.get_row()}')
        return None

    def lexema_config(self):
        global list_lexemas
        
        is_configuracion = False
        for i in range(len(list_lexemas)):
            if list_lexemas[i].operacion(None) == 'configuraciones':
                is_configuracion = True
                
        
        if is_configuracion is False:
            return 'No hay configuraciones, se usarán las predeterminadas.'
        
        for i in range(len(list_lexemas)):
            lexema = list_lexemas[i]
            if lexema.operacion(None) == 'texto':
                list_graphviz.append(list_lexemas[i + 1].operacion(None))
            elif lexema.operacion(None) == 'fondo':
                list_graphviz.append(list_lexemas[i + 1].operacion(None))
            elif lexema.operacion(None) == 'fuente':
                list_graphviz.append(list_lexemas[i + 1].operacion(None))
            elif lexema.operacion(None) == 'forma':
                list_graphviz.append(list_lexemas[i + 1].operacion(None))

    def opciones_config(self, no_nodo, id, etiqueta, objeto):
        global list_graphviz
        
        color_fondo = list_graphviz[1].lower()
        color_fuente = list_graphviz[2].lower()
        forma = list_graphviz[3].lower()
        
        if color_fondo == 'negro':
            color_fondo = 'black'
        elif color_fondo == 'rojo':
            color_fondo = 'red'
        elif color_fondo == 'verde':
            color_fondo = 'green'
        elif color_fondo == 'azul':
            color_fondo = 'blue'
        elif color_fondo == 'amarillo':
            color_fondo = 'yellow'
        elif color_fondo == 'naranja' or color_fondo == 'anaranjado':
            color_fondo = 'orange'
        elif color_fondo == 'morado':
            color_fondo = 'purple'
        elif color_fondo == 'rosa':
            color_fondo = 'pink'
        elif color_fondo == 'marron' or color_fondo == 'marrón':
            color_fondo = 'brown'
        elif color_fondo == 'gris':
            color_fondo = 'gray'
        else:
            color_fondo = 'white'
            
        if color_fuente == 'blanco':
            color_fuente = 'white'
        elif color_fuente == 'rojo':
            color_fuente = 'red'
        elif color_fuente == 'verde':
            color_fuente = 'green'
        elif color_fuente == 'azul':
            color_fuente = 'blue'
        elif color_fuente == 'amarillo':
            color_fuente = 'yellow'
        elif color_fuente == 'naranja' or color_fuente == 'anaranjado':
            color_fuente = 'orange'
        elif color_fuente == 'morado':
            color_fuente = 'purple'
        elif color_fuente == 'rosa':
            color_fuente = 'pink'
        elif color_fuente == 'marron' or color_fuente == 'marrón':
            color_fuente = 'brown'
        elif color_fuente == 'gris':
            color_fuente = 'gray'
        else:
            color_fuente = 'black'
            
        if forma == 'elipse':
            forma = 'ellipse'
        elif forma == 'cuadrado':
            forma = 'box'
        elif forma == 'triangulo':
            forma = 'triangle'
        elif forma == 'diamante':
            forma = 'diamond'
        elif forma == 'paralelogramo':
            forma = 'parallelogram'
        elif forma == 'trapezoide':
            forma = 'trapezium'
        elif forma == 'hexagono':
            forma = 'hexagon'
        elif forma == 'octagono':
            forma = 'octagon'
        elif forma == 'huevo':
            forma = 'egg'
        elif forma == 'ovalo':
            forma = 'oval'
        elif forma == 'texto':
            forma = 'plaintext'
        elif forma == 'punto':
            forma = 'point'
        elif forma == 'ninguna':
            forma = 'none'
        elif forma == 'registro':
            forma = 'record'
        else:
            forma = 'circle' 
        
        body = ''
        if objeto:
            if type(objeto) == Valor:
                body += f'Nodo_{no_nodo}{id}{etiqueta}[label="{objeto.operacion(None)}", fillcolor={color_fondo}, fontcolor={color_fuente}, shape={forma}, style=filled];\n'

            if type(objeto) == Trigonometria:
                body += f'Nodo_{no_nodo}{id}{etiqueta}[label="{objeto.valor.lexema}\\n{objeto.operacion(None)}", fillcolor={color_fondo}, fontcolor={color_fuente}, shape={forma}, style=filled]\n'
                
                body += self.opciones_config(no_nodo, id + 1, etiqueta + '_angulo', objeto.left)
                body += f'Nodo_{no_nodo}{id}{etiqueta} -> Nodo_{no_nodo}{id + 1}{etiqueta}_angulo;\n'
            
            if type(objeto) == Aritmetica:
                body += f'Nodo_{no_nodo}{id}{etiqueta}[label="{objeto.valor.lexema}\\n{objeto.operacion(None)}", fillcolor={color_fondo}, fontcolor={color_fuente}, shape={forma}, style=filled];\n'
                
                body += self.opciones_config(no_nodo, id + 1, etiqueta + '_valor1', objeto.left)
                body += f'Nodo_{no_nodo}{id}{etiqueta} -> Nodo_{no_nodo}{id + 1}{etiqueta}_valor1;\n'
                
                body += self.opciones_config(no_nodo, id + 1, etiqueta + '_valor2', objeto.right)
                body += f'Nodo_{no_nodo}{id}{etiqueta} -> Nodo_{no_nodo}{id + 1}{etiqueta}_valor2;\n'
                
        return body
                
    def operar_intrucciones(self):
        global list_tokens
        
        while True:
            operacion = self.operacion_valores()
            
            if operacion:
                list_tokens.append(operacion)
            else:
                break
            
            for token in list_tokens:
                token.operacion(None)
        return list_tokens

    def creaciones_lexemas_numeros(self, txt):
        global pos_column
        global pos_row
        lexema = ''
        contador = 0
        while txt:
            char = txt[contador]
            contador += 1
            if char == '\"':
                lexema, txt = self.crear_lexema(txt[contador:])
                if lexema and txt:
                    pos_column += 1
                    lex = Lexema(lexema, pos_row, pos_column)
                    list_lexemas.append(lex)
                    pos_column += len(lexema) + 1
                    contador = 0
            elif char.isdigit() or char == '-':
                token, txt = self.crear_numero(txt)
                if token and txt:
                    numero = Valor(token, pos_row, pos_column)
                    list_lexemas.append(numero)
                    pos_column += len(str(token))
                    contador = 0
            elif char == '[' or char == ']':
                corchete = Lexema(char, pos_row, pos_column)     
                pos_column += 1
                list_lexemas.append(corchete)
                txt = txt[1:]
                contador = 0
            elif char == '\t':
                txt = txt[4:]
                pos_column = 0
                pos_row += 1
                contador = 0
            elif char == '\n':
                txt = txt[1:]
                pos_column = 0
                pos_row += 1
                contador = 0
            elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == ':' or char == '.':
                txt = txt[1:]
                pos_column += 1
                contador = 0
            else:
                txt = txt[1:]
                pos_column += 1
                contador = 0
                list_errors.append(Error(char, pos_row, pos_column))
        return list_lexemas
        
    def crear_lexema(self, txt):
        lexema = ''
        txt_union = ''
        for char in txt:
            txt_union += char	
            if char == '\"':
                return lexema, txt[len(txt_union):]
            else:
                lexema += char
        return None, None

    def crear_numero(self, txt):
        numero = ''
        txt_union = ''
        is_negativo = False
        is_decimal = False
        
        for char in txt:
            txt_union += char
            if char == '-':
                is_negativo = True
            if char == '.':
                is_decimal = True
            if char == '"' or char == ' ' or char == '\n' or char == '\t' or char == ']' or char == ',':
                if is_decimal:
                    return float(numero), txt[len(txt_union) - 1:]
                if is_negativo:
                    return int(numero), txt[len(txt_union) - 1:]
                else:
                    return int(numero), txt[len(txt_union) - 1:]
            else:
                numero += char
        return None, None
    
    def reporte(self, txt):
        self.creaciones_lexemas_numeros(txt)
        self.lexema_config()
        self.operar_intrucciones()
        self.graphviz()
        
        self.limpiar_listas()
        
    def analizar(self, txt):
        global list_analyse
        self.creaciones_lexemas_numeros(txt)
        self.lexema_config()
        lexema = ''
        for i in range(len(list_lexemas)):
            lexema += str(list_lexemas[i].operacion(None)) + '\n'
        
        with open('src/Analisis_202200174.txt', 'w', encoding='UTF-8') as archivo:
            archivo.write(lexema)
        self.limpiar_listas()
        
    def errores(self, txt):
        global list_errors
        self.creaciones_lexemas_numeros(txt)
        self.lexema_config()
        
        body = '{\n\t"errores": [\n'
        
        for i in range(len(list_errors)):
            error = list_errors[i]
            body += error.operacion(i + 1)
            if i != len(list_errors) - 1:
                body += ',\n'
            else:
                body += '\n'
        body += '\n\t]\n}'
        return body
        
    def crear_archivo_errores(self, txt):
        with open('src/Errores_202200174.json', 'w', encoding='UTF-8') as archivo:
            archivo.write(self.errores(txt))
            
        self.limpiar_listas()
        
    def limpiar_listas(self):
        global list_tokens
        global list_analyse
        global pos_column
        global pos_row
        global list_lexemas
        global list_errors
        
        list_tokens.clear()
        pos_column = 0
        pos_row = 1
        list_lexemas.clear()
        list_errors.clear()
        list_graphviz.clear()
        list_analyse.clear()

global list_tokens
global list_analyse
global list_lexemas
global list_errors

list_lexemas = []
list_tokens = []
list_errors = []
list_graphviz = []
list_analyse = []