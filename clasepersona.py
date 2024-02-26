class estudiante:
    def __init__(self,nombre,apellido,cedulaint, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedulaint= cedulaint
        self.correo= correo
        self.telefono= telefono
    def obtenernombre(self):
        return f'mi nombre es {self.nombre} {self.apellido}'
    def obtenercedula(self):
        return f'mi cedula es {self.cedulaint}' 
    def obtenercorreo(self):
        return f'mi correo es {self.correo}'
    def obtenertelefono(self):
        return f'mi correo es {self.telefono}'

p=estudiante("fabian andres","perez melendez", "1041976100", "fabianandres.perezmelendez@unitecnar.edu.co" , "3014469610")

print("mi nombre es", p.obtenernombre(), "mi cedula es", p.obtenercedula(), "mi correo es" , p.obtenercorreo() , "y mi numero de telefono es", p.obtenertelefono())