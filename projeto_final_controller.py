from projeto_final_modelo import Video, BaseDeDados
from projeto_final_view import BuscaGUI
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from tkinter.filedialog import askopenfilename

class ExcecaoModelo(Exception):
    pass

class ExcTituloInvalido(ExcecaoModelo):
    pass

class ExcTituloInvalido(ExcecaoModelo):
    pass


class BuscaController:
    '''Classe De controle da aplicação'''
    def __init__(self, model, view):
        '''Cria os atributos da classe controller'''
        self._model = model
        self._view = view
        self._config_but()
        
    def _config_but(self):
        '''metodo configura os botões e suas ações'''
        self._view.botoes['Buscar']['command'] = self._busca_video
        self._view.botoes['Limpar']['command'] = self._limpar_selec
        self._view.botoes['A_Arquivo']['command'] = self._add_arquivo
        
    def _busca_video(self):
        tit, canal,  datai, dataf, categor , rb = self._view._add_dados()
        if rb == '1':
            try: 
                if tit != '':
                    p = ['']
                    self._view._atualiza_tv(p)       
                    bt = self._model.busca_por_titulo(tit)
                    self._view._atualiza_tv(bt)
                else:
                    mb.showerror('Busca', 'Nenhum titulo inserido')
            except ExcTituloInvalido as err:
                mb.showerror('Busca', 'Nenhum titulo inserido')
        elif rb == '2':
            try:        
                if canal != '':
                    bt = self._model.busca_por_canal(canal)
                    self._view._atualiza_tv(bt)
                else:
                    mb.showerror('Busca', 'Nenhum canal inserido')
            except ExcTituloInvalido as err:
                mb.showerror('Busca', 'Nenhum canal inserido')
        elif rb == '3':
            try:        
                if datai != '' and dataf != '': 
                    bt = self._model.busca_por_periodo(datai, dataf)
                    self._view._atualiza_tv(bt)
                else:
                    mb.showerror('Busca', 'Nenhuma data inserida')
            except ExcTituloInvalido as err:
                mb.showerror('Busca', 'Nenhuma data inserida')
        elif rb == '4':
            try:        
                if categor != '': 
                    bt = self._model.busca_por_categoria(categor)
                    self._view._atualiza_tv(bt)
                else:
                    mb.showerror('Busca', 'Nenhuma categoria  selecionada' )
            except ExcTituloInvalido as err:
                mb.showerror('Busca', 'Nenhuma categoria  selecionada' )
        else:
            mb.showerror('Nenhuma Opção de Busca selecionada',\
              'Nenhuma Opção de Busca selecionada')    
        
    def seleciona_arquivo(self):
        self.tipos_arq = (
            ('Arquivos CSV', '*.csv'),
            ('Arquivos de texto', '*.txt'),
            ('Todos os arquivos', '*.*')
        )

        self.nome_arq  = askopenfilename(title='Abrir arquivo',\
                                   filetypes=self.tipos_arq)
        if self.nome_arq:
            return self.nome_arq
        
    def _add_arquivo(self):
        r = self.seleciona_arquivo() 
        p =  self._model.converter_video_lista(self._model.df)
        self._view._quant_v(len(self._model.df))
        self._view._atualiza_tv(p)

    def _limpar_selec(self):
        self._view._limpar_selec()
        

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Buscador Youtube')

    model = BaseDeDados('BR_youtube_trending_data_p1.csv')
    view = BuscaGUI(root)
    controller = BuscaController(model, view)

    root.mainloop()
