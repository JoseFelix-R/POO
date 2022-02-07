"""
    ! Classe usada para o modelo do projeto final
"""

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

    @staticmethod
    def inicializador(tupla):
        '''Inicializa as informações do Video'''
        v = Video()
        v.idvideo = tupla[0]
        v.titulo = tupla[1]
        v.datap = tupla[2]
        v.idcanal = tupla[3]
        v.canal = tupla[4]
        v.datat = tupla[5]
        v.qvisu = tupla[6]
        v.qlikes = tupla[7]
        v.qdislikes = tupla[8]
        v.qcom = tupla[9]
        v.desc = tupla[10]
        v.catin = tupla[11]
        return v

    def __str__(self):
        '''Metodo usado para saida das Informações de um video do youtube'''
        s = '----------------------------------------'
        return f'{self.canal}\n - {self.titulo}\n - {self.catin}\n - Views: {str(self.qvisu)}\n - Comentarios: {self.qcom}\n - Likes: {self.qlikes}\n Publicado em: {self.datap}\n {s}\n'


class BaseDeDados:
    '''
    Representa uma Base de Dados,
    responsável por realizar consultas
    em um arquivo Pandas.Dataframe.
    '''

    def __init__(self, nome_arq=''):
        '''
        Inicializa uma base de dados
        com o nome do arquivo (.csv)
        '''
        self.convert = ''

        # abre o dataframe e o atribui a um atributo de instância
        self.df = pd.read_csv(str(nome_arq), lineterminator='\n')

        # VEJA SEÇÃO 2.3.3 altera tipo das colunas data
        self.df.dt_publicacao = pd.to_datetime(self.df.dt_publicacao)
        self.df.dt_trending = pd.to_datetime(self.df.dt_trending)

        # SUBSTITUA df ABAIXO pelo atributo de instância
        # correspondente ao dataframe
        print(f'Arquivo: {nome_arq}')
        print(f'Possui dados dos vídeos em tendência no Youtube BR')
        print(f'Total de vídeos: {len(self.df)}')
        print(
            f'Período: {self.df.dt_publicacao.min()} até {self.df.dt_publicacao.max()}')
        print(f'Dados dos vídeos:')
        for c in self.df.columns.to_list():
            print(c, end=', ')

    def lista_categorias(self):
        '''
        Retorna lista contendo todas as categorias
        presentes no dataframe.
        '''

        # SUBSTITUA df ABAIXO pelo atributo de instância
        # correspondente ao dataframe
        return list(self.df.categoria.unique())

    @staticmethod
    def conversor(dataframe):
        res = [tup for tup in zip(dataframe.id_video, dataframe.titulo,
                                  dataframe.dt_publicacao, dataframe.id_canal,
                                  dataframe.canal, dataframe.dt_trending,
                                  dataframe.cont_views, dataframe.likes,
                                  dataframe.dislikes, dataframe.cont_comentarios,
                                  dataframe.descricao, dataframe.categoria)]

        lista_v = []
        for i in res:
            v = Video.inicializador(i)
            lista_v.append(v)
        for i in lista_v:
            print(i)
        return lista_v

    def busca_por_titulo(self, titulo):
        print('Buscando por titulo')
        t = titulo
        dataframe_t = self.df[self.df.titulo.str.contains(t, case=False)]
        self.convert = BaseDeDados.conversor(dataframe_t)
        return self.convert

    def busca_por_canal(self, nome_canal):
        n_canal = nome_canal
        dataframe_nc = self.df[self.df.canal.str.contains(n_canal, case=False)]
        self.convert = BaseDeDados.conversor(dataframe_nc)
        return self.convert

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

        categoria = categoria.capitalize()

        for chave, valor in categ.items():
            if valor == categoria:
                r = chave

        res = self.df[self.df.categoria == categ[r]]
        self.convert = BaseDeDados.conversor(res)
        return self.convert

    def busca_por_periodo(self, inicio, fim):
        self.df.dt_publicacao = pd.to_datetime(self.df.dt_publicacao)
        self.df.dt_trending = pd.to_datetime(self.df.dt_trending)

        masc = (self.df.dt_publicacao.dt.date >= pd.to_datetime(inicio)) & (
            self.df.dt_publicacao.dt.date <= pd.to_datetime(fim))

        res = self.df[masc]
        self.convert = BaseDeDados.conversor(res)
        return self.convert

    def __str__(self):
        r = self.convert
        s = '\nSaida do Programa:\n'
        for i in r:
            s += f'{i}\n'
        return s


if __name__ == '__main__':
    ld = BaseDeDados('BR_youtube_trending_data_p1.csv')
    
    print(ld.lista_categorias())
    #res = ld.busca_por_titulo('Palmeiras')
    #res = ld.busca_por_canal('Diana Demarchi')
    res = ld.busca_por_categoria('comedy') # também pode ser informado um nr. inteiro
    #res = ld.busca_por_periodo('2020-11-01', '2020-11-30')

    print('\n\n\n')
    for v in res:
        print(v)
