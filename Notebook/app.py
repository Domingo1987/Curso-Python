import os
import nbformat
import re


def listar_archivos(ruta_directorio):
    try:
        # Consigue una lista de archivos dentro de un directorio especificado
        directorios = os.listdir(ruta_directorio)
        
        # Filtra los archivos que no terminen en ".ipynb"
        directorios = [directorio for directorio in directorios if os.path.isfile(os.path.join(ruta_directorio, directorio)) and directorio.endswith('.ipynb')]
        
        return directorios
    except Exception as e:
        return str(e)
    
def contar_desafios(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
            content = nbformat.writes(notebook)
            # Usa una expresión regular para contar la palabra exacta "Desafío"
            return len(re.findall(r'\bDesafío\b', content))
    except Exception as e:
        return str(e)

def escribirArchivo(directorios, rutaOut, ruta_directorio):
    try:
        # Defino la variable totalDesafios
        totalDesafios = 0
        
        # Abre el archivo Markdown para escribirlo
        with open(rutaOut, mode='w', encoding='utf-8') as outfile:            
            # Escribe el header
            outfile.write('# Archivos\n')
           
            # Escribe los nombres de los archivos y sus desafíos
            for file in directorios:
                file_path = os.path.join(ruta_directorio, file)
                num_desafios = contar_desafios(file_path)
                totalDesafios += num_desafios
                
                # Escribe el nombre del archivo como encabezado y la cantidad de desafíos
                outfile.write(f'## [{file}]({file}) - {num_desafios} Desafíos\n')
            
            outfile.write(f'# El número Total de Desafíos es {totalDesafios}')
                
    except Exception as e:
        return str(e)

ruta_directorio = 'Notebook/'  # Reemplazarlo con la ruta donde estan los archivos ".ipynb"
rutaOut = 'Notebook/0_0_Resumen.md'  # Reemplazarlo con la ruta donde desea guardar el archivo markdown
directorios = listar_archivos(ruta_directorio)

print("Archivos Notebook encontrados:")
for directorio in directorios:
    print(directorio)

escribirArchivo(directorios, rutaOut, ruta_directorio)

print(f"Los archivos fueron guardados en: {rutaOut}")
