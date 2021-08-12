# transformer
A utility tool for transforming spatial data

## Description
A simple tool using Docker and GDAL to support spatial data transforms.

Currently supported transforms (processes):
* re-projection
* clip


## Use
  
Build docker image  
`docker build . -t transformer`

### re-projection
Re-projects any spatial files found in the input directory. The transformed file is saved in the outputs directory with the same file name as the input.

`docker run -v <local path>/transformer/output:/data/outputs --env process=re-project -t transformer`

Default output projection is British National Grid (27700), though output can be specified by using an additional environmental variable:  
`--env output_crs=<EPSG code for chosen crs>`

### clip
Clips a spatial input dataset to a new spatial boundary (currently this must be supplied as a spatial dataset).

`docker run -v <local path>/transformer/output:/data/outputs --env process=re-project -t transformer`

The following variables should be added to the above (before the `-t` flag)

* input_file: the file to be clipped
  * `--env input_file=<name of file>`
* clip_file: the file containing the spatial boundary to clip the _input_file_ with
  * `--env clip_file=<name of file>`
* output_file: the name to be given to the output file
  * `--env output_file=<name of file>`

