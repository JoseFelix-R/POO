import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from tkinter.filedialog import askopenfilename

class BuscaGUI:
    '''View do Projeto'''
    def __init__(self, root):
        
        self.botoes= {}
        self._tv = None
        self._root = root
        self._categoria = ['Comedia', 'Entretenimento', 'Esportes', 'Documentarios', 'Educacional','Games','Musica']        
        self._inicializar_vars()
        self._inicializa_gui()
        
    def _inicializar_vars(self):
        self._titulo = tk.StringVar()
        self._canal = tk.StringVar()
        self._data_i = tk.StringVar()
        self._data_f = tk.StringVar()     
        self._categ = tk.StringVar()
        self.nome_arq = tk.StringVar()
    
    def seleciona_arquivo():
        tipos_arq = (
            ('Arquivos de texto', '*.txt'),
            ('Arquivos CSV', '*.csv'),
            ('Todos os arquivos', '*.*')
        )

        nome_arq  = askopenfilename(title='Abrir arquivo',\
                                   filetypes=tipos_arq)
        if nome_arq:
            nome_arq.set('Arquivo escolhido: ' + nome_arq)
    
    def _inicializa_gui(self):
        ttk.Style().theme_use('vista')
        frame_top = tk.Frame(self._root, bd=10, relief=tk.SUNKEN)
        frame_top.config(bg='red')
        frame_top.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        frame_right = tk.Frame(self._root, bd=10, relief=tk.SUNKEN)
        frame_right.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT) 
        frame_down = tk.Frame(self._root, bd = 10, relief=tk.SUNKEN)
        frame_down.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM) 
        
        colunas = ['0','1','2','3','4','5','6']
        self._tv = ttk.Treeview(frame_right, columns=colunas, show='headings')
        self._tv.pack(expand=True, fill=tk.BOTH, side=tk.TOP) 
        
        #heading
        self._tv.heading('0', text='Canal')
        self._tv.heading('1', text='Titulo')
        self._tv.heading('2', text='Categoria')
        self._tv.heading('3', text='Views')
        self._tv.heading('4', text='Comentatios')
        self._tv.heading('5', text='Likes')
        self._tv.heading('6', text='Publicacao')
        
        self._tv.column('0', width=90, minwidth=100)
        self._tv.column('1', width=90, minwidth=100)
        self._tv.column('2', width=90, minwidth=100)
        self._tv.column('3', width=90, minwidth=100)
        self._tv.column('4', width=90, minwidth=100)
        self._tv.column('5', width=90, minwidth=100)
        self._tv.column('6', width=90, minwidth=100)
        
        #ScrollBar    
        sb_y = ttk.Scrollbar(frame_right, orient=tk.VERTICAL, command=self._tv.yview)
        self._tv.configure(yscroll=sb_y.set)
        
        sb_x = ttk.Scrollbar(frame_right, orient=tk.HORIZONTAL, command=self._tv.xview)
        self._tv.configure(xscroll=sb_x.set)
        
        self._tv.grid(row=0, column=0)
        sb_y.grid(row=0, column=1, sticky='ns')
        sb_x.grid(row=1, column=0, sticky='we')
        
        
        #Menu de Busca
        v_titu = tk.Label(frame_top, text='Titulo: ')
        v_titu.grid(row = 0, column = 0)
        e_titu = tk.Entry(frame_top, width=40,textvariable=self._titulo)
        e_titu.grid(row = 0, column = 1, columnspan=3, sticky='W')
    
        
        v_canal = tk.Label(frame_top, text='Canal: ')
        v_canal.grid(row = 1, column = 0)
        e_canal = tk.Entry(frame_top, width=20, textvariable=self._canal)
        e_canal.grid(row = 1, column = 1, sticky='W')
        
        v_data_i = tk.Label(frame_top, text='Inicio: ')
        v_data_i.grid(row = 2, column = 0)
        e_data_i= tk.Entry(frame_top, width=10, textvariable=self._data_i)
        e_data_i.grid(row = 2, column = 1, sticky='W')
        
        v_data_f = tk.Label(frame_top, text='Final: ')
        v_data_f.grid(row = 2, column = 2)
        e_data_f= tk.Entry(frame_top, width=10, textvariable=self._data_f)
        e_data_f.grid(row = 2, column = 3, sticky='W')
        
        #Combobox categoria
        
        v_cat = tk.Label(frame_top, text='Categoria: ')
        v_cat.grid(row = 3, column = 0, sticky='S')
        v_cb = ttk.Combobox(frame_top, width = 20, textvariable=self._categ,
                           state='readonly', values=self._categoria)
        v_cb.grid(row = 3, column=1, sticky='W')
        

        #Butões
        self.botoes['Buscar'] = tk.Button(frame_top, width=10, text='Buscar')
        self.botoes['Buscar'].grid(row = 4, column = 3, sticky='E')
        self.botoes['limpar'] = tk.Button(frame_top, width=10, text='limpar')
        self.botoes['limpar'].grid(row = 4, column = 4, sticky='E')
        
        self.nome_arq.set('Arquivo escolhido: ')
        self.botoes['A_Arquivo'] = tk.Button(frame_top, width=10, text='Abrir Arquivo', command=BuscaGUI.seleciona_arquivo)
        self.botoes['A_Arquivo'].grid(row = 4, column = 5, sticky='E')
        
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Buscador Youtube')

    gui = BuscaGUI(root)
    #gui.atualiza_listbox(['um', 'dois', 'tres']) # Observe: LISTA DE STRINGS

    root.mainloop()
        

        
        
        
        
        
