# transformer
A utility tool for transforming spatial data

## Description
A simple tool using Docker and GDAL to support spatial data transforms.

Currently supported transforms (processes):
* clip
* re-projection


## Use
  
Build docker image  
`docker build . -t transformer`

### re-projection
Re-projects any spatial files found in the input directory. The transformed file is saved in the outputs directory with the same file name as the input.

`docker run -v <local path>/transformer/output:/data/outputs --env process=re-project -t transformer`

Default output projection is British National Grid (27700), though output can be specified by using an additional environmental variable:  
`--env output_crs=<EPSG code for chosen crs>`
