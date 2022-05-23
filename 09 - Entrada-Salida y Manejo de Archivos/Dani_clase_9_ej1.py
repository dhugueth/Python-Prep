import sys 

if len(sys.argv)==4:  #Se ponen 4 porque adicionalmente a los 3 que se deben de ingresar tenemos siempre en argv[0] el nombre del archivo
    print('El primer argumento ingresado es:', sys.argv[1])
    print('El segundo argumento ingresado es:', sys.argv[2])
    print('El tercer argumento ingresado es:', sys.argv[3])
else:
    print("ERROR: se ejecuto el programa con una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo de como ingresar los argumentos al ejecutar es: python clase09_ej1.py 1 2 3')
