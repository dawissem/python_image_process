#pip install Pillow
# Importing Image from PIL package
from PIL import Image
# creer un objet image object
chemin="C:\Users\47\Desktop\LIM2second_semestre\traitement_iamge\TP\src"
fichier=input("le nom du fichier: ")
fichier = chemin +fichier
image = Image.open(fichier)
L, H = image.size
print("largeur = ", L,"hauteur = ",H)
im.show()
cimag=im.copy()
newim=cimag.crop([0,10,183,150])
newim2=cimag.crop ([0, 150, 183, 275])
# newim3 - cimag.crop ([0,820,L,H])
#
newim.show()
newim2. show()