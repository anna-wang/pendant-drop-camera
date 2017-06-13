import capture_time_series
from capture_time_series import *

fnames = input('Enter filename prefix (with "quotes"):')
camera_number = input('Enter which camera port to use - 0 or 1 (usu. USB camera):')
dt = input('Seconds between frames (min. 2 s):')
frames = input('How many frames in total?')
#filetype = input('What file extension to use e.g. ".jpg"')

print 'Saving '+str(frames)+' frames'+' in current directory'
print 'Completion in '+str((frames+dt)/60.)+' minutes'


#timelapse(frames,dt,fnames,filetype,camera_number)
timelapse(frames=frames,dt=dt,fileprefix=fnames,ftype='.jpg',camera_port=camera_number)

