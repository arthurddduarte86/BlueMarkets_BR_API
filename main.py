
# API creation using FastAPI
# pra executar uma API, abra o terminal na pasta
#     uvicorn main:bluecapmarket --reload
from fastapi import FastAPI
import pandas as pd
import time

bluecapmarket = FastAPI()

# Reading DataFrame with pandas
df = pd.read_csv('DataFrame_corp_data_for_database_CSV.csv')

# criar rotas ( routes )
@bluecapmarket.get("/")
def home(): 
    return {"Olá": "Bem vindo, visite /docs para mais informações"}

@bluecapmarket.get("/data")
def data(sum: bool = None, idtrans: int = None, describe: bool = None, cityMean: bool=None):
    if sum==True: 
        total = df['Value_Price'].sum()
        return ({"Total de Vendas: ": total})
    
    if (idtrans != None and idtrans >= 0):
        return df.loc[idtrans].to_dict() 
        
    if describe==True:
        return df.describe().to_dict()
    
    if (cityMean != None):
        return (df.groupby('City')['Value_Checkout'].mean()).to_dict()
        
        
@bluecapmarket.get("/backup")   
def backup(len:int):
    i=0
    while i < len :
        yield (df.loc[i].to_dict()) 
        #time.sleep(0.1)
        i+=1
        