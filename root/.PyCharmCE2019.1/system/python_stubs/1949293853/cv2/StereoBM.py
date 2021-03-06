# encoding: utf-8
# module cv2 calls itself cv2.cv2
# from /opt/ros/kinetic/lib/python2.7/dist-packages/cv2.so
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2.cv2 as  # /usr/local/lib/python3.5/dist-packages/cv2/cv2.cpython-35m-x86_64-linux-gnu.so
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.ml as ml # <module 'cv2.ml'>
import os as os # /usr/lib/python3.5/os.py
import cv2.data as data # /usr/local/lib/python3.5/dist-packages/cv2/data/__init__.py
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.instr as instr # <module 'cv2.instr'>
import importlib as importlib # /usr/lib/python3.5/importlib/__init__.py
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.cv2 as cv2 # /usr/local/lib/python3.5/dist-packages/cv2/cv2.cpython-35m-x86_64-linux-gnu.so
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
from cv2.cv2 import (createButton, createTrackbar, dnn_registerLayer, 
    dnn_unregisterLayer, redirectError, setMouseCallback)


from .StereoMatcher import StereoMatcher

class StereoBM(StereoMatcher):
    # no doc
    def create(self, numDisparities=None, blockSize=None): # real signature unknown; restored from __doc__
        """
        create([, numDisparities[, blockSize]]) -> retval
        .   @brief Creates StereoBM object
        .   
        .   @param numDisparities the disparity search range. For each pixel algorithm will find the best
        .   disparity from 0 (default minimum disparity) to numDisparities. The search range can then be
        .   shifted by changing the minimum disparity.
        .   @param blockSize the linear size of the blocks compared by the algorithm. The size should be odd
        .   (as the block is centered at the current pixel). Larger block size implies smoother, though less
        .   accurate disparity map. Smaller block size gives more detailed disparity map, but there is higher
        .   chance for algorithm to find a wrong correspondence.
        .   
        .   The function create StereoBM object. You can then call StereoBM::compute() to compute disparity for
        .   a specific stereo pair.
        """
        pass

    def getPreFilterCap(self): # real signature unknown; restored from __doc__
        """
        getPreFilterCap() -> retval
        .
        """
        pass

    def getPreFilterSize(self): # real signature unknown; restored from __doc__
        """
        getPreFilterSize() -> retval
        .
        """
        pass

    def getPreFilterType(self): # real signature unknown; restored from __doc__
        """
        getPreFilterType() -> retval
        .
        """
        pass

    def getROI1(self): # real signature unknown; restored from __doc__
        """
        getROI1() -> retval
        .
        """
        pass

    def getROI2(self): # real signature unknown; restored from __doc__
        """
        getROI2() -> retval
        .
        """
        pass

    def getSmallerBlockSize(self): # real signature unknown; restored from __doc__
        """
        getSmallerBlockSize() -> retval
        .
        """
        pass

    def getTextureThreshold(self): # real signature unknown; restored from __doc__
        """
        getTextureThreshold() -> retval
        .
        """
        pass

    def getUniquenessRatio(self): # real signature unknown; restored from __doc__
        """
        getUniquenessRatio() -> retval
        .
        """
        pass

    def setPreFilterCap(self, preFilterCap): # real signature unknown; restored from __doc__
        """
        setPreFilterCap(preFilterCap) -> None
        .
        """
        pass

    def setPreFilterSize(self, preFilterSize): # real signature unknown; restored from __doc__
        """
        setPreFilterSize(preFilterSize) -> None
        .
        """
        pass

    def setPreFilterType(self, preFilterType): # real signature unknown; restored from __doc__
        """
        setPreFilterType(preFilterType) -> None
        .
        """
        pass

    def setROI1(self, roi1): # real signature unknown; restored from __doc__
        """
        setROI1(roi1) -> None
        .
        """
        pass

    def setROI2(self, roi2): # real signature unknown; restored from __doc__
        """
        setROI2(roi2) -> None
        .
        """
        pass

    def setSmallerBlockSize(self, blockSize): # real signature unknown; restored from __doc__
        """
        setSmallerBlockSize(blockSize) -> None
        .
        """
        pass

    def setTextureThreshold(self, textureThreshold): # real signature unknown; restored from __doc__
        """
        setTextureThreshold(textureThreshold) -> None
        .
        """
        pass

    def setUniquenessRatio(self, uniquenessRatio): # real signature unknown; restored from __doc__
        """
        setUniquenessRatio(uniquenessRatio) -> None
        .
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


