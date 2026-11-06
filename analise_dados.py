import pandas as pd

# Carregar os dados do arquivo CSV
df = pd.read_csv('banco_atendimentos_ti_consolidado.csv', encoding='utf-8')

# Converter data para datetime
df['data_abertura'] = pd.to_datetime(df['data_abertura'], errors='coerce')
df['data_fechamento'] = pd.to_datetime(df['data_fechamento'], errors='coerce')

# 1. Tempo médio de atendimentos por mês durante o ano

# Filtrar apenas os chamados fechados/resolvidos
df_fechados = df.dropna(subset=['data_fechamento']).copy()

# calcular o tempo de atendimento em horas
df_fechados['tempo_atendimento'] = (df_fechados['data_fechamento'] - df_fechados['data_abertura']).dt.total_seconds() / 3600 

# Criar uma coluna para o mês e ano de abertura do chamado
df_fechados['ano_mes'] = df_fechados['data_abertura'].dt.to_period('M')

# Calcular a TMA (Tempo Médio de Atendimento) mensal por hora
tma_mensal = df_fechados.groupby('ano_mes')['tempo_atendimento'].mean().reset_index()

# Renomear as colunas para melhor entendimento
tma_mensal.columns = ['mes', 'tma_horas']

# Colocar o resultado em uma tabela no DataFrame
df_tma_mensal = pd.DataFrame(tma_mensal)

# 2. Total de atendimentos por tecnico durante o ano

# Agrupar por id e nome do tecnico e contar o número de atendimentos
atendimentos_por_tecnico = df.groupby(['id_tecnico', 'nome_tecnico']).size().reset_index(name='total_atendimentos')

# Colocar o resultado em uma tabela no DataFrame
df_atendimentos_por_tecnico = pd.DataFrame(atendimentos_por_tecnico)

# 3. Total de atendimentos por tipo de chamado durante o ano

# Agrupar por tipo de chamado e contar o número de atendimentos
atendimentos_por_tipo = df.groupby('categoria').size().reset_index(name='total_atendimentos')

# Colocar o resultado em uma tabela no DataFrame
df_atendimentos_por_tipo = pd.DataFrame(atendimentos_por_tipo)

# 4. Media diária de atendimentos geral

# Garantir que a média diária seja apenas o dia
df['data_dia'] = df['data_abertura'].dt.date

# Contar quantos atendimentos aconteceram em cada dia
atendimentos_diarios = df.groupby('data_dia').size().reset_index(name='total_atendimentos')

# Calcular a média diária de atendimentos
media_diaria = atendimentos_diarios['total_atendimentos'].mean()

# Colocar o resultado em uma tabela no DataFrame
df_media_diaria = pd.DataFrame({'media_diaria_atendimentos': [media_diaria]})

# 5. Total de atendimentos resolvidos por setor

# Agrupar por departamento e contar o número de atendimentos resolvidos
atendimentos_por_setor = df_fechados.groupby('departamento').size().reset_index(name='total_atendimentos')

# Colocar o resultado em uma tabela no DataFrame
df_atendimentos_por_setor = pd.DataFrame(atendimentos_por_setor)

# 5. Exportar dados para arquivo xlsx

# Nome do arquivo de saída
analise_atendimentos = 'analise_atendimentos.xlsx'

# Exportar os DataFrames para o arquivo Excel
with pd.ExcelWriter(analise_atendimentos, engine='openpyxl') as writer:
    df_atendimentos_por_setor.to_excel(writer, sheet_name='Atendimento_Setor', index=False)
    df_media_diaria.to_excel(writer, sheet_name='Media_Diaria', index=False)
    df_tma_mensal.to_excel(writer, sheet_name='TMA_Mensal', index=False)
    df_atendimentos_por_tecnico.to_excel(writer, sheet_name='Atendimento_Tecnico', index=False)
    df_atendimentos_por_tipo.to_excel(writer, sheet_name='Atendimento_Tipo', index=False)

print('DataFrame exportado com sucesso!')

# Exportar o banco de dados consolidado para o arquivo Excel
# df.to_excel('banco_atendimentos_ti_consolidado.xlsx', index=False, engine='openpyxl')
# print('Banco de dados consolidado exportado com sucesso!')