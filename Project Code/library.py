
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium

p = "menu.json"
data = pd.read_json(p)

with open("municipality.json") as m:
    muni = json.load(m)

place= []
for pl in data:
    place.append(pl)

def list_resturant():
   places = {
    "Restaurantes": place
   }
   df = pd.DataFrame(places)
   pd.set_option('display.max_rows', None)
   return df

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

for i in place:
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

def dict_num_values(l : dict):
   lista = []
   for i in l.values():
      if isinstance(i,dict):
         lista.extend(dict_num_values(i))
      else:
         lista.append(i)
   return(lista)

def media(x: str,y: str):
   for a in data:
      cart = data[a]["municipality"]
      if cart == x: 
         m = data[a]["menu"]
         for b in m:
            if b == y:
               n = data[a]["menu"][y]
               lists = dict_num_values(n)
   median = np.median(lists)
   return median

x = ['AN', 'BY', 'CH', 'CR', 'CT', 'DO', 'GB', 'HE', 'HV','LL','MR','PY','PR','RG','SM']

def pyplot_bar(y: list, title: str):
    colors = ["r", "r", "g", "r", "r", "r", "r", "r", "g", "r", "r", "g", "g", "r", "r"]
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color=colors)
    plt.xlabel("MUNICIPIOS")
    plt.ylabel("CANTIDAD")
    plt.title(title)
    plt.show()

names = []
for n in data:
    names.append(n)

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

def price_int(index: int):
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
    agg = "aggregations"
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
        if names.index(i) == index:
            menu = data[i]["menu"]
            for r in menu:
                if r == bkf:
                    values =  menu[r].values()
                    for bk in values:
                        if type(bk) == int or type(bk) == float:
                            lbkf.append(bk)
                        else:
                           lbkf.extend(price_int(bk))
                if r == ent:
                    values =  menu[r].values()
                    for en in values:
                        if type(en) == int or type(en) == float:
                            lent.append(en)
                        else:
                            lent.extend(price_int(en))
                if r == plp:
                    values =  menu[r].values()
                    for pl in values:
                        if type(pl) == int or type(pl) == float:
                            lplp.append(pl)
                        else:
                            lplp.extend(price_int(pl))
                if r == ftt:
                    values =  menu[r].values()
                    for ft in values:
                        if type(ft) == int or type(ft) == float:
                            lftt.append(ft)
                        else:
                            lftt.extend(price_int(ft))
                if r == pzz:
                    values =  menu[r].values()
                    for pz in values:
                        if type(pz) == int or type(pz) == float:
                            lpzz.append(pz)
                        else:
                            lpzz.extend(price_int(pz))
                if r == agg:
                    values =  menu[r].values()
                    for ag in values:
                        if type(ag) == int or type(ag) == float:
                            lagg.append(ag)
                        else:
                            lagg.extend(price_int(ag))
                if r == crm:
                    values =  menu[r].values()
                    for cr in values:
                        if type(cr) == int or type(cr) == float:
                            lcrm.append(cr)
                        else:
                            lcrm.extend(price_int(cr))
                if r == pst:
                    values =  menu[r].values()
                    for pst in values:
                        if type(pst) == int or type(pst) == float:
                            lpst.append(pst)
                        else:
                            lpst.extend(price_int(pst))
                if r == sps:
                    values =  menu[r].values()
                    for sp in values:
                        if type(sp) == int or type(sp) == float:
                            lsps.append(sp)
                        else:
                            lsps.extend(price_int(sp))
                if r == brd:
                    values =  menu[r].values()
                    for br in values:
                        if type(br) == int or type(br) == float:
                            lbrd.append(br)
                        else:
                            lbrd.extend(price_int(br))
                if r == dsr:
                    values =  menu[r].values()
                    for ds in values:
                        if type(ds) == int or type(ds) == float:
                            ldsr.append(ds)
                        else:
                            ldsr.extend(price_int(ds))
                if r == drk:
                    values =  menu[r].values()
                    for dk in values:
                        if type(dk) == int or type(dk) == float:
                            ldrk.append(dk)
                        else:
                            ldrk.extend(price_int(dk))
                if r == bar:
                    values =  menu[r].values()
                    for b in values:
                        if type(b) == int or type(b) == float:
                            lbar.append(b)
                        else:
                            lbar.extend(price_int(b))
                if r == ctn:
                    values =  menu[r].values()
                    for ct in values:
                        if type(ct) == int or type(ct) == float:
                            lctn.append(ct)
                        else:
                            lctn.extend(price_int(ct))
                if r == inf:
                    values =  menu[r].values()
                    for nf in values:
                        if type(nf) == int or type(nf) == float:
                            linf.append(nf)
                        else:
                            linf.extend(price_int(nf))
                else:
                    continue
        else:
            continue    
    dishes = [lbkf, lent, lplp, lftt, lpzz, lagg, lcrm, lpst, lsps, lbrd, ldsr, ldrk, lbar, lctn, linf]
    median = []
    for r in dishes:
        median.append(np.nanmedian(r))
    return median

def price(index: int):
    budget = np.nansum(price_int(index))
    return int(budget)

# Salary

salaries = muni["LH"]["salario_medio_en_2023"] 
salary = []

for s in names:
    index = names.index(s)
    bt = price(index)
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

ml = []
for  i in ub.values:
    ml.append(i)

def map():
    map = folium.Map(location=[23.1057291,-82.3581364], zoom_start=10)
    for i, mp in ub.iterrows():
        folium.Marker(location=[mp.latitud, mp.longitud], popup=f"{mp['name']} , gasto mínimo(todos los tipos de platos): {mp['budget']}, teléfono : {mp['phone']}" ).add_to(map)
    return map