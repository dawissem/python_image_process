from PIL import Image
import matplotlib.pyplot as plt
# creer un objet image object
file_path= r"C:/Users/47/Desktop/LIM2second_semestre/traitement_iamge/TP/src/"
fichier=input("le nom du fichier: ")
fichier = file_path +fichier 
image = Image.open(fichier)
L, H = image.size
print("largeur = ", L,"hauteur = ",H)
image.show()
  