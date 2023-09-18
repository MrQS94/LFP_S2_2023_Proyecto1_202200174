import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
from Controlador_Analisis import Analizar

analizar_handler = Analizar()

class Controlador():
    def __init__(self):
        self.root = tk.Tk()
        self.file_path = ''
        self.text_area = tk.Text()

    def cargar_frame(self):
        self.root.geometry("1000x600")
        self.root.resizable(0, 0)
        self.root.title("GUI")
        
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()
        
        wventana = 1000
        hventana = 600
        
        pwidth = round(wtotal / 2 - wventana / 2)
        pheight = round(htotal / 2 - hventana / 2)

        self.root.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
        self.root.grid()
        self.cargar_frame_contenido()
        
        self.root.mainloop()
        
    def cargar_frame_contenido(self):
        frame_contenido = tk.Frame(self.root, bg='#493eb8', width=1000, height=75)
        frame_contenido.pack(side='top', fill='x', expand=True)
        frame_contenido.place(x=0, y=0)
        
        combo = ttk.Combobox(frame_contenido, values=['Abrir', 'Guardar', 'Guardar como', 'Salir'], state='readonly', font=('Arial', 12), width=15)
        combo.place(x=200, y=25)
        combo.set('ARCHIVO')
        
        self.text_area = tk.Text(self.root, wrap='word', width=105, height=25, font=('Arial', 11))
        self.text_area.place(x=75, y=100)
        
        button_analizar = tk.Button(frame_contenido, text='Analizar', font=('Arial', 12), padx=15, pady=5, command=self.analizar)
        button_analizar.place(x=400, y=20)
        
        button_errores = tk.Button(frame_contenido, text='Errores', font=('Arial', 12), padx=15, pady=5, command=self.errores)
        button_errores.place(x=550, y=20)
        
        button_reporte= tk.Button(frame_contenido, text='Reporte', font=('Arial', 12), padx=15, pady=5, command=self.reporte)
        button_reporte.place(x=700, y=20)
        
        info_frame = tk.Frame(self.root)
        info_frame.pack(fill=tk.X, side='bottom')
        
        posiciones = tk.Label(info_frame, text="Líneas: 1, Columnas: 1")
        posiciones.pack(side=tk.LEFT, padx=10)
        
        self.text_area.bind("<Key>", lambda event: self.contar_columnas(self.text_area, posiciones))
        self.text_area.bind("<Button-1>", lambda event: self.contar_columnas(self.text_area, posiciones))
        combo.bind("<<ComboboxSelected>>", lambda event: self.on_abrir_archivo(combo, self.text_area))
        
    def analizar(self):
        txt = self.text_area.get(1.0, tk.END)
        if txt != '\n':
            analizar_handler.analizar(txt)
            messagebox.showinfo('TERMINADO!', 'Análisis terminado!\nEl archivo de analisis se encuentra en la carpeta src del proyecto.')
        else:
            messagebox.showerror('ERROR!', 'No hay texto para analizar.')
    
    def errores(self):
        txt = self.text_area.get(1.0, tk.END)
        if txt != '\n':
            analizar_handler.crear_archivo_errores(txt)
            messagebox.showinfo('TERMINADO!', 'Errores terminados!\nEl archivo de errores se encuentra en la carpeta src del proyecto.')
        else:
            messagebox.showerror('ERROR!', 'No hay texto para analizar.')
    
    def reporte(self):
        txt = self.text_area.get(1.0, tk.END)
        if txt != '\n':
            analizar_handler.reporte(txt)
            messagebox.showinfo('TERMINADO!', 'Reporte terminado!\nEl archivo de reporte se encuentra en la carpeta src del proyecto.')
        else:
            messagebox.showerror('ERROR!', 'No hay texto para analizar.')
        
    def contar_columnas(self, text_widget, posiciones):
        linea, column = text_widget.index(tk.CURRENT).split('.')
        posiciones.config(text=f"Línea: {linea}, Columna: {column}")

    def on_abrir_archivo(self, combo, text_widget):
        opcion = combo.get()
        if opcion == 'Abrir':
            self.file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
            if self.file_path:
                with open(self.file_path, "r", encoding='UTF-8') as file:
                    try:
                        json_data = json.load(file)
                        text_widget.delete('1.0', tk.END)  # Limpiar el TextBox
                        text_widget.insert(tk.END, json.dumps(json_data, indent=4))
                    except json.JSONDecodeError:
                        print("Error al decodificar el archivo JSON")
                    file.close()
        elif opcion == 'Guardar':
            text_json = text_widget.get("1.0", tk.END)
            with open(self.file_path, 'w', encoding='UTF-8') as file:
                file.write(text_json)
                file.close()
        elif opcion == 'Guardar como':
            file_path = filedialog.asksaveasfilename(filetypes=[("JSON Files", "*.json")])
            text_json = text_widget.get("1.0", tk.END)
            if file_path:
                with open(file_path + '.json', "w", encoding='UTF-8') as file:
                    file.write(text_json)
                    file.close()
        elif opcion == 'Salir':
            result = messagebox.askyesno("¿SALIR?", "¿Quieres salir del programa?")
            if result:
                self.root.destroy()