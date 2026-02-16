# rAM_SHEP
ACCESS-rAM3 simulations for the CORDEX Sub-Hourly Extreme Precipitation (SHEP) Australasia project

## Contributions

- Leena Khadke: project management, experiment design, analysis
- Jason Evans: project supervison, experiment design
- Mathew Lipson: model setup, ancillary generation, experiment design, running models, documentation

# Setup

**Model**: ACCESS-rAM (with OSTIA varying sea surface temperature)  
**Period**: 2016‑01‑27 to 2016‑01‑31 UTC  
**Boundaries**:

- ERA5 for atmosphere initialisation and lateral boundaries  
- BARRA-R2 for land initialisation  
- OSTIA for sea surface temperature

**Nests**:  

1. GAL9 at 12.2km
2. RAL3p2 at 4.4km
3. RAL3p2 at 1.1km  

# Domain Ancillaries

See individual city folders for generation information, e.g. [Sydney/README.md](Sydney/README.md)
![SHEP domains](ancil_generation/SHEP_domains_surface_altitude.png)

Code to plot: [ancil_generation/plot_domains.py](ancil_generation/plot_domains.py).

# Case dates

## Run the OSTIA suite to generate SSTs

For any particular date, the global OSTIA Sea Surface Temperature should be generated (say for 2 days before, date of case, and 1 day after).

Checkout the OSTIA ancillary suite
`rosie checkout u-dk517`

Update case information, either through the GUI or in  `rose-suite.conf`.

```
[jinja2:suite.rc]
COUNT="4"
INITIAL_CYCLE_POINT="201601270000"
OSTIA_OUTPUT="/scratch/ng72/SHEP/OSTIA_ANCIL"
SITE="nci-gadi"
```

## Instructions to run:

`TBC`

## Analysis






