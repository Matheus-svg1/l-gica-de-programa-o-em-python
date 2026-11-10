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
            