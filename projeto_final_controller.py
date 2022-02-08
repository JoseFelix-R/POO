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
                    bt = self._model.busca_por_titulo(tit)
                    self._view._atualiza_tv(bt)
            except ExcTituloInvalido as err:
                mb.showerror('Busca', str(err))
            else:
                bt = self._model.busca_por_titulo(tit)
                self._view._atualiza_tv(bt)
                mb.showinfo('Busca', 'Busca por titulo realizada com sucesso')
        elif rb == '2':
            try:        
                if canal != '':
                    bt = self._model.busca_por_canal(canal)
                    self._view._atualiza_tv(bt)
                elif tit == '':
                    mb.showerror('Busca', str(err))
            except ExcTituloInvalido as err:
                mb.showerror('Busca', str(err))
            else:
                bt = self._model.busca_por_canal(canal)
                self._view._atualiza_tv(bt)
                mb.showinfo('Busca', 'Busca por canal realizada com sucesso')
        elif rb == '3':
            try:        
                if datai != '' and dataf != '': 
                    bt = self._model.busca_por_periodo(datai, dataf)
                    self._view._atualiza_tv(bt)
                elif tit == '':
                    mb.showerror('Busca', str(err))
            except ExcTituloInvalido as err:
                mb.showerror('Busca', str(err))
            else:
                bt = self._model.busca_por_periodo(datai,dataf)
                self._view._atualiza_tv(bt)
                mb.showinfo('Busca', 'Busca por periodo realizada com sucesso')
        elif rb == '4':
            try:        
                if categor != '': 
                    bt = self._model.busca_por_categoria(categor)
                    self._view._atualiza_tv(bt)
                elif tit == '':
                    mb.showerror('Busca', str(err))
            except ExcTituloInvalido as err:
                mb.showerror('Busca', str(err))
            else:
                bt = self._model.busca_por_categoria(categor)
                self._view._atualiza_tv(bt)
                mb.showinfo('Busca', 'Busca por categoria realizada com sucesso')
            
        else:
            mb.showerror('Nenhuma Opção de Busca selecionada',\
              'Nenhuma Opção de Busca selecionada')
    
    def _limpar_selec(self):
        self._view.self._inicializar_vars._titulo.set('')
        self._view.self._inicializar_vars._canal.set('')
        self._view.self._inicializar_vars._data_i.set('')
        self._view.self._inicializar_vars._cata_f.set('')
        
        
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
        #self._model.conversor(self._model.df) 
        p =  self._model.conversor(self._model.df)
       
        #for i, valor in enumerate(p):
        #    l.append(self.converter_video(valor[i]))
        

        self._view._r = str(len(self._model.df))
        self._view._atualiza_tv(p)
    

    def converter_video(self, video):
        self.info = video
        self.canal = str(self.info[0])
        self.titulo = str(self.info[1])
        self.categoria = str(self.info[2])
        self.views = str(self.info[3])
        self.coments = str(self.info[4])
        self.likes = str(self.infor[5])
        self.datap = str(self.info(6))
         
        self.t = [self.canal,self.titulo,self.categoria,self.views,self.coments,self.likes,self.datap]
        return self.t

    

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Buscador Youtube')

    model = BaseDeDados('BR_youtube_trending_data_p1.csv')
    view = BuscaGUI(root)
    controller = BuscaController(model, view)

    root.mainloop()
