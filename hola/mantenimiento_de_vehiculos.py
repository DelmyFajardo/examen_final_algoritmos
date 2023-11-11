import openpyxl
libro = openpyxl.load_workbook('vehiculos.xlsx')
hoja = libro ["listado"]


hoja ['A1'].value = "Codigo"
hoja ['B1'].value = "Marca"
hoja ['C1'].value = "Modelo"
hoja ['D1'].value = "Precio"
hoja ['E1'].value = "Kilometraje"
hoja ['F1'].value = "CantidadeFotos"

datos=[
   {
      "Codigo":"CITY01",
      "Marca":"HONDA",
      "Modelo":"2020",
      "Precio":"80000",
      "Kilometraje":"600",
      "CantidadFotos":"0"
   },
   {
      "Codigo":"CIVIC01",
      "Marca":"HONDA",
      "Modelo":"2021",
      "Precio":"90000",
      "Kilometraje":"0",
      "CantidadFotos":"0"
   },
   {
      "Codigo":"PILOT01",
      "Marca":"HONDA",
      "Modelo":"2021",
      "Precio":"40000",
      "Kilometraje":"1300",
      "CantidadFotos":"0"
   },
   {
      "Codigo":"BT50",
      "Marca":"MAZDA",
      "Modelo":"2021",
      "Precio":"50000",
      "Kilometraje":"600",
      "CantidadFotos":"0"
   },
   {
      "Codigo":"BALENO1",
      "Marca":"SUZUKI",
      "Modelo":"2021",
      "Precio":"60000",
      "Kilometraje":"2000",
      "CantidadFotos":"0"
   },
   {
      "Codigo":"XL71",
      "Marca":"SUZUKI",
      "Modelo":"2021",
      "Precio":"70000",
      "Kilometraje":"1500",
      "CantidadFotos":"0"
   }
]


proxima_fila = hoja.max_row + 1 
for registro in datos:
    hoja [f"A{proxima_fila}"].value = registro ["Codigo"]
    hoja [f"B{proxima_fila}"].value = registro ["Marca"]
    hoja [f"C{proxima_fila}"].value = registro ["Modelo"]
    hoja [f"D{proxima_fila}"].value = registro ["Precio"]
    hoja [f"F{proxima_fila}"].value = registro ["Kilometraje"]
    hoja [f"G{proxima_fila}"].value = registro ["CantidadFotos"]
    proxima_fila +=1


def crear_vehiculos():
  
   pass
def editar_vehiculo():
   pass

def eliminar_vehiculo():
   pass
def listar_vehiculos():
   pass
   

while opcion :
    opcion=input ("elige una opcion")
    print("1. crear registro")
    print("2. editar registro")
    print("3. eliminar  registro")
    print("4. listar  registro")

if opcion == 1 :
 crear_vehiculos()
if opcion == 2 :
 editar_vehiculo()
if opcion == 3 :
 eliminar_vehiculo()
if opcion == 4:
   listar_vehiculos() 


libro.save("vehiculos.xlsx")