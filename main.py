import subprocess
from os import listdir, getenv, mkdir
from os.path import isfile, join, isdir


def check_output_dir(path):
    """
    Check output directory exists and create if not
    """
    if isdir(path) is False:
        mkdir(path)

    return


# a list of default options
defaults = {
    'process': 're-project',
    'output_crs': '27700'
}

# options to accept where can be limited
options = {
    'process': ['clip', 're-project']
}


# fetch environmental variables if passed
process = getenv('process') # one of: 'clip', 're-project'
if process is None: # grab the default if the var hasn't been passed
    process = defaults['process']

if process not in options['process']:
    # if the set process is not accepted, return error and exit
    exit(2)

# file paths
data_path = '/data'
input_dir = 'inputs'
output_dir = 'outputs'

check_output_dir(join(data_path, output_dir))

# get input file(s)
files = [f for f in listdir(join(data_path, input_dir)) if isfile(join(data_path, input_dir, f))]
print(files)

# run re-project
if process == 're-project':
    """
    Re-project a spatial file into a new projection
    """
    # output crs
    crs_output = getenv('output_crs')
    if crs_output is None: # use default is nothing is passed
        crs_output = defaults['output_crs']

    # check if crs of file is already the output crs or not
    # to add

    # run re-project for any files in the input directory
    for file in files:
        subprocess.run(["ogr2ogr", "-t_srs", "EPSG:%s" %crs_output, "-f", "GPKG", join(data_path, output_dir, file), join(data_path, input_dir, file)])
    print('Completed running re-project')

elif process == 'clip':
    """
    Clip a spatial dataset using another spatial boundary file
    """
    # file to clip
    input_file = getenv('file_to_clip')

    # clip area file
    clip_file = getenv('file_clip_area')

    # output file
    output_file = getenv('file_output')

    # run clip process
    subprocess.run(["ogr2ogr", "-clipsrc", join(data_path, input_dir, clip_file), join(data_path, output_dir, output_file), join(data_path, input_dir, input_file)])

    print('Completed running clip')