import tkinter as tk
from tkinter import messagebox 
import json
import os

arquivo = "dados.json"

def dados():
    if not os.path.exists(arquivo):
        return[]
    try:
        with open(arquivo, "r", encoding= "utf-8") as f:
            return json.load(f)
        
    except json.JSONDecodeError:
        return []
    
    
def salvar_dados(estoque):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii= False, indent= 4)
        
        
    
    
    
    
    