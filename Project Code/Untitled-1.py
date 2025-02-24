
from library import data
from library import names
from library import muni
from library import price
from library import list_mar
from library import dict_num_values
from library import dict_keys
from library import remove_duplicados
from library import media
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import pandas as pd

def list_hv():
    hv = []
    for i in names:
        if data[i]["municipality"] == "HV":
            hv.append(i)
    return hv

def list_anidada(l: list):
    new_list = []
    for i in l:
        if type(i) != list:
            new_list.append(i)
        else:
            new_list.extend(list_anidada(i))
    return new_list

def raiz(n: float, grado: float):
    fraction = 1/grado
    return n ** fraction


def potencia(n: float, exponente: float):
    return n ** exponente

potencia(0.57,4) - (2 * potencia(0.57,2))
