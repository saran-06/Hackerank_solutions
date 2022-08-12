#!/usr/bin/env python
# coding: utf-8

# In[131]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[132]:


img1=cv2.imread("C:\\Users\\Saranya\\Downloads\\login-background.jpg")


# In[133]:


plt.imshow(img1)


# In[134]:


#printing height and width of image
(height,width)=img1.shape[:2]
print("height={} width={}".format(height,width))


# In[135]:


#extracting the RGB value of colors
(B,G,R)=img1[100,100]
print("R = {}, G = {}, B = {}".format(R, G, B))


# In[136]:


#extracting the RGB value of colors for one color
B=img1[100,100,0]
print("blue:{}".format(B))


# In[137]:


#Extracting the Region Of Interest(ROI) in image
roi=img1[200:500,300:700]
plt.title("ROI image")
plt.imshow(roi)


# In[138]:


#Resizing the image
resize=cv2.resize(img1,(800,800))
plt.title("resized image")
plt.imshow(resize)


# In[139]:


#height and width of reshaped image
(h,w)=resize.shape[:2]
print((h,w))


# In[140]:


# # Calculating the ratio
# ratio = 800 / w
# # Creating a tuple containing width and height
# dim = (800, int(h * ratio))

# # Resizing the image
# aspect_ratio= cv2.resize(img1, dim)
# plt.imshow(aspect_ratio)
#To find a center of an image
center=h//2,w//2
print(center)


# In[141]:



matrix=cv2.getRotationMatrix2D(center,-90,1.0)
rotated=cv2.warpAffine(img1,matrix,(height,width))
plt.title("rotated image")
plt.imshow(rotated)


# In[160]:


#copy image
copied_img=img1.copy()


# In[161]:


#draw qa rectangle in image
rectangle=cv2.rectangle(copied_img,[1500,900],[600,400],(255,0,0),8)
plt.imshow(rectangle)


# In[162]:


text=cv2.putText(copied_img,"hi hello",(700,500),cv2.FONT_HERSHEY_TRIPLEX,4,(0,255,0),8)
plt.imshow(text)


# In[ ]:




