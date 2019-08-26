import os, errno
from paraview.simple import *

# Get active view
view = GetActiveView()
cam = GetActiveCamera()
dp = GetDisplayProperties()

# Parameters
res = 10
elev = 3
start = 0
alpha = 360/elev
theta = 360/res
save_path = "F:/"

# Background Colour
view.Background = [1, 1, 1]  #white

#set image size
view.ViewSize = [500, 600] #[width, height]

# Set Display Properties
dp.DiffuseColor = [0, 0, 1] # Surface Colour
dp.Representation = "Surface" # Representation

# Initialize Start View
cam.SetFocalPoint(0, 0, 16.5)
cam.SetPosition(105.5, 0, 16.5)
cam.SetViewUp(0, 0, 1)
cam.ViewAngle = 25
cam.OrthogonalizeViewUp()
Render()

def filer(name):
    spath = os.path.join(save_path, name)
    if not os.path.exists(spath):
        os.makedirs(spath)
    return

for i in range (elev-1):
    cam.Roll(alpha)
    Render()
    filer(str(i))
# Rotate 360 in increments of theta
    for x in range (res-1):
        cam.Azimuth(theta)
        Render()
        SaveScreenshot("F:/{}/image{}.png".format(i, x))


