from PIL import Image
import matplotlib.pyplot as plt
img = Image.open("C:/Users/47/Desktop/LIM2second_semestre/traitement_iamge/TP/src/leo.jpg")
img=img.rotate(angle=50,expand=True,fillcolor="green")
img.show()
