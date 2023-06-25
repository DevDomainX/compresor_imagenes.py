#!/usr/bin/env python3
#Author: Hans Saldias


from PIL import Image
import os
print("Script para comprimir peso de imagenes \nejecuta el script donde tengas todas las imagenes para comprimirlas script craedo por Hans Saldias\n")
op = input("Aceptas comprimir las imagenes (si/no): ")
print("\n")
if op == "si":
    if not os.path.exists('imagenes_comprimidas'):
        os.mkdir('imagenes_comprimidas')

        for imagen in os.listdir('.'):
            if imagen.endswith('.jpg') or imagen.endswith('.png') or imagen.endswith('.jpeg') or imagen.endswth('.JPG') or imagen.endswith('.PNG'):

                nombre = os.path.splitext(imagen)[0]

                img = Image.open(imagen)

                img.save(f'imagenes_comprimidas/{nombre}.jpg', optimize=True, quality=50)
                print("#" * 60)
                print("todas las imagenes han sido gurdadas\nexitosamente!!\n En la carpeta imagenes comprimidas")

print("Creador: Hans Saldias")
