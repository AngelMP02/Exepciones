import re
class usuario:
  def __init__(self, correo):
    self.correo=correo
   
  def Email(self):
    
    email=input("Introduzca su email:")

    try:
      if email=="":
             raise Exception("Es una entrada incorrecta")
      elif re.search(". * @. * \ .. *", email) is None:
              raise Exception("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx ")
  
      else: 
          if email==self.correo:
                print("Bienvenido")
             
          else:
           raise Exception("Cuenta bloqueada a causa de un ataque")
    finally:
        return 