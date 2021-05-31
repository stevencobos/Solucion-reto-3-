from datetime import datetime
import random

def cdia_humita():
  """ 
  Returns
  -------
  humita:str
  Lista de Humitas aleatoriamente     
  """
  cdia=["aer*+aq@ta","aqp*xap@ka","adv*qa+@ga","avo*uaq@ca","aex*qay@va","asw*oap@ja","aru*uap@da","auy*vay@ca","aco*uan@ha","anm*+at@ta","atp*+an@wa","apy*+an@ya","a@l*+ax@ba","a@o*+ay@ua","a@w*tax@ka","a@p*naq@aa","a@q*nau@ka","a@v*xaq@ra","aft*yaoqia","ayt*xausja","abp*qavqpa","adw*&a@oha","alwrqarxfa","aunnxatola","aumro@t@sa","a*upp@w@ca","a*o*q@w@ka","a*o*p@r@oa","a*m*q@y@aa","aau*t@n@xa","afv*xav@na","aw@*+asoca","af@*+aotja","aq@*+auvda","ar@*+axvca","am@*+aosta","ap@*+apyaa","af@*+aqpsa","aq@*+apnea","a@w*+aq@ea","a@s*+at@ba","c@v*+ax@ba","a@o*+ax@sa","c@r*+as@ma","c@n*+aw@ia","crw*+aoxma","ciy*+atsqp","col*aatusu","csv*aapsxv","ctv*aaruxf","cavkaavqdi","apyka@y@pr","apswa@w@ux","auxxu@p@ha","ajokj@r@ja","agrwg@t@wa","apqmp@y@ga","agqogan@ga","ao@*oauypa","ak@*kaqrfa","ae@*eauoma","at@*tayvfa","ab@*bawwea"]
  indice = random.randint(0, 62)
  return cdia[indice]

def lista_profesion():
  profesion=["salud_1","salud_2","basica","secundaria","ninguno"]
  if "@" in cdia_humita():
    indice = random.randint(0, 1)
  elif "+" in cdia_humita():
    indice = random.randint(2, 3)
  else:
    indice = random.randint(3, 4)
  print(f"CDIA:      {cdia_humita()}")
  print(f"PROFESION: {profesion[indice]}")
  return



def proc_control(cd1):
  v1 = len(cd1)==10 and cd1.count("A")==3
  v2 = type(cd1)==type("str") and cd1[0]== cd1 [9]
  v3 = "+" in cd1 or "=" in cd1 or "&" in cd1
  v4 = cd1[2]=="*" and "@" in cd1
 
  if v1==True and v2==True and v3==True and v4==True:
    validacion=True
  else:
    validacion=False

  return validacion


def formulario():
  formulario_dig = input('Humascciano, desea realizar el cuestionario CrownV: (SI/NO) ')
  formulario_new = formulario_dig.upper()
  if formulario_new == 'SI' or formulario_new == 'S':
    print("================CUESTIONARIO PREVENTIVO CONTRA  CROWNV============")
    Retorno = input('Retorno al país las últimas dos semanas (Si, No)')
    Retorno_new=Retorno.upper()
    if Retorno_new == 'SI' or Retorno_new=='S':
      pais= input('¿Si su respuesta es SÍ por favor indique de qué país llegó?')
    else:
      print('')
    contacto=input("Ha tenido contacto a < 2 metros\n con una persona a la que se le haya diagnosticado Covid-19 SI/NO: ")
    Fecha_nac=input('Fecha de Nacimiento (en formato DD/MM/AAAA)')
    fiebre=input("Ha presentado fiebre hace < 2 semanas SI/NO: ")
    tos=input("Ha presentado tos hace < 2 semanas SI/NO: ")
    sabores=input("Ha presentado hace < 2 semanas capacidad para percibir sabores SI/NO: ")
    validacion_formulario(pais,contacto,Fecha_nac,fiebre,tos,sabores)
  else:
    print("Es necesario realizar el cuestionario contra el CrownV")
  return

def calcular_edad(c_edad_Humascciano):
  fecha = datetime.strptime(c_edad_Humascciano, "%d/%m/%Y")
  hoy = datetime.now()
  diferencia = hoy - fecha
  años=diferencia.days / 365
  
  return años

def validacion_formulario(pais1,cont,fecha,fieb,ts,sb):
  edad=int(f"{calcular_edad(fecha):.0f}")
  contador=cont,fieb,ts,sb
  print("===================RESULTADO DE SU PRUEBA DE CROWNV=================")
  print("")
  if edad<=50 and contador.count('S')==2 or contador.count('s')==2:
    resp=contador.count('S') or contador.count('s')
    print(f"Como Usted viene de {pais1} con una edad de {edad} años y ha dado {resp} respuestas positivas, se le ha clasificado como posible caso de PYAN_V19 y debe ser enviado a cuarentena")

  elif edad>=50 and contador.count("S")==1 or contador.count('s')==2:
    resp=contador.count("S") or contador.count('s')
    print(f"Como Usted viene de {pais1} con una edad de {edad} años y ha dado {resp} respuestas positivas, se le ha clasificado como posible caso de PYAN_V19 y debe ser enviado a cuarentena")  
  else:
    print("Humascciano usted tiene que permanecer en cuarentena")
  return
