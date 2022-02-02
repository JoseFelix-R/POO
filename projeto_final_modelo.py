import pandas as pd

class Video:
    '''
    Representa um vídeo do Youtube.
    '''
    def __init__(self, idvideo='padrao', titulo='padrao', dt_publicacao='01/01/2022', idcanal='idpadrao', canal='padrao', datat='0/0/0', cont_views=0, likes=0, dislikes=0, cont_comentarios=0, descricao='padrao', categoria='ALL'):
        self.idvideo = idvideo
        self.titulo = titulo 
        self.datap = dt_publicacao
        self.idcanal = idcanal
        self.canal = canal
        self.datat = datat
        self.qvisu = cont_views
        self.qlikes = likes
        self.qdislikes = dislikes
        self.qcom = cont_comentarios
        self.desc = descricao
        self.catin = categoria
        
    def inicializador(self, video):
        '''Inicializa as informações do Video'''
        self.idvideo = video[0]
        self.titulo = video[1] 
        self.datap = video[2] 
        self.idcanal = video[3] 
        self.canal = video[4] 
        self.datat = video[5] 
        self.qvisu = video[6] 
        self.qlikes = video[7] 
        self.qdislikes = video[8] 
        self.qcom = video[9]
        self.desc = video[10]
        self.catin = video[11]
   
        
    def __str__(self):
        '''Metodo usado para saida das Informações de um video do youtube'''    
        return f'{self.canal}\n - {self.titulo}\n - {self.catin}\n - Views: {str(self.qvisu)}\n - Comentarios: {self.qcom}\n - Likes: {self.qlikes}\n Publicado em: {self.datap}\n {"------------------------------"}'
    
        

class BaseDeDados:
    '''
    Representa uma Base de Dados,
    responsável por realizar consultas
    em um arquivo Pandas.Dataframe.
    '''
    
    def __init__(self, nome_arq):
        '''
        Inicializa uma base de dados
        com o nome do arquivo (.csv)
        '''
        
        ## abre o dataframe e o atribui a um atributo de instância
        self.df = pd.read_csv(str(nome_arq), lineterminator='\n')
        
        self.c = BaseDeDados.convert(self) 
        
        ## VEJA SEÇÃO 2.3.3 altera tipo das colunas data
        self.df.dt_publicacao = pd.to_datetime(self.df.dt_publicacao)
        self.df.dt_trending = pd.to_datetime(self.df.dt_trending)
        
        ## SUBSTITUA df ABAIXO pelo atributo de instância
        ## correspondente ao dataframe
        print(f'Arquivo: {nome_arq}')
        print(f'Possui dados dos vídeos em tendência no Youtube BR')
        print(f'Total de vídeos: {len(self.df)}')
        print(f'Período: {self.df.dt_publicacao.min()} até {self.df.dt_publicacao.max()}')
        print(f'Dados dos vídeos:')
        for c in self.df.columns.to_list():
            print(c, end=', ')
    
    def lista_categorias(self):
        '''
        Retorna lista contendo todas as categorias
        presentes no dataframe.
        '''
        
        ## SUBSTITUA df ABAIXO pelo atributo de instância
        ## correspondente ao dataframe
        return list(self.df.categoria.unique())
    
    def convert(self):
        res = [tup for tup in zip(self.df.id_video, self.df.titulo,
                          self.df.dt_publicacao, self.df.id_canal,
                          self.df.canal, self.df.dt_trending,
                          self.df.cont_views, self.df.likes,
                          self.df.dislikes, self.df.cont_comentarios,
                          self.df.descricao, self.df.categoria)]
        
        i = Video.inicializador(self, res)
      
    def busca_por_titulo(self, titulo):
        print('Buscando por titulo')
        r = []  
        c = self.df.titulo.str.contains(titulo, case=False)
        print(c)
        for i in c:
            if c == True:
                r.append(tup)
        return r
        
            

    def busca_por_canal(self, nome_canal):
        res = self.df[self.df.canal == nome_canal]
        display(res)
    
    def busca_por_categoria(self, categoria):
        categ = {'29': 'Nonprofits & Activism',
         '1': 'Film & Animation', 
         '2': 'Autos & Vehicles', 
         '10': 'Music', 
         '15': 'Pets & Animals', 
         '17': 'Sports', 
         '18': 'Short Movies', 
         '19': 'Travel & Events', 
         '20': 'Gaming', 
         '21': 'Videoblogging', 
         '22': 'People & Blogs', 
         '23': 'Comedy', 
         '24': 'Entertainment', 
         '25': 'News & Politics', 
         '26': 'Howto & Style', 
         '27': 'Education', 
         '28': 'Science & Technology', 
         '30': 'Movies', 
         '31': 'Anime/Animation', 
         '32': 'Action/Adventure', 
         '33': 'Classics', 
         '34': 'Comedy', 
         '35': 'Documentary', 
         '36': 'Drama', 
         '37': 'Family', 
         '38': 'Foreign', 
         '39': 'Horror', 
         '40': 'Sci-Fi/Fantasy', 
         '41': 'Thriller', 
         '42': 'Shorts', 
         '43': 'Shows', 
         '44': 'Trailers'}
       
        res = self.df[self.df.categoria == categ['24']]
        display(res)
    
    def busca_por_periodo(self,inicio, fim):
        self.df.dt_publicacao = pd.to_datetime(self.df.dt_publicacao)
        self.df.dt_trending = pd.to_datetime(self.df.dt_trending)
        # Retorna um dataframe contendo todos os vídeos
        # no período que envolve a data 'ini' e data 'fim'
        masc = (self.df.dt_publicacao.dt.date >= pd.to_datetime(inicio)) & (self.df.dt_publicacao.dt.date <= pd.to_datetime(fim))

        # masc é uma expressão que gera um 'vetor' de True/False; este vetor é então utilizado para retornar o dataframe resultante
        res = self.df[masc]
        display(res)

    def __str__(self):
        s = '\nSaida do Programa:\n' 
        
        return s

