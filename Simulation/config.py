####################################
N = 100  #total population
I = 5	#number of infected people 
S = N - I #susceptible people
R = 0 #recover people

####################################
TRANS_RATE = 0.95 # prob of transmitting the virus
RECOV_RATE = (30,100) # period of recovery

####################################
QUARENTINE = True
if QUARENTINE:
	QUARENTINE_RATE = 0.9 #for no quarentine set this value >= 1.0
	QUARETNTINE_RADIUS = 40
else:
	QUARENTINE_RATE = 1.0
	QUARETNTINE_RADIUS = 0

