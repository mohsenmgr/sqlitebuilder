import pandas as pd
import sqlite3

excel_file = './Plant_SACHIM_v080623ML.xlsx'
sheet_name = 'Plant'
df = pd.read_excel(excel_file,sheet_name)

column_mapping = {
'Codice Stabilimento':'CodiceStabilimento'
,'Descrizione Stabilimento':'DescrizioneStabilimento'
,'Edificio':'Edificio'
,'Vettore':'Vettore'
,'POD':'POD'
,'Piano':'Piano'
,'Reparto':'Reparto'
,'Quadro':'Quadro'
,'Descrizione Quadro':'DescrizioneQuadro'
,'Sottoquadro':'Sottoquadro'
,'Descrizione Sottoquadro':'DescrizioneSottoquadro'
,'Linea':'Linea'
,'Descrizione Linea':'DescrizioneLinea'
,'Area Funzionale ENEA':'AreaFunzionaleENEA'
,'Cod. Funzionale TERA':'Cod.FunzionaleTERA'
,'Tipologia Dispositivo':'TipologiaDispositivo'
,'Codice Modello Dispositivo':'CodiceModelloDispositivo'
,'Taglia Interruttore':'TagliaInterruttore'
,'Tipologia Misura':'TipologiaMisura'
,'Hostname Edge':'HostnameEdge'
,'ID Modbus':'IDModbus'
,'Tipo Dispositivo':'TipoDispositivo'
}



df_selected = df.rename(columns=column_mapping)[list(column_mapping.values())]

sqlite_db = './sqlite_database.db'
conn = sqlite3.connect(sqlite_db)


table_name = 'real_variables'
df.to_sql(table_name,conn,if_exists='replace', index=False)

conn.close()
