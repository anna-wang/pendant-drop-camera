# pendant-drop-camera

 CAPTURE-script.py is a simple Python script that'll ask you for the number of images you 
 want in a timelapse, time between frames, and which camera to use (typically cameraport 0
 is an inbuilt webcam on laptops, and cameraport 1 is anything extra you plug in).
 
 You choose the file prefix to use, and the images will be saved as 
 
 PREFIX_00.jpg, PREFIX_01.jpg, ... 
 with a metadata file, PREFIX_metadata.txt including the time between frames, and total #.
 
 It'll save the images as greyscale images. This is for pendant drop analysis.
 
 The image colour, filetype, etc. can be easily changed in capture_time_series.py.
 
 