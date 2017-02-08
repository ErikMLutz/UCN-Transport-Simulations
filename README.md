# UCN-Transport-Simulations
Upgrade and use of Adam Holley's neutron transport code for use in the NCSU UCN project.

To Do:
GENERAL
  -Edit Transport Simulator.c to read a parameters file to set the rest of the parameters that are defined as macros in the beginning
  
LEUNG SOURCE     
  -Edit Transport simulator so that poof() can be called with a random offset from the cutplane to enable particle generation anywhere in a region: use for Leung Next Generation Source
  -Edit transport simulator so that cutplanes can reflect particles with same properties as region. create new special handling code in connex file for this
  
FROST SIMULATIONS
  -Edit Transport simulator to enable 108neV boost in random direction on contact with a cutplane: use for simulation of frost on surface of deuterium
