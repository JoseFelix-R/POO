from projeto_final_modelo import Video, BaseDeDados
from projeto_final_view import BuscaGUI
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
        pass
    
    def _limpar_selec(self):
        self._view._inicializar_vars.self._titulo.set('')
        self._view._inicializar_vars.self._canal.set('')
        self._view._inicializar_vars.self._data_i.set('')
        self._view._inicializar_vars.self._cata_f.set('')
        
        
    def seleciona_arquivo(self):
        self.tipos_arq = (
            ('Arquivos CSV', '*.csv'),
            ('Arquivos de texto', '*.txt'),
            ('Todos os arquivos', '*.*')
        )

        self.nome_arq  = askopenfilename(title='Abrir arquivo',\
                                   filetypes=self.tipos_arq)
        print(self.nome_arq)
        if self.nome_arq:
            return self.nome_arq
        
    
    def _add_arquivo(self):
        r = self.seleciona_arquivo()
        self._model.conversor = self._model.df
        p =  self._model.conversor
        self._view._atualiza_tv(p)

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Lista de Filmes')

    model = BaseDeDados('BR_youtube_trending_data_p1.csv')
    view = BuscaGUI(root)
    controller = BuscaController(model, view)

    root.mainloop()