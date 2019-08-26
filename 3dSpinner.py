import os, errno
from paraview.simple import *
import numpy as np

settings_file = "settings.csv"

# Initialize Start View
cam.SetFocalPoint(0, 0, 16.5)
cam.SetPosition(105.5, 0, 16.5)
cam.SetViewUp(0, 0, 1)
cam.ViewAngle = 25
cam.OrthogonalizeViewUp()
Render()

def filer(name, save_path):
    spath = os.path.join(save_path, name)
    if not os.path.exists(spath):
        os.makedirs(spath)
    return

def loader(settings_file):
        try:
            data = np.loadtxt(open(settings_file, "rb"), delimiter = "|" , skiprows = 1)

        except Exception as e:
            er = "Error Occurred: "+ str(e)
            print(er)
            break
        return bgColour, imgSize, difColour, rep, focalP, pos, vUp, vAngle, res, elev, save_path

def getView(model_path):
    
    # Load Model
    model = STLReader (FileName=[model_path])
    SetActiveSource(model)
    view = GetActiveViewOrCreate('RenderView')
    Show(model, view)

    # Camera Settings
    cam = GetActiveCamera()
    dp = GetDisplayProperties()
    view.Background = bgColour # Backgrount Colour
    view.ViewSize = imgSize # Image Size
    dp.DiffuseColor = difColour # Surface Colour
    dp.Representation = rep # Representation
    cam.SetFocalPoint = focalP # Focal Camera Point
    cam.SetPosition = pos # Initial Camera Position
    cam.SetViewUp = vUp # Initial View Up
    cam.ViewAngle = vAngle # Camera Angle
    cam.OrthogonalizeViewUp() # Camera Parallel Projection
    Render()
    return

def spinner(elev,res, save_path)
alpha = 360/elev
theta = 360/res
for i in range (elev-1):
    cam.Roll(alpha)
    Render()
    filer(str(i))
# Rotate 360 in increments of theta
    for x in range (res-1):
        cam.Azimuth(theta)
        Render()
        SaveScreenshot(os.path.join(save_path,"{}/image{}.png".format(i, x))


