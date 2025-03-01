
# Biblioteca para el análisis de los restaurantes #

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import seaborn as sns
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning, message="Mean of empty slice")
warnings.filterwarnings("ignore", category=RuntimeWarning, message="invalid value encountered in scalar divide")
warnings.filterwarnings("ignore", category=RuntimeWarning, message="All-NaN slice encountered")
warnings.filterwarnings("ignore", category=UserWarning, message="Creating legend with loc='best' can be slow with large amounts of data")

# Importación de los archivos .json #

p = "menu.json"
data = pd.read_json(p)

with open("municipality.json") as m:
    muni = json.load(m)

x = ['AN', 'BY', 'CH', 'CR', 'CT', 'DO', 'GB', 'HE', 'HV','LL','MR','PY','PR','RG','SM']
municipios = ["Arroyo Naranjo","Boyero","Centro Habana","Cotorro","Cerro","Diez de Octubre","Guanabacoa","Habana del Este","Habana Vieja","La Lisa","Marianao","Playa","Plaza de la Revolución","Regla","San Miguel del Padrón"]
df_municipality = pd.DataFrame({
    "Abreviatura": x,
    "Nombre Completo Del Municipio": municipios
})

names = []
for n in data:
    names.append(n)
 
# Lista de los restaurantes # 
def list_restaurant():
   places = {
    "Restaurantes": names
   }
   df = pd.DataFrame(places)
   pd.set_option('display.max_rows', None)
   return df

# Conteo de Restaurantes por municipio #

an = 0
by = 0
ch = 0
ct = 0
cr = 0
do = 0
gb = 0
he = 0
hv = 0
ll = 0
mr = 0
py = 0
pr = 0
rg = 0
sm = 0

for i in names:
    count = data[i]["municipality"]
    if count == "AN":
        an += 1
    if count == "BY":
        by += 1
    if count == "CH":
        ch += 1
    if count == "CT":
        ct += 1
    if count == "CR":
        cr += 1
    if count == "DO":
        do += 1
    if count == "GB":
        gb += 1
    if count == "HE":
        he += 1
    if count == "HV":
        hv += 1
    if count == "LL":
        ll += 1
    if count == "MR":
        mr += 1
    if count == "PY":
        py += 1
    if count == "PR":
        pr += 1
    if count == "RG":
        rg += 1
    if count == "SM":
        sm += 1
    else:
        continue

muny = [an,by,ch,ct,cr,do,gb,he,hv,ll,mr,py,pr,rg,sm]

def count_muni():
    print(f"Arroyo Naranjo : {an}")
    print(f"Boyero : {by}")
    print(f"Centro Habana : {ch}")
    print(f"Cotorro : {ct}" )
    print(f"Cerro : {cr}")
    print(f"Diez de Octubre : {do}")
    print(f"Guanabacoa : {gb}")
    print(f"Habana del Este : {he}")
    print(f"Habana Vieja : {hv}")
    print(f"La Lisa : {ll}")
    print(f"Marianao : {mr}")
    print(f"Playa : {py}")
    print(f"Plaza de la Revolución : {pr}")
    print(f"Regla : {rg}")
    print(f"San Miguel del Padrón : {sm}")
    print(f"Total : {sum(muny)}")

# Función para sacar los valores enteros y flotantes de un diccionario y añadirlos a una lista #

def dict_num_values(l : dict):
   lista = []
   if type(l) == dict:
      for i in l.values():
          if type(i) == int or type(i) == float:
              lista.append(i)
          else:
              lista.extend(dict_num_values(i))
  
   return lista

def dict_keys(l : dict):
   lista = []
   if type(l) == dict:
      for i in l.keys():
          if type(i) == str or type(i) == str:
              lista.append(i)
          else:
              lista.extend(dict_num_values(i))
   return lista

# Función para Calular la media de los precios de un tipo plato en especifico en un municipio #

def media(x: str,y: str):
   for a in names:
      cart = data[a]["municipality"]
      if cart == x: 
         m = data[a]["menu"]
         for b in m:
            if b == y:
               n = data[a]["menu"][y]
               lista = dict_num_values(n)
   median = np.nanmedian(lista)
   return median

def search(origen: str, entrada: str):
    return origen.upper().count(entrada.upper())

# Cálculo para un plato en específico por municipio #

def especific_dish_median(muni: str,types: str, dish: str):
    lista = []
    for i in names:
        if data[i]["municipality"] == muni:
            menu = data[i]["menu"]
            for m in menu:
                if m == types:
                    dr = menu[types]
                    for d in dict_keys(dr):
                        if d.upper().count(dish.upper()) > 0:
                           beer = dr[d]
                           valores = dict_num_values(beer)
                           lista.extend(dict_num_values(beer))
                           if type(beer) == int or type(beer) == float:
                               lista.append(beer)
                           else:
                            continue
                        else:
                            continue
                else:
                    continue
        else: continue
    return np.median(lista)

# Cálculo para un plato en específico en general para análizar lagares mas baratos y mas caros #

def dish(types: str, dish: str, rango: int, list_caros: list, list_baratos: list):
    lista = []
    for i in names:
            menu = data[i]["menu"]
            for m in menu:
                if m == types:
                    dr = menu[types]
                    for d in dr:
                        if d.upper().count(dish.upper()) > 0:
                           beer = dr[d]
                           valores = dict_num_values(beer)
                           precio_maximo = max(valores)
                           lista.extend(dict_num_values(beer))
                           if type(beer) == int or type(beer) == float:
                               lista.append(beer)
                           else:
                            continue
                        else:
                            continue
                else:
                    continue
    return np.median(lista)

#  Cálculo para los mariscos#
  
def median_mariscos(muni: str):
    lista = []
    for i in names:
        if data[i]["municipality"] == muni:
            menu = data[i]["menu"]
            for m in menu:
                if m == "main_dishes":
                    dr = menu["main_dishes"]
                    for d in dict_keys(dr):
                        if d.upper().count(" marisc ".upper()) > 0 or d.upper().count(" mar ".upper()) > 0 or d.upper().count(" mar".upper()) > 0 or d.upper().count("mar ".upper()) > 0:
                           beer = dr[d]
                           lista.extend(dict_num_values(beer))
                           if type(beer) == int or type(beer) == float:
                               lista.append(beer)
                           else:
                            continue
                        else:
                            continue
                else:
                    continue
        else: continue
    return np.median(lista)


# COMPARACIÓN DE LOS PRECIOS DE LAS CERVEZAS Y LOS REFRESCOS COMPARADOS CON OTROS LÍQUIDOS #

def drinks():
    drink = ["CERVEZAS", "REFRESCOS", "OTROS LÍQUIDOS"] 
    beers = []
    softdrinks = []
    others = []
    total = []
    for i in names:
        menu = data[i]["menu"]
        for m in menu:
            if m == "drinks":
                dr = menu["drinks"]
                for d in dr:
                    if d.upper().count("cerveza".upper()) > 0:
                        beer = dr[d]
                        if type(beer) == int or type(beer) == float:
                            beers.append(beer)
                        else:
                            beers.extend(dict_num_values(beer))
                    if d.upper().count("refresco".upper()) > 0:
                        softdrink = dr[d]
                        if type(softdrink) == int or type(softdrink) == float:
                            softdrinks.append(softdrink)
                        else:
                            softdrinks.extend(dict_num_values(softdrink))
                    else:
                        other = dr[d]
                        if type(other) == int or type(other) == float:
                            others.append(other)
                        else:
                            others.extend(dict_num_values(other))
            else:
                continue
    mediana_beers = float(np.median(beers))
    mediana_softdrinks = float(np.median(softdrinks))
    mediana_others = float(np.median(others))

    total.append(mediana_beers)
    total.append(mediana_softdrinks)
    total.append(mediana_others)

    plt.bar(drink, total, color = ["y","r","b"])
    plt.xlabel("BEBIDAS")
    plt.ylabel("PRECIOS")
    plt.title("COMPARACIÓN DE LOS PRECIOS DE LAS CERVEZAS Y LOS REFRESCOS COMPARADOS CON OTROS LÍQUIDOS")
    plt.show()  

# Función para gráficar #


def pyplot_bar(y: list, title: str):
    colors = ["r", "r", "g", "r", "r", "r", "r", "r", "g", "r", "r", "g", "g", "r", "r"]
    etiquetas = {"r": "Municipios Con Pocos Turístas", "g": "Municipios Con Muchos Turístas"}
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color=colors)
    plt.xlabel("MUNICIPIOS")
    plt.ylabel("CANTIDAD")
    plt.title(title)
    handles = [plt.Rectangle((0,0),1,1, color=color, label=label) for color, label in etiquetas.items()]
    plt.legend(handles=handles)
    plt.show()

# Funcón para contar los lugares con mensajería por municipio #

deliver = []
for mss in names:
    dlv = data[mss]["messenger"]
    if dlv  == True:
        deliver.append(mss)
porcent_deliver = (len(deliver) / len(names)) * 100

def deliver(d: str):
    delivers = []
    for i in data:
        de = data[i]["messenger"]
        mnp = data[i]["municipality"]
        if de == True and mnp == d:
            delivers.append(i)
    return len(delivers)

dlvrs = []

for dvs in x:
    dlvrs.append(deliver(dvs))


# Precios#

def dish_median(index: str):
    bkf = "breafasts"
    lbkf = []
    ent = "appetizers"
    lent = []
    plp = "main_dishes"
    lplp = []
    ftt = "fittings"
    lftt = []
    pzz = "pizzas"
    lpzz = []
    agg = "aggregation"
    lagg = []
    crm = "creams"
    lcrm = []
    pst = "pastes"
    lpst = []
    sps = "soups"
    lsps = []
    brd = "breads"
    lbrd = []
    dsr = "desserts"
    ldsr = []
    drk = "drinks"
    ldrk = []
    bar = "bar"
    lbar = []
    ctn = "containers"
    lctn = []
    inf = "infusions"
    linf = []
    for i in names:
        if i == index:
            menu = data[i]["menu"]
            for r in menu:
                if r == bkf:
                    values =  menu[r].values()
                    for bk in values:
                        if type(bk) == int or type(bk) == float:
                            lbkf.append(bk)
                        else:
                           lbkf.extend(dish_median(bk))
                if r == ent:
                    values =  menu[r].values()
                    for en in values:
                        if type(en) == int or type(en) == float:
                            lent.append(en)
                        else:
                            lent.extend(dish_median(en))
                if r == plp:
                    values =  menu[r].values()
                    for pl in values:
                        if type(pl) == int or type(pl) == float:
                            lplp.append(pl)
                        else:
                            lplp.extend(dish_median(pl))
                if r == ftt:
                    values =  menu[r].values()
                    for ft in values:
                        if type(ft) == int or type(ft) == float:
                            lftt.append(ft)
                        else:
                            lftt.extend(dish_median(ft))
                if r == pzz:
                    values =  menu[r].values()
                    for pz in values:
                        if type(pz) == int or type(pz) == float:
                            lpzz.append(pz)
                        else:
                            lpzz.extend(dish_median(pz))
                if r == agg:
                    values =  menu[r].values()
                    for ag in values:
                        if type(ag) == int or type(ag) == float:
                            lagg.append(ag)
                        else:
                            lagg.extend(dish_median(ag))
                if r == crm:
                    values =  menu[r].values()
                    for cr in values:
                        if type(cr) == int or type(cr) == float:
                            lcrm.append(cr)
                        else:
                            lcrm.extend(dish_median(cr))
                if r == pst:
                    values =  menu[r].values()
                    for pst in values:
                        if type(pst) == int or type(pst) == float:
                            lpst.append(pst)
                        else:
                            lpst.extend(dish_median(pst))
                if r == sps:
                    values =  menu[r].values()
                    for sp in values:
                        if type(sp) == int or type(sp) == float:
                            lsps.append(sp)
                        else:
                            lsps.extend(dish_median(sp))
                if r == brd:
                    values =  menu[r].values()
                    for br in values:
                        if type(br) == int or type(br) == float:
                            lbrd.append(br)
                        else:
                            lbrd.extend(dish_median(br))
                if r == dsr:
                    values =  menu[r].values()
                    for ds in values:
                        if type(ds) == int or type(ds) == float:
                            ldsr.append(ds)
                        else:
                            ldsr.extend(dish_median(ds))
                if r == drk:
                    values =  menu[r].values()
                    for dk in values:
                        if type(dk) == int or type(dk) == float:
                            ldrk.append(dk)
                        else:
                            ldrk.extend(dish_median(dk))
                if r == bar:
                    values =  menu[r].values()
                    for b in values:
                        if type(b) == int or type(b) == float:
                            lbar.append(b)
                        else:
                            lbar.extend(dish_median(b))
                if r == ctn:
                    values =  menu[r].values()
                    for ct in values:
                        if type(ct) == int or type(ct) == float:
                            lctn.append(ct)
                        else:
                            lctn.extend(dish_median(ct))
                if r == inf:
                    values =  menu[r].values()
                    for nf in values:
                        if type(nf) == int or type(nf) == float:
                            linf.append(nf)
                        else:
                            linf.extend(dish_median(nf))
                else:
                    continue
        else:
            continue    
    dishes = [lbkf, lent, lplp, lftt, lpzz, lagg, lcrm, lpst, lsps, lbrd, ldsr, ldrk, lbar, lctn, linf]
    median = []
    for r in dishes:
        median.append(float(np.nanmedian(r)))
    return median

def price(index:str):
    budget = np.nansum(dish_median(index))
    return int(budget)

# Salary

salaries = muni["LH"]["salario_medio_en_2023"] 
salary = []

for s in names:
    bt = price(s)
    if bt <= salaries:
        salary.append(s)

porcent = (len(salary) / len(names) * 100)

def posibility(p: str):
    l = []
    for calc in salary:
        cc = data[calc]["municipality"]
        if cc == p:
            l.append(calc)
    return len(l)

pb = []
for pby in x:
    pb.append(posibility(pby))

def median_for_municipality():
    mnc = [[] for i in range(15)]
    for i in names:
        for o in x:
            if data[i]["municipality"] == o:
                m_index = x.index(o)
                mnc[m_index].append(price(i))
    mediana_for_region = []
    for z in mnc:
        median = np.median(z)
        mediana_for_region.append(median)
    df_median = pd.DataFrame({
             "restaurante": municipios,
             "Costos Media De Los Restaurantes Por Municipio": mediana_for_region
    })
    return df_median

# Mapas y Datos de lugares

name = []
coordinates = []
lat = []
long = []
budget = []
delivers = []
phone = []

def phones():
    pn = data[cds]["phone_number"]
    if pd.isna(pn):
        phone.append("El local no tiene teléfono")
    else:
        phone.append(pn)

def date():
    name.append(cds)
    bgt = price(idx)
    budget.append(bgt)
    phones()

for cds in names:
    coordinate = data[cds]["coordinates"]
    idx = names.index(cds)
    if type(coordinate) == list and len(coordinate) == 2:
        coordinates.append(coordinate)
        date()  
    else:
        coordinates.append([0,0])
        date()
            
for cc in coordinates:
    if len(cc) > 0:
        lat.append(cc[0])
        long.append(cc[1])
      
ubications = {
    "name": name,
    "latitud": lat,
    "longitud": long,
    "budget": budget,
    "phone": phone
}
ub = pd.DataFrame(ubications)

def map():
    map = folium.Map(location=[23.1057291,-82.3581364], zoom_start=10)
    for i, mp in ub.iterrows():
        folium.Marker(location=[mp.latitud, mp.longitud], popup=f"{mp['name']} , gasto mínimo(todos los tipos de platos) sin incluir por ciento por el servicio : {mp['budget']}, teléfono : {mp['phone']}" ).add_to(map)
    return map

def search_person():
    m = str(input("Por Favor, ¿ Digame a que municipiode La Habana de gustaría ir a comer ? : "))
    b = int(input(" ¿ Con qué presupuesto cuentas ? : "))
    k = str(input(" ¿ Qué tipo de cocina que interesaría comer ?"))
    c = str(input(" ¿ Le gustaría ver las cartas ? : "))
    if type(b) != int:
        print("debe introducir un número")

    if "Arroyo Naranjo".upper().count(m.upper()) > 0:
        m = "AN"
    if "Boyero".upper().count(m.upper()) > 0:
        m = "BY"
    if "Centro Habana".upper().count(m.upper()) > 0:
        m = "CH"
    if  "Cotorro".upper().count(m.upper()) > 0:
        m = "CT"
    if  "Cerro".upper().count(m.upper()) > 0:
        m = "CR"
    if "Diez de Octubre".upper().count(m.upper()) > 0:
        m = "DO"
    if "Guanabacoa".upper().count(m.upper()) > 0:
        m = "GB"
    if "Habana del Este".upper().count(m.upper()) > 0:
        m = "HE"
    if "Habana Vieja".upper().count(m.upper()) > 0:
        m = "HV"
    if "La Lisa".upper().count(m.upper()) > 0:
        m = "LL"
    if "Marianao".upper().count(m.upper()) > 0:
        m = "MR"
    if "Playa".upper().count(m.upper()) > 0:
        m = "PY"
    if "Plaza de la Revolución".upper().count(m.upper()) > 0:
        m = "PR"
    if "Regla".upper().count(m.upper()) > 0:
        m = "RG"
    if "San Miguel del Padrón".upper().count(m.upper()) > 0:
        m = "SM"

    for i in names:
        munis = data[i]["municipality"]
        if m == munis:
            if price(i) <= b:
                for kn in data[i]["kitchen"]:
                    if kn.upper().count(k.upper()) > 0:
                        if "si".upper().count(c.upper()) > 0:
                            for cart in data[i]["menu"]:
                                print(f" {i} : {cart} {data[i]['menu'][cart]}")


def median_bar(muni: str, types: str, dish: str, intdish: str):
    lista = []
    for i in names:
        if data[i]["municipality"] == muni:
            menu = data[i]["menu"]
            for m in menu:
                if m == types:  
                    dr = menu[types]
                    for d in dr:
                        if d.upper().count(dish.upper()) > 0:
                            beer = dr[d]
                            for i in beer:
                                if i == intdish:
                                    lista.extend(dict_num_values(beer))
                                    if type(beer) == int or type(beer) == float:
                                        lista.append(beer)
                                    else:
                                        lista.extend(dict_num_values(beer))
                                else:
                                    continue
                        else:
                            continue
                else:
                    continue
        else:
            continue
    return np.median(lista)

median_bar("DO","bar", "cocktails", "mojito")
mojito = []
cuba_libre = []
daiquiri = []

for b in x:
    mojito.append(median_bar(b,"bar", "cocktails", "mojito"))
    cuba_libre.append(median_bar(b,"bar", "cocktails", "cuba libre"))
    daiquiri.append(median_bar(b,"bar", "cocktails", "daiquiri"))

def barra_bar(x, coctails):
    num_barras = 3  
    ancho = 0.8 / num_barras
    y = np.arange(len(x))  

    plt.figure(figsize=(16, 10))  
    for i in range(num_barras):
        plt.bar(y + i * ancho - (ancho * (num_barras - 1)) / 2, 
                coctails[i], width=ancho, 
                label=["MOJITO", "CUBA LIBRE", "DAIQUIRI"][i])
    plt.xlabel('Municipios')
    plt.ylabel('Precios')
    plt.title("COMPARACIÓN DE LOS PRECIOS DEL MOJITO, CUBA LIBRE Y DAIQUIRI")
    plt.xticks(y, x) 
    plt.legend()
    plt.show()  

x = ['AN', 'BY', 'CH', 'CR', 'CT', 'DO', 'GB', 'HE', 'HV', 'LL', 'MR', 'PY', 'PR', 'RG', 'SM']

coctails = [mojito, cuba_libre, daiquiri]

def bar():
    return barra_bar(x, coctails)

def percent():
    no_cobran = 0
    cinco_percent = 0
    diez_percent = 0
    for p in names:
        charge_for_service = data[p]["there_is_an_additional_charge_for_service"]
        if charge_for_service == True:
            percent_collected = data[p]["percent_collected"]
            if percent_collected == 5:
                cinco_percent += 1
            if percent_collected == 10:
                diez_percent += 1
            else:
                continue
        else:
            no_cobran += 1
    total = [no_cobran, cinco_percent, diez_percent]
    plt.pie(total, labels= ["no cobran por servicio", "cobran cinco por ciento por servicio", "cobran diez por ciento por servicio"], autopct="%0.1f %%")
    plt.title("COMPARACIÓN DEL POR CIENTO ENTRE LOS RESTAURANTES QUE COBRAN Y NO POR SERVICIO")
    plt.show()

camaron = []
cangrejo = []
calamar = []
pulpo = []
langosta = []
other_mariscos = []

for a in x:
    camaron.append(especific_dish_median(a,"main_dishes", "camaron"))
    cangrejo.append(especific_dish_median(a,"main_dishes", "cangrejo"))
    calamar.append(especific_dish_median(a,"main_dishes", "calamar"))
    pulpo.append(especific_dish_median(a,"main_dishes", "pulpo"))
    langosta.append(especific_dish_median(a,"main_dishes", "langosta"))
    other_mariscos.append(median_mariscos(a))


def graph_mariscos(categorias, valores, name):
    num_barras = len(valores)
    ancho = 1.0 / num_barras 
    x = np.arange(len(categorias))
    plt.figure(figsize=(16, 10))
    for i in range(num_barras):
        plt.bar(x + i * ancho - (ancho * (num_barras - 1)) / 2, valores[i], width=ancho, label=name[i])
    plt.xlabel('Municipios')
    plt.ylabel('Precios')
    plt.title('Gráfica con la comparación de los precios de los mariscos por municipio')
    plt.xticks(x, categorias)
    plt.legend()
    plt.show()


list_mariscos = [camaron, cangrejo, calamar, pulpo, langosta, other_mariscos] 
name_mariscos = ['Camarón', 'Cangrejo', 'Calamar', 'Pulpo', 'Langosta', 'Otros Platos Con Mariscos']

def mariscos():
    return graph_mariscos(x, list_mariscos, name_mariscos)

def go_to():
    positive = 0
    negative = 0
    for x in names:
        if "containers" in data[x]["menu"] or "to go" in data[x]["menu"]:
            positive += 1
        else:
            negative += 1
    count = [positive, negative]
    name = ["ofertan alimentos para llevar","no ofertan alimentos para llevar" ]
    plt.pie(count, labels= name, autopct="%0.1f %%")
    plt.title("Parte de los restaurantes que ofertan alimentos para llevar")
    plt.show()


def social_network():
    total = len(names)
    negative = 0
    for i in names:
        if pd.isna(data[i]["social_network"]):
            negative += 1
    with_network = total - negative
    return with_network, negative

def with_phone():
    total = len(names)
    negative = 0
    for i in names:
        if pd.isna(data[i]["phone_number"]):
            negative += 1
    with_network = total - negative
    return with_network, negative

def comunications():
    sn_with, sn_without = social_network()
    ph_with, ph_without = with_phone()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.pie([sn_with, sn_without], labels=["Con redes sociales", "Sin redes sociales"], autopct="%0.1f %%", colors=['#66b3ff', '#ff9999'])
    ax1.set_title("Porción de los restaurantes que poseen redes sociales")
    ax2.pie([ph_with, ph_without], labels=["Con teléfono", "Sin teléfono"], autopct="%0.1f %%", colors=['#8fd9b6', '#ffcc99'])
    ax2.set_title("Porción de los restaurantes que poseen teléfono")
    plt.tight_layout()
    plt.show()


def remove_duplicados(l: list):
    newlist = []
    for i in l:
        if i not in newlist:
            newlist.append(i)
    return newlist


def lista(dish:str):
    list_restaurant = []
    for i in names:
            menu = data[i]["menu"]
            for m in menu:
                if m == "appetizers":
                    dr = dict_keys(menu["appetizers"])
                    for d in dr:
                        if d.upper().count(dish.upper()) > 0:
                           list_restaurant.append(i)
                        else:
                            continue
                if m =="main_dishes":
                    dr = dict_keys(menu["main_dishes"])
                    for d in dr:
                        if d.upper().count(dish.upper()) > 0:
                           list_restaurant.append(i)
                        else:
                            continue
                if m == "aggregation":
                    dr = dict_keys(menu["aggregation"])
                    for d in dr:
                        if d.upper().count(dish.upper()) > 0:
                           list_restaurant.append(i)
                        else:
                            continue
                if m == "pizzas":
                    dr = dict_keys(menu["pizzas"])
                    for d in dr:
                        if d.upper().count(dish.upper()) > 0:
                           list_restaurant.append(i)
                        else:
                            continue
                if m == "pastes":
                    dr = dict_keys(menu["pastes"])
                    for d in dr:
                        if d.upper().count(dish.upper()) > 0:
                           list_restaurant.append(i)
                        else:
                            continue
                else:
                    continue
    return remove_duplicados(list_restaurant)


def median_general(lugar: str, dish: str):
    lista = []
    if "appetizers" in data[lugar]["menu"]:
        for a in data[lugar]["menu"]["appetizers"]:
            if a.upper().count(dish.upper()) > 0:
                dishes = data[lugar]["menu"]["appetizers"][a]
                if type(dishes) == int or type(dishes) == float:
                    lista.append(dishes)
                if type(dishes) == dict:
                   lista.extend(dict_num_values(dishes))
            else:
                continue
    if "main_dishes" in data[lugar]["menu"]:
        for b in data[lugar]["menu"]["main_dishes"]:
            if b.upper().count(dish.upper()) > 0:
                dishes = data[lugar]["menu"]["main_dishes" ][b]
                if type(dishes) == int or type(dishes) == float:
                    lista.append(dishes)
                if type(dishes) == dict:
                   lista.extend(dict_num_values(dishes))
            else:
                continue
    if "pastes" in data[lugar]["menu"]:
        for c in data[lugar]["menu"]["pastes"]:
            if c.upper().count(dish.upper()) > 0:
                dishes = data[lugar]["menu"]["pastes"][c]
                if type(dishes) == int or type(dishes) == float:
                    lista.append(dishes)
                if type(dishes) == dict:
                   lista.extend(dict_num_values(dishes))
            else:
                continue
    if "pizzas" in data[lugar]["menu"]:
        for d in data[lugar]["menu"]["pizzas"]:
            if d.upper().count(dish.upper()) > 0:
                dishes = data[lugar]["menu"]["pizzas"][d]
                if type(dishes) == int or type(dishes) == float:
                    lista.append(dishes)
                if type(dishes) == dict:
                   lista.extend(dict_num_values(dishes))
            else:
                continue
    if "aggregation" in data[lugar]["menu"]:
        for e in data[lugar]["menu"]["aggregation"]:
            if e.upper().count(dish.upper()) > 0:
                dishes = data[lugar]["menu"]["aggregation"][e]
                if type(dishes) == int or type(dishes) == float:
                    lista.append(dishes)
                if type(dishes) == dict:
                   lista.extend(dict_num_values(dishes))
            else:
                continue
    return (lugar, (float(np.median(lista))))

def list_mar(dish: str, l: list, price: list):
    list_dish = [median_general(a, dish) for a in lista(dish)]
    for i in range(len(list_dish)):
        l.append(list_dish[i][0])
        if pd.isna(list_dish[i][1]):
            price.append(0.0)
        else:
            price.append(list_dish[i][1])
    return

list_calamares = []
calamares = []

list_mar("calamar", list_calamares, calamares)

calamar = {
    "restaurate": list_calamares,
    "precio media de los calamares": calamares
}
df_calamares = pd.DataFrame(calamar)
pd.set_option('display.max_rows', None)
df_calamares


def camarones():
    list_camarones = []
    camarones = []
    list_mar("camarones",list_camarones,camarones)
    df_camarones = pd.DataFrame({
    "Restaurante Con los Camarones": list_camarones,
    "Precio Media De Los Camarones": camarones
    })
    df_camarones_ordenado = df_camarones.sort_values(by="Precio Media De Los Camarones", ignore_index=True)
    first_ten_camarones = df_camarones_ordenado.head(10)
    df_camarones_ordenado_end = df_camarones.sort_values(by="Precio Media De Los Camarones", ignore_index=True,ascending=False)
    end_ten_camarones = df_camarones_ordenado_end.head(10)
    print("Restaurantes Con Los Camarones Más Caros :")
    print(end_ten_camarones)
    
    print("Restaurantes Con Los Camarones Más Baratos :")
    return  first_ten_camarones


def ice_cream():
    restaurantes = []
    price_ice_cream = []
    municipality = []
    for i in names:
        if "helados" in data[i]["kitchen"]:
            restaurantes.append(i)
            price_ice_cream.append(np.median(dict_num_values(data[i]["menu"]["desserts"])))
            municipality.append(data[i]["municipality"])
    df_ice_creams = pd.DataFrame({
        "Restaurante": restaurantes,
        "Presupuesto": price_ice_cream,
        "Municipio": municipality
    })
    df_ordenado = df_ice_creams.sort_values(by="Presupuesto", ignore_index=True)
    return df_ordenado



def bar_hv():
    total = 0
    for m in names:
        if data[m]["municipality"] == "HV":
            total += 1
    count = 0
    for i in names:
        if data[i]["municipality"] == "HV" and "bar" in data[i]["menu"]:
            count += 1
    percent_bar = count / total * 100
    return f"El {percent_bar} % de los restaurantes de la Habana Vieja cuentan con servicio de bar"

def list_hv():
    hv = []
    for i in names:
        if data[i]["municipality"] == "HV":
            hv.append(i)
    return hv

def df_hv():
    prices_hv = []
    for i in list_hv():
        prices_hv.append(price(i))
    df = pd.DataFrame({
        "Restaurante": list_hv(),
        "Presupuesto Requerido Por Persona": prices_hv 
    })
    return df.sort_values(by= "Presupuesto Requerido Por Persona", ignore_index= True)
          
def graph_bar_hv():
    l_bar = []
    bar_median = []
    for i in list_hv():
        if "bar" in data[i]["menu"]:
            l_bar.append(i)
            bar_median.append(np.median(dict_num_values(data[i]["menu"]["bar"])))
    x = l_bar
    y = bar_median
    plt.figure(figsize=(16, 10))
    plt.barh(x, y, color= "red")
    plt.title("Precio Medio De Las Bebidas En Los Bares De Los Restaurantes De Habana Vieja")
    plt.ylabel("Restaurantes")
    plt.xlabel("Precios")
    plt.show()

def list_anidada(l: list):
    new_list = []
    for i in l:
        if type(i) != list:
            new_list.append(i)
        else:
            new_list.extend(list_anidada(i))
    return new_list

def type_dish_muni(l: list, code_muni: str, s: list, v: list):
    median_for_dish = []
    ldishes = []
    for i in l:
        ldishes.append(dict_keys(data[i]["menu"]))
    types = remove_duplicados(list_anidada(ldishes))
    ln = len(types)
    type_dishes = types[0:ln-4]
    for d in type_dishes:
        median_for_dish.append(media(code_muni, d))
    v.extend(median_for_dish)
    s.extend(type_dishes)

def graph_dish_hv():
    dish_hv = []
    median_hv = []
    x = dish_hv
    y = median_hv
    type_dish_muni(list_hv(),"HV", dish_hv, median_hv)
    plt.figure(figsize=(16, 10))
    plt.bar(x,y, color= ["b","g","r", "c", "m","y","b","g","r", "c", "m","y", "b", "r" ,"g"])
    plt.title("Comparación del precio de los diferentes tipos de plato en La Habana vieja")
    plt.xlabel("Tipos de Platos")
    plt.ylabel("Precios")
    plt.show()

def graph_drinks_hv():
    l_drinks = []
    drinks_median = []
    for i in list_hv():
        if "drinks" in data[i]["menu"]:
            l_drinks.append(i)
            drinks_median.append(np.median(dict_num_values(data[i]["menu"]["drinks"])))
    x = l_drinks
    y = drinks_median
    plt.figure(figsize=(16, 10))
    plt.barh(x, y, color= "orange")
    plt.title("Precio Medio De Las Bebidas En Los Restaurantes De Habana Vieja")
    plt.ylabel("Restaurantes")
    plt.xlabel("Precios")
    plt.show()

def count_drinks():
    total = len(list_hv())
    count = 0
    for i in names:
        if data[i]["municipality"] == "HV" and "drinks" in data[i]["menu"]:
            count += 1
    percent_bar = count / total * 100
    return f"El {percent_bar} % de los restaurantes de Habana Vieja venden bebidas alcohólicas y no alcohólicas" 

list_do = []
def df_do():
    prices_do = []
    for o in names:
        if data[o]["municipality"] == "DO":
            prices_do.append(price(o))
            list_do.append(o)
    df = pd.DataFrame({
        "Restaurante": list_do,
        "Presupuesto Requerido Por Persona": prices_do
    })
    return df.sort_values(by="Presupuesto Requerido Por Persona", ignore_index=True)

def pizzas_do():
    count = 0
    pizzas = []
    prices_pizzas = [] 
    for i in names:
        if data[i]["municipality"] == "DO" and "pizzas" in data[i]["menu"]:
            count += 1
            pizzas.append(i)
            prices_pizzas.append(np.median(dict_num_values(data[i]["menu"]["pizzas"])))
    x = pizzas
    y = prices_pizzas
    print(f"El {(count / len(list_do)) *100} % de los restaurantes de Diez de Octure venden pizzas.")
    plt.figure(figsize=(16, 10))
    plt.barh(x, y, color= "yellow")
    plt.title("Precio Medio De Las Pizzas En El Municipio Diez De Octubre")
    plt.ylabel("Restaurantes")
    plt.xlabel("Precios")
    return plt.show()

def graph_dish_do():
    dish_do = []
    median_do = []
    x = dish_do
    y = median_do
    type_dish_muni(list_do,"DO", dish_do, median_do)
    plt.figure(figsize=(16, 10))
    plt.bar(x,y, color= ["b","g","r", "c", "m","y","b","g","r", "c", "m","y", "b", "r" ,"g"])
    plt.title("Comparación del precio de los diferentes tipos de plato en Diez de Octubre")
    plt.xlabel("Tipos de Platos")
    plt.ylabel("Precios")
    plt.show()

def df2_ice_cream():
    repeat = []
    median_ic = []
    for i in names:
        postres = data[i]["menu"]
        if "desserts" in postres:
            for o in postres["desserts"]:
                if o.upper().count("helad".upper()) > 0:
                    repeat.append(i)
                    helados = data[i]["menu"]["desserts"][o]
                    if type(helados) == float or type(helados) == int:
                        median_ic.append(helados)
                    else:
                        median_ic.append(dict_num_values(helados))
                else: continue
        else:
            continue
    place = remove_duplicados(repeat)
    print(f"A pesar de la baja cifra {(len(place) / len(names)) * 100} % de los restaurantes de La Habana tiene al menos tipo de helado en su menú, ya que es unos de los postres más consumidos por los cubanos")
    


















