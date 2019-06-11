
import sys
print(sys.path)

from ij import IJ
from ij.io import DirectoryChooser
import os

print("aaa")
def Analysis(imagepath):
    imp = IJ.openImage(imagepath)
    savefilepath = os.path.splitext(imagepath)[0]
    print("aaa")
#####################################################
# Write your script

    IJ.run(imp, "Subtract Background...", "rolling=15")
    IJ.setAutoThreshold(imp, "Default dark")
    IJ.run("Set Measurements...", "area mean centroid fit limit redirect=None decimal=3")
    IJ.run(imp, "Analyze Particles...", "size=5-Infinity display exclude clear")
    IJ.saveAs("Results", savefilepath + "result.csv")

#####################################################

    imp.close()


srcDir = DirectoryChooser("Choose Folder").getDirectory()
IJ.log("directory: " + srcDir)

for root, directories, filenames in os.walk(srcDir):
    for filename in filenames:
        if filename.endswith(".tif"):
            path = os.path.join(root, filename)
            IJ.log(path)
            Analysis(path)

IJ.log("Finish")
