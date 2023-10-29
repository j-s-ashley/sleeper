# Generation Process


## Initial Set Up

	Clone essential repos and pull necessary Docker image:
	`
	git clone https://github.com/lawrenceleejr/DVMuReint.git

	git clone https://github.com/A-A-Abdelhamid/LLP_Sleptons_RPV_SUSY.git

	docker pull scailfin/madgraph5-amc-nlo:mg5_amc3.3.1
	`

## Start Up

	Run the Docker image (DO NOT use the latest version)

	`docker run --rm -ti -v $PWD:$PWD -w $PWD scailfin/madgraph5-amc-nlo:mg5_amc3.3.1`

	Download the PDF set

	`lhapdf get NNPDF23_lo_as_0130_qed`

	Run MadGraph

	`mg5_aMC`
## Event Generation
	
	Import SUSY model

	`import model /userdata/jordan/DVMuReint/RPVMSSM_UFO/RPVMSSM_UFO/`

	Set definitions

	`define q = g u c d s u~ c~ d~ s~ b t b~ t~ h01 h2 h3 h+ h-

	define p = g u c d s u~ c~ d~ s~ b b~`

	Generate event

	`generate p p > mur- mur+ /q

	display processes

	output /userdata/jordan/run_13`

	Edit parameter card

	'shell vi /userdata/jordan/run_13/Cards/param_card.dat

	:set number

	i`

	Change Smuon mass and decay parameters ("The mass (in GeV) is in line 51 1000013 4.000000e+02 # msl2 400 GeV The decay width is in line 757 DECAY 1000013 6.500000e-15")

		- Line 59: change 2.029157e+02 to 4.000000e+02
		- Line 77: change 1.441028e+02 to 4.000000e+02
		- Line 458: change 2.126822e-01 to 6.500000e-15
		- Add line break after 458
		- (New) line 459:    1               2    13  -12 

	Escape to exit <insert> mode, then :wq to write and quit.

	Edit run card

	`shell vi /userdata/jordan/run_13/Cards/run_card.dat

	:set number

	i`

	Change number of events and time of flight and set decay width error handling. 

		- Line 26: change 10000 to 10
		- Line 65: change -1.0 to 0.0
		- Add three line breaks at the end of the document
		- (New) line 141, add 1e-30 = small_width_treatment

	Escape to exit <insert> mode, then :wq to write and quit.

	`LAUNCH`

	Enable Pythia showering

	`shower=Pythia8`
