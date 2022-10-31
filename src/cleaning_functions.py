#!/usr/bin/env python
# coding: utf-8

# # Funciones utilizadas para la limpieza del archivo.

# In[1]:


get_ipython().run_line_magic('pip', 'install ipython')
get_ipython().run_line_magic('pip', 'install seaborn')

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re




# In[2]:


def limpiar_fecha(s):
    
    x = s.split('.')
    lista=[]
    
    for i in x:
        
        lista.append(i)
            
    return ('.'.join(lista[0:3]))


# In[3]:


def quitar_fechas(a):
    
    for i in a:
        
        if len(a)!=10:
            
            return 'unknown'
        
        if len(a)==10:
            
            return a


# In[4]:


def contar_fechas(c):
    
    lista=[]
    
    for i in c:
        
        if i[8:10]=='00':
            
            lista.append(i)
    
    return len(lista)


# In[5]:


def cambiar_year(a):
    
    for i in [a]:
        
        if i>0:
            
            return i
        
        if i==0:
            
            return 'unknown'


# In[6]:


def limpiar_country(country):
    
    country=re.findall('\w+', country)
    country=' '.join(country)
    
    return country


# In[7]:


def limpiar_activity(x):
    
    dicc_actividades = {"Fishing":re.search(".*[Ff](ishing|ISHING).*",str(x)),
                        "Swimming":re.search(".*[Ss](wimming|WIMMing).*",str(x)),
                        "Kite":re.search(".*[Kk](ite|ITE).*",str(x)),
                        "Walking":re.search(".*[Ww](alking|ALKING).*",str(x)),
                        "Boogie Board":re.search(".*[Bb](oogie|OOGIE).*",str(x)),
                        "Body Boarding":re.search(".*[Bb](ody|ODY).*",str(x)),
                        "Wind Surfing":re.search(".*[wW](ind|IND).*",str(x)),
                        "Boat":re.search(".*[Bb](oat|OAT).*",str(x)),
                        "Interact with sharks":re.search(".*[Ss](hark|HARK).*",str(x)),
                        "Diving":re.search(".*[Dd](iving|IVING).*",str(x)),
                        "Standing in water":re.search(".*[Ss](tand|TAND).*",str(x)),
                        "Paddling":re.search(".*[Pp](addl|ADDL).*",str(x)),
                        "Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),
                        "OverBoard":re.search(".*[Oo](verb|VERB).*",str(x)),
                        "Bathing":re.search(".*[Bb](athing|ATHING).*",str(x)),
                        "Floating":re.search(".*[Ff](loat|LOAT).*",str(x)),
                        "Jumping":re.search(".*[Jj](ump|UMP).*",str(x))}

    for key,values in dicc_actividades.items():        
        
        if values:            
            
            return key            
    
    return "other"


# In[8]:


def change_name(name):
    
        if re.search('^[A-Z].+',str(name)):
            
            return name
        
        else:
            
            return 'unknown'


# In[9]:


def unificar_sex(sex_):
    
    if sex_=='F':
        
        return 'F'
    
    if sex_=='M':
        
        return 'M'
    
    else:

        return 'unknown'


# In[10]:


from statistics import mean

def mean_age(x):
    
    x = x.lower()
    num=re.findall('\d+', x)[:5]
    res = [eval(i) for i in num]
    
    if num:
        return mean(res)
    elif 'teen' in x:
        return 15.5
    elif 'young' in x:
        return 18.5
    elif 'adult' in x:
        return 49
    elif 'elderly' in x:
        return 70
    elif 'middle' in x :
        return 50
    elif '18months' in x:
        return 1.5
    elif '9months' in x:
        return 0.75
    elif '2to3months' in x:
        return 0.2
    else:
        return 


# In[11]:


def unificar_fatal(f):
    
    if f=='N' or f==' N' or f=='N ':
        
        return 'N'
    
    if f=='Y' or f=='y':
        
        return 'Y'
    
    else:

        return 'N/A'


# In[12]:


def horas(x):
    
    
    if x:
        
        return x[0:3]


# In[13]:


def limpiar_time(x):
    
    if x=='07h' or x=='08h' or x=='09h' or x=='10h' or x=='11h' or x=='Mor' or x=='Day' or x=='AM' or x=='A.M' or x=='Daw':
        
        return 'Morning'
    
    if x=='12h' or x=='13h' or x=='14h' or x=='15h' or x=='16h' or x=='17h' or x=='18h' or x=='19h' or x=='Mid' or x=='Aft' or x=='PM' or x=='P.M' or x=='Lun' or x=='Sun' or x=='Noo':
        
        return 'Afrternoon'
    
    if x=='20h' or x=='21h' or x=='22h' or x=='Eve':
        
        return 'Evening'
        
    if x=='23h' or x=='00h' or x=='01h' or x=='02h' or x=='03h' or x=='04h' or x=='05h' or x=='06h' or x=='Nig' or x=='Dar' or x=='Dus' or x=='dus':
        
        return 'Nigth'
    
    else:
        
        return 'unknown'
        


# In[14]:


def limpiar_species(x):
    
    dicc_especies = {
            "White shark":re.search(".*[Ww](hite|HITE).*",str(x)),
            "Tiger shark":re.search(".*[Tt](iger|IGER).*",str(x)),
            "Lemon shark":re.search(".*[Ll](emon|EMON).*",str(x)),
            "Hammerhead shark":re.search(".*[Hh](ammerhead|AMMERHEAD).*",str(x)),
            "Bull shark":re.search(".*[Bb](ull|ULL).*",str(x)),
            "Blue shark":re.search(".*[Bb](lue|LUE).*",str(x)),
            "Silvertip shark":re.search(".*[Ss](ilvertip|ILVERTIP).*",str(x)),
            "Nurse shark":re.search(".*[Nn](urse|URSE).*",str(x)),
            "Whaler shark":re.search(".*[Ww](haler|HALER).*",str(x)),
            "Blacktip shark":re.search(".*[Bb](lacktip|LACKTIP).*",str(x)),
            "Mako shark":re.search(".*[MM](ako|AKO).*",str(x)),
            "Sand shark":re.search(".*[Ss](and|AMD).*",str(x)),
            "Wobbegong shark":re.search(".*[Ww](obbegong|OBBEGONG).*",str(x)),
            "Galapagos shark":re.search(".*[Gg](alapagos|ALAPAGOS).*",str(x)),
            "Grey shark":re.search(".*[Gg](rey|REY).*",str(x)),
            "Leopard shark":re.search(".*[Ll](eopard|EOPARD).*",str(x)),
            "Zambesi shark":re.search(".*[Zz](ambesi|AMBESI).*",str(x)),
            "Blacktail shark":re.search(".*[Bb](lacktail|LACKTAIL).*",str(x)),
            "Red shark":re.search(".*[Rr](ed|ED).*",str(x)),
            "Dusky shark":re.search(".*[Dd](usky|USKY).*",str(x)),
            "Raggedtooth shark":re.search(".*[Rr](aggedtooth|AGGEDTOOTH).*",str(x)),
            "Spinner shark":re.search(".*[Ss](pinner|PINNER).*",str(x)),
            "Cow shark":re.search(".*[Cc](ow|OW).*",str(x)),
            "Porbeagle shark":re.search(".*[Pp](orbeagle|ORBEAGLE).*",str(x)),
            "Caribbean reef shark":re.search(".*[Cc](aribbean|ARIBBEAN).*",str(x)),
            "Sandbar shark":re.search(".*[Ss](and|AND).*",str(x)),
            "Silky shark":re.search(".*[Ss](ilky|ILKY).*",str(x)),
            "Zambezi shark":re.search(".*[Zz](ambezi|AMBEZI).*",str(x)),
            "Sevengill shark":re.search(".*[Ss](evengill|EVENGILL).*",str(x)),
            "Copper shark":re.search(".*[Cc](opper|OPPER).*",str(x)),
            "Angel shark":re.search(".*[Aa](ngel|NGEL)\s",str(x)),
            "Salmon shark":re.search(".*[Ss](almon|ALMON).*",str(x)),
            "Goblin shark":re.search(".*[Gg](oblin|OBLIN).*",str(x)),
            "Thresher shark":re.search(".*[Tt](hresher|HRESHER).*",str(x)),
            "Dogfish shark":re.search(".*[Dd](ogfish|OGFISH).*",str(x)),
            "Involvement not confirmed":re.search("[^.?!]*involvement[^.?!]*",str(x))}
    
    for key,values in dicc_especies.items():
        
        if values:
            
            return key

    return "other_specie"


# In[15]:


def liampiar_web(x):
    
    if x[0:7]=='http://':
        
        return x
    else:
        
        return 'unknown'

