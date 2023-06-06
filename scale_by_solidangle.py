import math

# Acceptances are plus or minus
central_thetas = [20,36] # degrees
acceptance_theta = 2.0 # degrees - correct if need be
acceptance_phi = 5.0 # degrees

for theta in central_thetas :

    # Solid angle integrals:
    # Omega = int_phi dphi int_theta sin theta dtheta
    # = (- cos theta)| thetas * phi| phis

    # I am looking for a fraction of the annulus which actually corresponds to the spectrometer.
    # Annulus has same theta range as spectrometer: cancels out in fraction. So I just have
    # fraction = delta_phi/(2.*math.pi) where delta_phi is the range of actual phi subtended at the relevant theta.

    # Acceptance is defined in terms of a full circle I think,
    # but actually a different proportion of distance over circle at different angles....
    fraction_subtended_perp = 2. * acceptance_phi / 360.
    circumference_perp = 1.0 # set R = 1, r = R sin theta. Scale out 2pi
    circumference_attheta = math.sin(math.radians(theta))
    fraction = fraction_subtended_perp/circumference_attheta

    print("For central spectrometer angle",theta,",")
    print("\tscale number of events in annulus by",fraction,"to get number in spectrometer.")