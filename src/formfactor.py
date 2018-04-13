# -*- coding: utf-8 -*-
import numpy as np

###############################################################################
## Form Factors 2D
###############################################################################  
    
def ff_orthogonal_2D(w, h):
    '''
    
    F1->2
    
     |2
    h| 
     |____ 1
        w
    '''
    w = np.float64(w)
    h = np.float64(h)
    
    return 0.5 - 0.5 * ff_parallel_2D(w, h)
    
def ff_parallel_2D(w, h):
    '''
    
    F1->2
    
     ____ 2
    |h
    |____ 1
       w
    '''
    w = np.float64(w)
    h = np.float64(h)
    
    return (np.sqrt(h*h + w*w) - h) / w

###############################################################################
## Form Factors 3D
###############################################################################

def ff_orthogonal_3D(w, l, h):
    '''
    Two finite rectangles of same length, having one common edge, and at an angle of 90° to each other.
    F1->2
    
      l/|
      / |
     h|2|-----/
      | / 1  /
      |/____/
         w
    Hottel 1931; Hamilton and Morgan; Byun 1999
    @src: http://www.thermalradiation.net/sectionc/C-14.html
    '''
    w = np.float64(w)
    l = np.float64(l)
    h = np.float64(h)
    
    H = h/l
    W = w/l
    HH = H*H
    WW = W*W
    return ((1.0 / (W * np.pi)) * (W * np.arctan(1.0 / W) + H * np.arctan(1.0 / H)
            - np.sqrt(HH + WW) * np.arctan(1.0 / np.sqrt(HH + WW))
            + 0.25 * np.log((1.0 + WW) * (1.0 + HH) / (1.0 + WW + HH))
            + 0.25 * WW * np.log(WW * (1.0 + WW + HH) / ((1 + WW) * (WW + HH)))
            + 0.25 * HH * np.log(HH * (1.0 + WW + HH) / ((1 + HH) * (WW + HH)))))
    
def ff_parallel_3D(w, h, l):
    '''
    Identical, parallel, directly opposed rectangles.
    F1->2
          w
       /----/
    h / 2  /
     /----/
     | 
    l| /----/
     |/ 1  /
     /----/
    Hottel 1931; Hamilton and Morgan; Byun 1999, Narayana 1998 
    @src: http://www.thermalradiation.net/sectionc/C-11.html
    '''
    w = np.float64(w)
    l = np.float64(l)
    h = np.float64(h)
    
    X = w/l
    Y = h/l
    XX = X*X
    YY = Y*Y
    return (2.0 / (np.pi * X * Y) * (0.5 * np.log((1 + XX) * (1 + YY) / (1 + XX + YY)) \
            + X * np.sqrt(1 + YY) * np.arctan(X / np.sqrt(1 + YY)) \
            + Y * np.sqrt(1 + XX) * np.arctan(Y / np.sqrt(1 + XX)) \
            - X * np.arctan(X) - Y * np.arctan(Y)))
            
###############################################################################
## Tests
###############################################################################
from assert_utils import assertEqual

def _test_ff_2D(w=1.0, h=2.0):
    assertEqual(ff_parallel_2D(w, h) + 2.0 * ff_orthogonal_2D(w, h), 1.0)
    assertEqual(ff_parallel_2D(h, w) + 2.0 * ff_orthogonal_2D(h, w), 1.0)
    
def _test_ff_3D(w=1.0, h=2.0, l=3.0):
    assertEqual(ff_parallel_3D(w, h, l), ff_parallel_3D(h, w, l))
    assertEqual(ff_parallel_3D(w, l, h), ff_parallel_3D(l, w, h))
    assertEqual(ff_parallel_3D(l, h, w), ff_parallel_3D(h, l, w))
    
    assertEqual(ff_parallel_3D(h, l, w) +  2.0 * ff_orthogonal_3D(h, l, w) + 2.0 * ff_orthogonal_3D(l, h, w), 1.0)
    assertEqual(ff_parallel_3D(h, w, l) +  2.0 * ff_orthogonal_3D(h, w, l) + 2.0 * ff_orthogonal_3D(w, h, l), 1.0)
    assertEqual(ff_parallel_3D(l, w, h) +  2.0 * ff_orthogonal_3D(l, w, h) + 2.0 * ff_orthogonal_3D(w, l, h), 1.0)
