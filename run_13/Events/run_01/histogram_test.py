import pyhepmc
import matplotlib.pyplot as plt
import numpy as np

hepmc_file = "tag_1_pythia8_events.hepmc"
with pyhepmc.open(hepmc_file) as f:
	event = f.read()

pos_particle_pts = []
pos_particle_etas = []
pos_particle_phis = []

neg_particle_pts = []
neg_particle_etas = []
neg_particle_phis = []

def mev_to_gev(mev):				# pT values are in MeV,
	return mev * 10**-3			# converting to GeV

num_particles = 0

for particle in event.particles:
	num_particles += 1
	if particle.pid == 2000013:
		p_pt = mev_to_gev( particle.momentum.pt() )
		pos_particle_pts.append(p_pt)
		p_eta = particle.momentum.eta()
		pos_particle_etas.append(p_eta)
		p_phi = particle.momentum.phi()
		pos_particle_phis.append(p_phi)
	elif particle.pid == -2000013:
		n_pt = mev_to_gev( particle.momentum.pt() )
		neg_particle_pts.append(n_pt)
		n_eta = particle.momentum.eta()
		neg_particle_etas.append(n_eta)
		n_phi = particle.momentum.phi()
		neg_particle_phis.append(n_phi)

# HISTOGRAM STUFF

def sturges(obs):
	val = 1 + ( 3.322 * np.log10(obs) )
	return int( round(val) )

# num_bins = sturges(num_particles / 2)

range_min = 0
range_max = 10**6

# --- pT ---
plt.hist(pos_particle_pts, range=(range_min, range_max), histtype='step', label='Positively charged smuons')
plt.hist(neg_particle_pts, range=(range_min, range_max), histtype='step', label='Negatively charged smuons')

plt.xlabel('pT [GeV]')
plt.ylabel('Number of Smuons')
plt.legend()
plt.title('Smuon pT')

plt.savefig('Smuon_pT_v2.0.pdf', bbox_inches='tight')
plt.savefig('Smuon_pT_v2.0.png', bbox_inches='tight')

plt.grid()
plt.show()


# --- pT2 ---
# Attempting to calculate pT separately.

# def xy_to_pt(px, py):
# 	return np.sqrt( (px * px) + (py * py) )

# pos_px = []
# pos_py = []

# neg_px = []
# neg_py = []

# for particle in event.particles:
#	if particle.pid == 2000013:
#		p_px = particle.momentum.px
#		pos_px.append(p_px)
#		p_py = particle.momentum.py
#		pos_py.append(p_py)
#	elif particle.pid == -2000013:
#		n_px = particle.momentum.px
#		neg_px.append(n_px)
#		n_py = particle.momentum.py
#		neg_py.append(n_py)

#pos_pt2 = []
#neg_pt2 = []

#for i, smuon in enumerate(pos_px):
#	pos_pt2.append( mev_to_gev( xy_to_pt(pos_px[i], pos_py[i]) ) )
#	#neg_pt2.append( mev_to_gev( xy_to_pt(neg_px[i], pos_px[i]) ) )

#plt.hist(pos_pt2, range=(range_min, range_max), histtype='step', label='Positively charged smuons')
#plt.hist(neg_pt2, range=(range_min, range_max), histtype='step', label='Negatively charged smuons')

#plt.xlabel('pT [GeV]')
#plt.ylabel('Number of Smuons')
#plt.legend()
#plt.title('Calculated Smuon pT')

#plt.savefig('Calc_Smuon_pT_v2.0.pdf', bbox_inches='tight')
#plt.savefig('Calc_Smuon_pT_v2.0.png', bbox_inches='tight')

#plt.grid()
#plt.show()


# --- eta ---
plt.hist(pos_particle_etas, range=(range_min, range_max), histtype='step', label='Positively charged smuons')
plt.hist(neg_particle_etas, range=(range_min, range_max), histtype='step', label='Negatively charged smuons')

plt.xlabel('$\eta$')
plt.ylabel('Number of Smuons')
plt.legend()
plt.title('Smuon $\eta$')

plt.savefig('Smuon_eta_v2.0.pdf', bbox_inches='tight')
plt.savefig('Smuon_eta_v2.0.png', bbox_inches='tight')

plt.grid()
plt.show()


# --- phi ---
plt.hist(pos_particle_phis, range=(range_min, range_max), histtype='step', label='Positively charged smuons')
plt.hist(neg_particle_phis, range=(range_min, range_max), histtype='step', label='Negatively charged smuons')

plt.xlabel('$\phi$')
plt.ylabel('Number of Smuons')
plt.legend()
plt.title('Smuon $\phi$')

plt.savefig('Smuon_phi_v2.0.pdf', bbox_inches='tight')
plt.savefig('Smuon_phi_v2.0.png', bbox_inches='tight')

plt.grid()
plt.show()

