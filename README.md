# rAM_SHEP
ACCESS-rAM3 simulations for the CORDEX Sub-Hourly Extreme Precipitation (SHEP) Australasia project

## Contributions

- Mathew Lipson: model setup, ancillary generation, experiment design, running experiments, documentation
- Leena Khadke: experiment design, analysis
- Jason Evans: experiment design, analysis

# Setup

**Model**: ACCESS-rAM (with OSTIA varying sea surface temperature)  
**Model suite**: TBC
**Period**: 2016‑01‑27 to 2016‑01‑31 UTC
**Nests**: 

ERA5 for atmosphere initialisation and lateral boundaries
BARRA-R2 for land initialisation
OSTIA for sea surface temperature

1. GAL9 at 12.2km (BARRA-R2 initialised)  
2. RAL3p2 at 3km
3. RAL3p2 at 1km  

# Domains

![SHEP domains](ancil_generation/SHEP_domains_surface_altitude.png)

Code to plot: [ancils/plot_domains.py](ancils/plot_domains.py).

## Instructions to run:

See [ancils README](ancils/README.md) if they need creation, then to run experiments:

```
svn co https://code.metoffice.gov.uk/svn/roses-u/d/g/7/6/8/rns_ostia_NA
cd rns_ostia_NA
rose suite-run
```

## Analysis

1. [Rainfall, wind speed, moisture convergence](experiment_analysis.md)





