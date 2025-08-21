## Steps to produce

1. Checkout the standard Regional Ancillary Suite (u-bu503).
2. Change the following lines in `u-bu503/app/ancil_lct_postproc_wc_urban/rose-app.conf`

-source_WC=${ANCIL_PREPROC_PATH}/urban_fraction.nc
+source_WC=/g/data/fy29/mjl561/data_sources/WorldCover_urban/urban_fraction_v200.nc

3. Copy the optional file from this repository to your u-bu503/opt directory:

`cp rose-suite-rAM_SHEP.conf ~/roses/u-bu503/opt/`

4. Run the suite with the optional file (and a custom name if desired):

`rose suite-run -O rAM_SHEP --name=ancils_SHEP`

## Results

Four sets of ancillaries for 1 driving model and 3 nests.

![SHEP domains](SHEP_domains_surface_altitude.png)