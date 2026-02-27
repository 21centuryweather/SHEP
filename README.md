# rAM_SHEP
ACCESS-rAM3 simulations for the CORDEX Sub-Hourly Extreme Precipitation (SHEP) Australasia project

## Contributions

- Leena Khadke: project management, experiment design, analysis
- Jason Evans: project supervison, experiment design
- Mathew Lipson: model setup, ancillary generation, experiment design, running models, documentation

# Setup

**Model**: ACCESS-rAM3 (with OSTIA varying sea surface temperature)  
**Period**: 2016‑01‑27 to 2016‑01‑31 UTC  
**Boundaries**:

- ERA5 for atmosphere initialisation and lateral boundaries  
- BARRA-R2 for land initialisation  
- OSTIA for sea surface temperature

SHEP uses NRI's ACCESS-rAM3 r335209. It has been minimally updated using an optional file, and updated stashpack for outputs. SHEP source is at `https://code.metoffice.gov.uk/svn/roses-u/d/x/3/5/6/trunk`

**Nests**:  

1. GAL9 at 12.2km
2. RAL3p2 at 4.4km
3. RAL3p2 at 1.1km  

# Domain Ancillaries

See individual city folders for generation information, e.g. [Sydney](Sydney/)

Code to plot: [ancil_generation/plot_domains.py](ancil_generation/plot_domains.py).

# Instructions

## Run the OSTIA suite to generate SSTs

For any particular date, the global OSTIA Sea Surface Temperature should be generated using `u-dk517` suite (say for 2 days before, date of case, and 1 day after).

Update case information in  `u-dk517/rose-suite.conf`.

Provide a window around the case date (e.g. ±3 days) to cover simulation period and OSTIA overlap.

```
[jinja2:suite.rc]
COUNT="6"
INITIAL_CYCLE_POINT="201601260000"
OSTIA_OUTPUT="/scratch/ng72/SHEP/OSTIA_ANCIL"
SITE="nci-gadi"
```

Then `rose suite-run`

## Steps to produce Ancils

1. Checkout the standard Regional Ancillary Suite (u-bu503).

2. Copy the ancillary optional file [Sydney/rose-suite-ancils_SHEP_SY.conf](Sydney/rose-suite-ancils_SHEP_SY.conf) from this repository to your u-bu503/opt directory, where SY is the city of interest (e.g. Sydney).

3. Run the suite with the optional file (and a custom name if desired):

`rose suite-run -O ancils_SHEP_SY --name=ancils_SHEP_SY`

## Steps to run model

1. Checkout rAM3 SHEP: `rosie checkout u-dx356`

2. Inspect the example optional file [Sydney/rose-suite-SHEP_SY1.conf](Sydney/rose-suite-SHEP_SY1.conf), where SY is the city of interest (e.g. Sydney), and 1 is the case number (e.g. 1 for Case 1). Change to your case as necessary.

3. Run the suite with the optional file and a custom cylc-name:

`rose suite-run -O rAM3_SHEP_SY1 --name=SHEP_SY1 `

An example of the 12->4.4->1.1 km configuration is below:

```
# For SHEP (sub-hourly extreme precipitation) experiments: Sydney case 1
[jinja2:suite.rc]

CRUN_LEN=12
INITIAL_CYCLE_POINT="20160127T1200Z"
FINAL_CYCLE_POINT="20160130T1200Z"
global_ostia_dir="/scratch/ng72/SHEP/OSTIA_ANCIL"
dm_ec_lam_ancil_dir="/scratch/ng72/$USER/cylc-run/ancils_SHEP_SY/share/data/ancils/SHEP_SY/era5"
rg01_name="SHEP_SY"
rg01_nreslns=3

# Resolution 1 (BARRA-R2)
rg01_rs01_name="12p2"
rg01_rs01_ancil_dir="/scratch/ng72/$USER/cylc-run/ancils_SHEP_SY/share/data/ancils/SHEP_SY/BARRA-R2"
rg01_rs01_m01_stashpack=false,false,false,false,false,true,false
rg01_rs01_m01_nproc=8,12

# Resolution 2 (4.4 km)
rg01_rs02_name="4p4"
rg01_rs02_ancil_dir="/scratch/ng72/$USER/cylc-run/ancils_SHEP_SY/share/data/ancils/SHEP_SY/4p4"
rg01_rs02_m01_stashpack=false,false,false,false,false,true,false
rg01_rs02_m01_dt=100
rg01_rs02_m01_raddt=900,300
rg01_rs02_m01_lbc_freq=1800,1800

# Resolution 3 (1.1 km)
rg01_rs03_name="1p1"
rg01_rs03_3D_ancils=true
rg01_rs03_alb_anc=false
rg01_rs03_ancil_dir="/scratch/ng72/$USER/cylc-run/ancils_SHEP_SY/share/data/ancils/SHEP_SY/1p1"
rg01_rs03_m01_stashpack=false,false,false,false,false,true,false
rg01_rs03_downscale_ukv=false
rg01_rs03_kscale=false
rg01_rs03_lai_anc=true
rg01_rs03_levset="L90_40km"
rg01_rs03_nmods=1
rg01_rs03_std_model="custom"
rg01_rs03_vargrid="fixed"
rg01_rs03_zon_avg_ozone=false
rg01_rs03_m01_arch=false,false,false
rg01_rs03_m01_config="ral3p3"
rg01_rs03_m01_dt=30
rg01_rs03_m01_ic_lbc_src=2,1
rg01_rs03_m01_lbc_freq=1800,0
rg01_rs03_m01_moruses=true
rg01_rs03_m01_name="RAL3P3"
rg01_rs03_m01_nproc=32,30
rg01_rs03_m01_progdust=false,false
rg01_rs03_m01_raddt=900,300
rg01_rs03_m01_simim=false

```

## Alternative setup

We discussed also testing a 12 km -> 1.1 km setup. That is available at [Sydney/rose-suite-ancils_SHEP_SY_nonest.conf](Sydney/rose-suite-ancils_SHEP_SY_nonest.conf)






