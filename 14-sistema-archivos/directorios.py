import os

#crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("ya existe")

#eliminar
#os.rmdir("./mi_carpeta")

#copiar
import shutil
#shutil.copyfile(src, dst)