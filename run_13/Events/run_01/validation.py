# ---LHE FILE PARSING---

import awkward as ak
import pylhe

lhe_file = "unweighted_events.lhe"

arr = pylhe.to_awkward(pylhe.read_lhe_with_attributes(lhe_file))

i = 0

pos = 0
neg = 0 

while i < len(arr.particles.id):
	for p in arr.particles.id[i]:
		if p == 2000013:
			pos += 1
		elif p == -2000013:
			neg += 1
	i += 1
print("Smuon total =", pos+neg)
print(f"Number of events: {pylhe.read_num_events(lhe_file)}")



# ---HEPMC FILE PARSING---

import numpy as np
import pyhepmc
from pyhepmc.view import savefig
import matplotlib.pyplot as plt

# Alaa's validater
hepmc_file = "tag_1_pythia8_events.hepmc"

with pyhepmc.open(hepmc_file) as f:
	for j, event in enumerate(f):
		savefig(event, f"event{j}.svg")
		savefig(event, f"event{j}.png")
		savefig(event, f"event{j}.pdf")

# Jordan's version

num_bins = 5
