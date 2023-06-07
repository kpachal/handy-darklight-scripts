### Settings to assume:

current = 300.0 # microamps

microamp_to_e = 6.242e12 # 1 microamp = 6.2 x 10^12 electrons per second

# Factors with which to scale numbers of events.
# Computed with scale_by_solidangle
# If they are actually correct as is, set to 1.
scale_ep = 0.0812168
scale_em = 0.0472584

# Only count electrons with energy above this value in MeV:
only_above = 20.0

#######################
## Code below

import sys
import ROOT

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

# Fraction of events containing interesting process
filename = sys.argv[1]
print("Reading file",filename)
tokens = filename.split("_")
nEvents_string = [i for i in tokens if "events" in i][0]
nEvents = eval(nEvents_string.replace("events",""))
print("This corresponds to",nEvents,"events.")
infile = ROOT.TFile.Open(sys.argv[1],"READ")

# Get number of events in each spectrometer, scaled.
energy_hist_em = infile.Get("energy_in_em_eminus")
n_em_total = energy_hist_em.Integral() * scale_em
print("Total number of e- in e- spectrometer is",n_em_total)
n_in_em_trimmed = energy_hist_em.Integral(energy_hist_em.FindBin(only_above),energy_hist_em.GetNbinsX()+1) * scale_em
print("Number of e- above",only_above,"is",n_in_em_trimmed)

energy_hist_ep = infile.Get("energy_in_ep_eminus")
n_ep_total = energy_hist_ep.Integral() * scale_ep
print("Total number of e- in e+ spectrometer is",n_ep_total)
n_in_ep_trimmed = energy_hist_ep.Integral(energy_hist_ep.FindBin(only_above),energy_hist_ep.GetNbinsX()+1) * scale_ep
print("Number of e- above",only_above,"is",n_in_ep_trimmed)

# Now convert to rates using the current.
e_per_second = current * microamp_to_e
# Electron spectrometer
frac_into_em = n_in_em_trimmed/nEvents
print("Fraction is",frac_into_em)
e_per_second_into_em = e_per_second * frac_into_em
print("Electrons with E>20 per second into e- spectrometer:",e_per_second_into_em/1000000.0,"MHz")
# And same for positron.
frac_into_ep = n_in_ep_trimmed/nEvents
print("Fraction is",frac_into_ep)
e_per_second_into_ep = e_per_second * frac_into_ep
print("Electrons with E>20 per second into e+ spectrometer:",e_per_second_into_ep/1000000.0,"MHz")