import numpy as np
import matplotlib.pyplot as plt
image=np.array([
[[255,0,0], [0,255,0]],
[  [0,0,255], [0,0,0]]])
plt.imshow(image)
plt.show()
def img2gray(img): 
    r,g,b = img[:,:,0],img[:,:,1 ],img[:,:,2]
    gray =0.299*r +0.5578*g + 0.114*b
    return gray
gray_image=img2gray(image)  
plt.imshow(gray_image,cmap="gray")
plt.show()