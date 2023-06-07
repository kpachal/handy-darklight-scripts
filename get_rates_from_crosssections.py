from scipy import constants
# Guts from Story!!

# Cross section, converted to m^2
# Recall radgen outputs cm^2
xsec_cm2 = 7.79208e-30 # cm^2
xsec_m2 = xsec_cm2 * 1.e-4 # m^2

# Material: tantalum
TARGET_RHO = 16.69e6 #g/m3
MOLAR_MASS = 180.95 #g/mol
ATOMS_RHO = TARGET_RHO/MOLAR_MASS * constants.N_A # atoms/m3

#######################
## Code below

# Function which returns (SI) luminosity by mutiplying incident flux, target density, & depth.
# Expects beam_current in microamps and target_depth in microns.
def luminosity(beam_curr, target_depth, target_density=ATOMS_RHO):
    current_elec = beam_curr * 1.e-6 * 6.28e18 # μA * (1e-6 A/μA) * 6.28e18 e/s / A = electrons/s
    luminosity = target_density * (target_depth * 1.e-6) * current_elec # atoms/m3 * m * electrons/s = (electron-atoms)/(m^2 * s)
    return luminosity

import sys

if len(sys.argv) < 2 :
    print("Give a current!")
    exit(0)

# Fraction of events containing interesting process
current = eval(sys.argv[1])
if len(sys.argv) > 2 :
    target_thickness = eval(sys.argv[2])
else :
    target_thickness = 1.0 # micron


print("Evaluating rate for cross section",xsec_m2,"m^2, current",current,"microAmps, and a",target_thickness,"micron target.")
lumi = luminosity(current, target_thickness)
print("Luminosity is",lumi,"m^-2 s^-1")
rate = xsec_m2 * lumi *73 * 73 # electron-atoms per second
print("Gives a rate of",rate/1.e6,"MHz")

