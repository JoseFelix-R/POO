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

    def __str__(self):
        '''Metodo usado para saida das Informações de um video do youtube'''
        return f'{self.titulo} - {self.datap} - {self.canal} - {self.datat} - {self.qvisu} - {self.qlikes} - {self.qdislikes} - {self.qcom} - {self.desc} - {self.catin} '


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
        # abre o dataframe e o atribui a um atributo de instância
        self.df = pd.read_csv(str(nome_arq), lineterminator='\n')
        # VEJA SEÇÃO 2.3.3 altera tipo das colunas data

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


if __name__ == '__main__':
    ld = BaseDeDados('BR_youtube_trending_data_completo.csv')
    print('\n\n\n')
    print(ld.lista_categorias())
    #res = ld.busca_por_titulo('fla')
    #res = ld.busca_por_canal('espor')
    # res = ld.busca_por_categoria('SPORTS') # também pode ser informado um nr. inteiro
    #res = ld.busca_por_periodo('2020-11-01', '2020-11-30')

    # print('\n\n\n')
    # for v in res:
    #  print(v)
    print('\n\n\n')
    v = Video()
    v.idvideo = 'YT@#$34'
    v.titulo = 'Tiringa Rindo'
    v.datap = '24/01/2021'
    v.idcanal = 'BR$#$%SEL'
    v.canal = 'Brasil Selvagem'
    v.datat = '30/11/2021'
    v.qvisu = 10900089
    v.qlikes = 120098
    v.qdislikes = 1190
    v.qcom = 845
    v.desc = 'Esse é um video do tiringa se divertindo com Tõe'
    v.catin = 'Comedy'

    print(v)
