import pyhepmc
import matplotlib.pyplot as plt
import numpy as np

hepmc_file = "tag_1_pythia8_events.hepmc"
#with pyhepmc.open(hepmc_file) as f:
#	event = f.read()

pos_particle_pts = []
pos_particle_etas = []
pos_particle_phis = []

neg_particle_pts = []
neg_particle_etas = []
neg_particle_phis = []

def mev_to_gev(mev):				# pT values are in MeV,
	return mev * 10**-3			# converting to GeV

num_particles = 0

with pyhepmc.open(hepmc_file) as f:
	for i, event in enumerate(f):
		for particle in event.particles:
			if particle.pid == 2000013:
				num_particles += 1
				p_pt = mev_to_gev( particle.momentum.pt() )
				pos_particle_pts.append(p_pt)
				p_eta = particle.momentum.eta()
				pos_particle_etas.append(p_eta)
				p_phi = particle.momentum.phi()
				pos_particle_phis.append(p_phi)
			elif particle.pid == -2000013:
				num_particles += 1
				n_pt = mev_to_gev( particle.momentum.pt() )
				neg_particle_pts.append(n_pt)
				n_eta = particle.momentum.eta()
				neg_particle_etas.append(n_eta)
				n_phi = particle.momentum.phi()
				neg_particle_phis.append(n_phi)

print(num_particles)

with pyhepmc.open(hepmc_file) as f:
	for i, event in enumerate(f):
		print("i:",i,"event#:",event.event_number)
