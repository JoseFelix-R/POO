import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from tkinter.filedialog import askopenfilename

class BuscaGUI:
    '''View do Projeto'''
    def __init__(self, root):
        
        self.botoes= {}
        self._tv = None
        self._ltv = []
        self._quant = '0'
        self._root = root
        self._categoria = ['Comedy', 'Entertainment', 'Sports', 'Documentary', 'Education','Gaming','Musica']        
        self._inicializar_vars()
        self._inicializa_gui()
   
    def _inicializar_vars(self):
        self._titulo = tk.StringVar()
        self._canal = tk.StringVar()
        self._data_i = tk.StringVar()
        self._data_f = tk.StringVar()     
        self._categ = tk.StringVar()
        self.nome_arq = tk.StringVar()
        self._esc = tk.StringVar()
    
    
    def _add_dados(self):
        '''Add os dados de entrada do usuario'''
        return(self._titulo.get(), self._canal.get(), self._data_i.get(), self._data_f.get(), self._categ.get(), self._esc.get())
    
    def _inicializa_gui(self):
        #Tema TTK
        ttk.Style().theme_use('vista')

        #Frames Interface
        frame_top = ttk.Frame(self._root)
        frame_top.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        frame_right = ttk.Frame(self._root)
        frame_right.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT) 
        frame_down = ttk.Frame(self._root)
        frame_down.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM) 
        
        #TreeView 
        colunas = ['0','1','2','3','4','5','6','7','8','9','10','11']
        self._tv = ttk.Treeview(frame_right, columns=colunas, show='headings')
        self._tv.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        
        #heading
        self._tv.heading('0', text='Id_video')
        self._tv.heading('1', text='Titulo')
        self._tv.heading('2', text='Publicacao')
        self._tv.heading('3', text='Id_canal')
        self._tv.heading('4', text='Canal')
        self._tv.heading('5', text='Threding')
        self._tv.heading('6', text='Visualizações')
        self._tv.heading('7', text='Likes')
        self._tv.heading('8', text='Dislikes')
        self._tv.heading('9', text='Comentarios')
        self._tv.heading('10', text='Descrução')
        self._tv.heading('11', text='Categoria')
        
        
        self._tv.column('0', width=90, minwidth=100)
        self._tv.column('1', width=90, minwidth=100)
        self._tv.column('2', width=90, minwidth=100)
        self._tv.column('3', width=90, minwidth=100)
        self._tv.column('4', width=90, minwidth=100)
        self._tv.column('5', width=90, minwidth=100)
        self._tv.column('6', width=90, minwidth=100)
        self._tv.column('7', width=90, minwidth=100)
        self._tv.column('8', width=90, minwidth=100)
        self._tv.column('9', width=90, minwidth=100)
        self._tv.column('10', width=90, minwidth=100)
        self._tv.column('11', width=90, minwidth=100)
        
        #ScrollBar    
        sb_y = ttk.Scrollbar(frame_right, orient=tk.VERTICAL, command=self._tv.yview)
        self._tv.configure(yscroll=sb_y.set)
        
        sb_x = ttk.Scrollbar(frame_right, orient=tk.HORIZONTAL, command=self._tv.xview)
        self._tv.configure(xscroll=sb_x.set)
        
        self._tv.grid(row=0, column=0)
        sb_y.grid(row=0, column=1, sticky='ns')
        sb_x.grid(row=1, column=0, sticky='we')
        
        
        #Menu de Busca
        v_titu = ttk.Label(frame_top, text='Titulo: ')
        v_titu.grid(row = 0, column = 0)
        e_titu = ttk.Entry(frame_top, width=40,textvariable=self._titulo)
        e_titu.grid(row = 0, column = 1, columnspan=3, sticky='W')
        rb_r = ttk.Radiobutton(frame_top, text='Titulo', value=1, variable=self._esc)
        rb_r.grid(row = 0, column = 5, sticky='E')
    
        
        v_canal = ttk.Label(frame_top, text='Canal: ')
        v_canal.grid(row = 1, column = 0)
        e_canal = ttk.Entry(frame_top, width=20, textvariable=self._canal)
        e_canal.grid(row = 1, column = 1, sticky='W')
        rb_r = ttk.Radiobutton(frame_top, text='Canal', value=2, variable=self._esc)
        rb_r.grid(row = 1, column = 5, sticky='E')       
        
        v_data_i = ttk.Label(frame_top, text='Inicio: ')
        v_data_i.grid(row = 2, column = 0)
        e_data_i= ttk.Entry(frame_top, width=10, textvariable=self._data_i)
        e_data_i.grid(row = 2, column = 1, sticky='W')
        
        v_data_f = ttk.Label(frame_top, text='Final: ')
        v_data_f.grid(row = 2, column = 2)
        e_data_f= ttk.Entry(frame_top, width=10, textvariable=self._data_f)
        e_data_f.grid(row = 2, column = 3, sticky='E')
        rb_r = ttk.Radiobutton(frame_top, text='Periodo', value=3, variable=self._esc)
        rb_r.grid(row = 2, column = 5, sticky='E')
        
        #Combobox categoria
        
        v_cat = ttk.Label(frame_top, text='Categoria: ')
        v_cat.grid(row = 3, column = 0, sticky='S')
        v_cb = ttk.Combobox(frame_top, width = 20, textvariable=self._categ,
                           state='readonly', values=self._categoria)
        v_cb.grid(row = 3, column=1, sticky='W')
        rb_r = ttk.Radiobutton(frame_top, text='Categoria', value=4, variable=self._esc)
        rb_r.grid(row = 3, column = 5, sticky='E')
        

        #Butões
        self.botoes['Buscar'] = ttk.Button(frame_top,text='Buscar')
        self.botoes['Buscar'].grid(row = 4, column = 3, sticky='E')
        self.botoes['Limpar'] = ttk.Button(frame_top,text='Limpar')
        self.botoes['Limpar'].grid(row = 4, column = 4, sticky='E')
        self.botoes['LimparB'] = ttk.Button(frame_top,text='Limpar Busca')
        self.botoes['LimparB'].grid(row = 4, column = 7, sticky='E')
        
        self.nome_arq.set('Arquivo escolhido: ')
        self.botoes['A_Arquivo'] = ttk.Button(frame_top, text='Abrir Arquivo')
        self.botoes['A_Arquivo'].grid(row = 4, column = 5, sticky='E')
        
        #Display quantidade de Videos
        
        v_quant = ttk.Label(frame_top,text='Videos encontrados: ')
        v_quant.grid(row = 7, column=0, columnspan=3, sticky='S')
        v_quant = ttk.Label(frame_top, text=self._quant)
        v_quant.grid(row = 7, column=2, sticky='S')
        
    def _atualiza_tv(self, lista):
        '''Modifica os valores da TreeVeiw'''
        self.remove_all()
        self._ltv = lista
        for i in self._ltv:
                self._tv.insert('', tk.END, values=i)

    def _limpar_selec(self):
        self._titulo.set('')
        self._canal.set('')
        self._data_i.set('')
        self._data_f.set('')    
        self._categ.set('')
         

    def remove_all(self):
        for record in self._tv.get_children():
            self._tv.delete(record)

    

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Buscador Youtube')
    gui = BuscaGUI(root)
    gui._atualiza_tv([['um','dois', 'tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze'],
    ['um','dois', 'tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze']])

    root.mainloop()
