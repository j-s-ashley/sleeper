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

def eVtoGeV(eV):				# Pretty sure I'm getting pT values in eV,
	return eV * 10**-9			# so I'm converting those values to GeV

num_particles = 0

for particle in event.particles:
	num_particles += 1
	if particle.pid == 2000013:
		p_pt = eVtoGeV( particle.momentum.pt() )
		pos_particle_pts.append(p_pt)
		p_eta = particle.momentum.eta()
		pos_particle_etas.append(p_eta)
		p_phi = particle.momentum.phi()
		pos_particle_phis.append(p_phi)
	elif particle.pid == -2000013:
		n_pt = eVtoGeV( particle.momentum.pt() )
		neg_particle_pts.append(n_pt)
		n_eta = particle.momentum.eta()
		neg_particle_etas.append(n_eta)
		n_phi = particle.momentum.phi()
		neg_particle_phis.append(n_phi)

# HISTOGRAM STUFF

def sturges(obs):
	val = 1 + ( 3.322 * np.log10(obs) )
	return int( round(val) )

num_bins = sturges(num_particles / 2)


# --- pT ---
plt.hist(pos_particle_pts, num_bins, histtype='step', label='Positively charged smuons')
plt.hist(neg_particle_pts, num_bins, histtype='step', label='Negatively charged smuons')

plt.xlabel('pT [GeV]')
plt.ylabel('Number of Smuons')
plt.legend()
plt.title('Smuon pT')

plt.savefig('Smuon_pT.pdf', bbox_inches='tight')
plt.savefig('Smuon_pT.png', bbox_inches='tight')

plt.grid()
plt.show()


# --- eta ---
plt.hist(pos_particle_etas, num_bins, histtype='step', label='Positively charged smuons')
plt.hist(neg_particle_etas, num_bins, histtype='step', label='Negatively charged smuons')

plt.xlabel('$\eta$')
plt.ylabel('Number of Smuons')
plt.legend()
plt.title('Smuon $\eta$')

plt.savefig('Smuon_eta.pdf', bbox_inches='tight')
plt.savefig('Smuon_eta.png', bbox_inches='tight')

plt.grid()
plt.show()


# --- phi ---
plt.hist(pos_particle_phis, num_bins, histtype='step', label='Positively charged smuons')
plt.hist(neg_particle_phis, num_bins, histtype='step', label='Negatively charged smuons')

plt.xlabel('$\phi$')
plt.ylabel('Number of Smuons')
plt.legend()
plt.title('Smuon $\phi$')

plt.savefig('Smuon_phi.pdf', bbox_inches='tight')
plt.savefig('Smuon_phi.png', bbox_inches='tight')

plt.grid()
plt.show()

