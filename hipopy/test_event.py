#!/usr/bin/env python
from __future__ import print_function

import collections
import sys
import time

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

from hipopy import Event, LorentzVector, Particle, hipo_reader, detector
from ROOT import TLorentzVector, TH2D, TFile
MASS_P = 0.93827
c_special_units = 29.9792458

def vertex_time(sc_time, sc_pathlength, relatavistic_beta):
	return sc_time - sc_pathlength / (relatavistic_beta * c_special_units)

def calc_dt(vertex, momentum, sc_t, sc_r, mass):
    mp = mass/momentum
    beta = 1.0 / np.sqrt(1.0 + mp * mp)
    return vertex - vertex_time(sc_t, sc_r, beta)

style.use('fivethirtyeight')
fig = plt.figure(figsize=(16, 9))

file_name = sys.argv[1]
reader = hipo_reader(file_name)
data = Event(reader)

delta_t = TH2D( 'delta_t', '#Delta T Protons', 500, 0.0, 7.0, 500, -10, 10)
hfile = TFile( 'example.root', 'RECREATE')

start = time.time()
i = 0
for event in data:
    i += 1
    sc_r_vertex = event.getPath(detector['FTOF1A'], 0)
    sc_t_vertex = event.getTime(detector['FTOF1A'], 0)

    vertex = vertex_time(sc_t_vertex, sc_r_vertex, 1.0)
    for x in range(1, len(event)):
        momentum = event.particle[x].P
        if momentum == 0:
            continue
        sc_r = event.getPath(detector['FTOF1A'], x)
        sc_t = event.getTime(detector['FTOF1A'], x)
        delta_t.Fill(momentum, calc_dt(vertex, momentum, sc_t, sc_r, MASS_P))

end = time.time()
print((end - start), "Sec")
print((i / (end - start)), "Hz")

hfile.cd()
delta_t.Write()
hfile.Write()
