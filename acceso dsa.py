edad =int(input("ingresa tu edad"))
poseer_aut=input("usted posee algun rol de autoridad?(sup=supervisor,aut=tener autorizacion,not=no tener rol de autoridad.)")

if edad >= 18 and poseer_aut =="SUPER" or "AUTR":
    print("felicidades, cuentas con los 2 requisitos para acceder a la zona restringida")
if edad < 18 and poseer_aut == "sup" or "aut":
        print("usted no cuenta con la edad suficiente para acceder a la zona restringida :C ")