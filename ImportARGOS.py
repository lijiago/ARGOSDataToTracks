##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2023
## Author: lijia.go@duke.edu (for ENV859) #this chunk is known as a boiler plate
##---------------------------------------------------------------------

# Import modules
import sys, os, arcpy #libraries typically used in GIS scripting 

# Set input variable (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFile = 'V:/ARGOSTracking/Scratch/ARGOSTrack.shp'