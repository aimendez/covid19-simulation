# COVID19 Agent-Based Simulation

Pygame implementation of an Agent-based Simulation of the spread of a COVID19-like virus in a closed environment.

**config.py**

File containg initial conditions of the population and relevant variables that determine the dynamics of the disease.
Can be modified to test the evolution of the spread under different conditions. 

**Parameters**

  N (*int*): Total population
  I (*int*): Initial number of infected people

  TRANS_RATE (*float*): Transmision rate of virus - probability of infecting other people -
  RECOV_RATE (*range float*): Recovery rate - number of iterations until recovery -

  QUARENTINE (*bool*): if True, some of the infected people will be put in quarentine. The chances of being put in quarentine are determined by QUARENTINE_RATE.
  QUARENTINE_RATE (*float*): Probability of being put in quarentine after getting infected.
  QUARENTINE_RADIUS (*int*): Radius of the quarentine area. Other people cannot cross this area. 
