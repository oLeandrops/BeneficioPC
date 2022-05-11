import pandas as pd
def tratarbase(arquivo_old,arquivo_new):
    df1 = pd.read_csv(arquivo_old, sep=';', encoding='ISO-8859-1')
    df2 = pd.read_csv(arquivo_new, sep=';', encoding='ISO-8859-1')
    df1 = df1.rename(columns={'MÊS COMPETÊNCIA': 'MES_COMPETENCIA',
                              'MÊS REFERÊNCIA': 'MES_REFERENCIA',
                              'CÓDIGO MUNICÍPIO SIAFI': 'CODIGO_MUNICIPIO_SIAFI',
                              'NOME MUNICÍPIO': 'NOME_MUNICIPIO',
                              'NIS BENEFICIÁRIO': 'NIS_BENEFICIARIO',
                              'CPF BENEFICIÁRIO': 'CPF_BENEFICIARIO',
                              'NOME BENEFICIÁRIO': 'NOME_BENEFICIARIO',
                              'NIS REPRESENTANTE LEGAL': 'NIS_REPRESENTANTE_LEGAL',
                              'NÚMERO BENEFÍCIO': 'NUMERO_BENEFICIO',
                              'BENEFÍCIO CONCEDIDO JUDICIALMENTE': 'BENEFICIO_CONCEDIDO_JUDICIALMENTE',
                              'VALOR PARCELA': 'VALOR_PARCELA',
                              'NOME REPRESENTANTE LEGAL': 'NOME_REPRESENTANTE_LEGAL',
                              'CPF REPRESENTANTE LEGAL': 'CPF_REPRESENTANTE_LEGAL'})
    df2 = df2.rename(columns={'MÊS COMPETÊNCIA': 'MES_COMPETENCIA',
                              'MÊS REFERÊNCIA': 'MES_REFERENCIA',
                              'CÓDIGO MUNICÍPIO SIAFI': 'CODIGO_MUNICIPIO_SIAFI',
                              'NOME MUNICÍPIO': 'NOME_MUNICIPIO',
                              'NIS BENEFICIÁRIO': 'NIS_BENEFICIARIO',
                              'CPF BENEFICIÁRIO': 'CPF_BENEFICIARIO',
                              'NOME BENEFICIÁRIO': 'NOME_BENEFICIARIO',
                              'NIS REPRESENTANTE LEGAL': 'NIS_REPRESENTANTE_LEGAL',
                              'NÚMERO BENEFÍCIO': 'NUMERO_BENEFICIO',
                              'BENEFÍCIO CONCEDIDO JUDICIALMENTE': 'BENEFICIO_CONCEDIDO_JUDICIALMENTE',
                              'VALOR PARCELA': 'VALOR_PARCELA',
                              'NOME REPRESENTANTE LEGAL': 'NOME_REPRESENTANTE_LEGAL',
                              'CPF REPRESENTANTE LEGAL': 'CPF_REPRESENTANTE_LEGAL'})
    df1['NIS_BENEFICIARIO'] = df1['NIS_BENEFICIARIO'].astype('str')
    df2['NIS_BENEFICIARIO'] = df2['NIS_BENEFICIARIO'].astype('str')
    df1['NIS_REPRESENTANTE_LEGAL'] = df1['NIS_REPRESENTANTE_LEGAL'].astype('str')
    df2['NIS_REPRESENTANTE_LEGAL'] = df2['NIS_REPRESENTANTE_LEGAL'].astype('str')
    df1['CODIGO_MUNICIPIO_SIAFI'] = df1['CODIGO_MUNICIPIO_SIAFI'].astype('str')
    df2['CODIGO_MUNICIPIO_SIAFI'] = df2['CODIGO_MUNICIPIO_SIAFI'].astype('str')
    df1['NUMERO_BENEFICIO'] = df1['NUMERO_BENEFICIO'].astype('str')
    df2['NUMERO_BENEFICIO'] = df2['NUMERO_BENEFICIO'].astype('str')
    df1['VALOR_PARCELA'] = df1['VALOR_PARCELA'].apply(lambda x: str(x).replace(',', '.'))
    df2['VALOR_PARCELA'] = df2['VALOR_PARCELA'].apply(lambda x: str(x).replace(',', '.'))
    df1['VALOR_PARCELA'] = df1['VALOR_PARCELA'].astype('float64')
    df2['VALOR_PARCELA'] = df2['VALOR_PARCELA'].astype('float64')
    #df1['BENEFICIO_CONCEDIDO_JUDICIALMENTE'] = df1['BENEFICIO_CONCEDIDO_JUDICIALMENTE'].apply(
    #    lambda x: str(x).replace('�', 'A'))
    #df2['BENEFICIO_CONCEDIDO_JUDICIALMENTE'] = df2['BENEFICIO_CONCEDIDO_JUDICIALMENTE'].apply(
     #   lambda x: str(x).replace('�', 'A'))
    tabelaMerge = df1.merge(df2, on='NUMERO_BENEFICIO', how='right')
    BaseDadosNovos = tabelaMerge[
        ['NUMERO_BENEFICIO', 'MES_COMPETENCIA_x', 'MES_COMPETENCIA_y', 'MES_REFERENCIA_y', 'UF_y',
         'CODIGO_MUNICIPIO_SIAFI_y'
            , 'NOME_MUNICIPIO_y', 'NIS_BENEFICIARIO_y', 'CPF_BENEFICIARIO_y', 'NOME_BENEFICIARIO_y',
         'NIS_REPRESENTANTE_LEGAL_y', 'CPF_REPRESENTANTE_LEGAL_y'
            , 'NOME_REPRESENTANTE_LEGAL_y', 'BENEFICIO_CONCEDIDO_JUDICIALMENTE_y'
            , 'VALOR_PARCELA_y']].loc[tabelaMerge['MES_COMPETENCIA_x'].isnull()]
    BaseDadosNovos.to_csv('basenovosregistros.csv')
    tabelaMerge = df1.merge(df2, on='NUMERO_BENEFICIO', how='left')
    BaseNovosExcluidos = tabelaMerge[
        ['NUMERO_BENEFICIO', 'MES_COMPETENCIA_y', 'MES_COMPETENCIA_x', 'MES_REFERENCIA_x', 'UF_x',
         'CODIGO_MUNICIPIO_SIAFI_x'
            , 'NOME_MUNICIPIO_x', 'NIS_BENEFICIARIO_x', 'CPF_BENEFICIARIO_x', 'NOME_BENEFICIARIO_x',
         'NIS_REPRESENTANTE_LEGAL_x', 'CPF_REPRESENTANTE_LEGAL_x'
            , 'NOME_REPRESENTANTE_LEGAL_x', 'BENEFICIO_CONCEDIDO_JUDICIALMENTE_x'
            , 'VALOR_PARCELA_x']].loc[tabelaMerge['MES_COMPETENCIA_y'].isnull()]
    BaseNovosExcluidos.to_csv('basenovosexcluidos.csv')
    print('Arquivo Criado Com sucesso!')

if __name__ == '__main__':
    tratarbase('202203_BPC.csv','202204_BPC.csv')