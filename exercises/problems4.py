####
# 4_A
####

# Write a class that controlls a syringe pump with an integrated valve 
# (3-way valve connecting syringe with either input or output)

# The example given in session4.py is a good starting point, copy-paste and adapt it. 
# Use a list to simulate the connection as shown in the example.

# The pump recognizes commands built as follows:
# /adress/command/end (e.g. device A, command INJECT: '/A/INJECT/end' )

# Each pump supports the following commands:
# CALIBRATE, INJECT, WITHDRAW, STOP		control syringe movements
# VIN, VOUT								control valve position

# All commands must be available through their separate method.
# e.g. INJECT should be available as pump.inject() for convenience



####
# 4_B
####

# Using your pump class create two pump instances with adresses A and B
# These are your pumps, running a droplet experiment (A = Oil, B = Water):

# 1. Calibrate both pumps
# 2. Switch both pumps to valve in and withdraw, to fill syringes
# 3. Start by filling the chip with oil (switch valve to out and inject)
# 4. Now start injecting water to produce droplets
# 5. You blew your chip up: STOP BOTH PUMPS!
# 6. Empty both pumps through the input (to save some of the precious precursors)

# Your done for the day, no more chips...

# What commands are in the connection list?



#### 
# 4_C
####

# Add a method valve(status) to your pump that takes one boolean as an argument
# Switch the valve according to the boolean
# e.g.  pump.valve(True) 	--> send VIN command
#		pump.valve(False) 	--> send VOUT command

# Now add method pump to your pump that does the same for inject, withdraw
# e.g. 	pump.pump(True)		--> send INJECT command
#		pump.pump(False)	--> send WITHDRAW command



####
# 4_D: Automated chip testing
####

# Your are testing a PDMS chip with pressure-based valves.
# The chip has 5 valves, each identified by a number between 0 and 4.
# The testing procedure is as follows:
# Repeat 50 times:
# 	  - Select 2 random valves out of the 5 available
#	  - Print valve numbers (pretend you would actually switch valves)
#	  - Wait half a second, use:
#		import time
#		time.sleep(0.5)

# If the chip is still ok after this stress test it is ready for use...