
# coding: utf-8

# In[1]:

import time
import pylab
import cv2
from pylab import imshow
from SimpleCV import Camera
from matplotlib import pyplot
pyplot.set_cmap('gray')

#get_ipython().magic(u'matplotlib inline')


# In[10]:

def capture_single(monochrome=True, camera_port = 0):
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.05)  # If you don't wait, the image will be dark
    return_value, image = camera.read()
    if monochrome:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # convert to grayscale
    del(camera)
    return image


# In[21]:

## p = capture_single()
## imshow(p)


# In[19]:

def timelapse(frames, dt, fileprefix, ftype = '.jpg', camera_port = 0):
    '''give dt time in seconds'''
    dt = float(dt)
    for i in range(0,frames):
        image = capture_single(True, camera_port)
        cv2.imwrite(fileprefix+'_'+str(i).zfill(2)+str(ftype), image)
        time.sleep(dt)
    file = open(fileprefix+'_metadata.txt','w')  
    file.write('Number of frames: ' + str(frames)+'\n') 
    file.write('Seconds between frames: ' + str(dt))  
    file.close() 
        


# In[20]:

## timelapse(5,2,'photobooth-on')


# In[ ]:



