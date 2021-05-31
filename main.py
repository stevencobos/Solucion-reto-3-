import  min_salud_ancon  as  asc

def leer_cdia():
  print("==========DIAGNOSTICO PREVENTIVO CONTRA CROWNV========")
  print("INFORMACION DEL SOLICITANTE HUMITA: ")
  asc.lista_profesion()
  print("××××××××××××××××××××××××××××××××××××××××××××××××××××××××××")
  cod_cdia=str(input("Humascciano por favor ingrese su codigo CDIA\n (codigode identificacion ASCCI): "))
  print("")
  print("***************************************************")
  codigo_cdia = cod_cdia.upper()
  print("Su codigo CDIA se ha actualizado...")
  print(f"Su nuevo codigo CDIA Humascciano es: {codigo_cdia}")
  print("***************************************************")
  validacion=asc.proc_control(codigo_cdia)

  if validacion==True:
    print("--------------------Bienvenido Humascciano-----------------")
    print("")
    print("Acontinuacion se le realizara un formulario preventivo contra el CrownV\n")
    asc.formulario()
  else:
    print("Usted no cuenta con un CDIA Humascciano")




leer_cdia()