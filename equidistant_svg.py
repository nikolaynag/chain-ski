#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import numpy as np
from numpy import sqrt, cos, sin, pi
import matplotlib.pyplot as plt

TEMPLATE="""<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="{Wmm}mm" height="{Hmm}mm" viewBox="0 0 {W} {H}"
     xmlns="http://www.w3.org/2000/svg" version="1.1">
  <title>Equidistant path</title>
  <desc>A path that draws equidistant from ellipse</desc>
  <path d="{commands}" fill="none" stroke="black" stroke-width="200" />
</svg>
"""

def make_svg_path(x, y):
    if len(x) < 1:
        return
    assert(len(x) == len(y))
    minx, miny = min(x), min(y)
    maxx, maxy = max(x), max(y)
    width = maxx - minx
    height = maxy - miny
    def translate_coords(x,y):
        return int((x - minx)*1000), int((y - miny)*1000)
    commands = "M {} {}".format(*translate_coords(x[0], y[0]))
    for i in range(1, len(x)):
        commands += " L {} {}".format(*translate_coords(x[i], y[i]))
    return TEMPLATE.format(
        Wmm = width,
        Hmm = height,
        W = int(width*1000),
        H = int(height*1000),
        commands = commands + " z"
    )
    
def ellipse_equidistant(t, h, a, b):
    x = a*cos(t)-(b*h*cos(t))/sqrt(a**2*sin(t)**2+b**2*cos(t)**2)
    y = b*sin(t)-(a*h*sin(t))/sqrt(a**2*sin(t)**2+b**2*cos(t)**2)
    return x, y

t = np.linspace(-pi/2, pi/2, 300)
L = 40
D = 16
alpha = 0.9831669742420941
xr, yr = ellipse_equidistant(t, D/2, L*cos(alpha), L*sin(alpha))
xl = -2*L - xr
yl = -yr
x = np.append(xr, xl)
y = np.append(yr, yl)
sys.stdout.write(make_svg_path(x, y))

