#!/usr/bin/python
import numpy
import pylab

# da equation is
# dV/dt = 1/tau_m * (-V + I*Rm)
T = 50       # total time to simulate (msec)
dt = 0.125 # simulation time step (msec)
time = numpy.arange(0, T + dt, dt) # time array
t_rest = 0 # initial refractory time

# LIF Properties

Vm = numpy.zeros(len(time)) # potential (V) trace over time
Rm = 1                  # resistance (kOhm)
Cm = 10                   # Capacicante (uF)
tau_m = Rm * Cm        # time constant (msec)
tau_ref = 4           # refractory period (msec)
Vth = 1            # spike threshold (V)
V_spike = 0.5      # spike delta (V)

# Stimulus
I = 1.5        # Input current (A)

# Iterate over each time step
print "t (msec),voltage (mV)"
for i, t in enumerate(time):
    if t > t_rest:
        Vm[i] = Vm[i-1] + (-Vm[i-1] + I*Rm) / tau_m * dt
        if Vm[i] >= Vth:
            Vm[i] += V_spike
            t_rest = t + tau_ref
        print str(t) + ", " + str(Vm[i])

# Plot membrane potential trace
pylab.plot(time, Vm)
pylab.title('Leaky Integrate and Fire example')
pylab.ylabel('Membrane Potential (V)')
pylab.xlabel('Time(msec)')
pylab.ylim([-0.1,2.0])
pylab.savefig("plot.jpg")

