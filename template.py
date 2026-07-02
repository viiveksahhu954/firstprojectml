import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name= 'mlproject'

list_of_files=[
   f"src/{project_name}/components/__init__.py",
   f"src/{project_name}/components/data_ignition.py" ,
   f"src/{project_name}/components/data_transformation.py", 
   f"src/{project_name}/components/model_tranier.py" ,
   f"src/{project_name}/components/model_monitering.py" ,
   f"src/{project_name}/piplines/__init__.py",
   f"src/{project_name}/piplines/traninig_piplines.py" ,
   f"src/{project_name}/piplines/pridiction_pipline.py" ,
   f"src/{project_name}/exceeption.py" ,
   f"src/{project_name}/logger.py" ,
   f"src/{project_name}/utils.py" ,
    "app.py",
    "dockersfile",
    "requirments.txt",
    "setup.py"




]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir}for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating file empty:{filepath}')


    else:
        logging.info(f"{filename} is already exists")    