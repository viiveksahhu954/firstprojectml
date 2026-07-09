from src.mlproject.logger import logging
from src.mlproject.exception import customException
import sys
from src.mlproject.components.data_ignition import DataIgnition
from src.mlproject.components.data_ignition import DataIgnitionConfi
from src.mlproject.components.data_transformation import DataTransformationConfig
from src.mlproject.components.data_transformation import DataTransformation



if __name__=="__main__":
    logging.info("the execution has started")

    try:
        data_ignition =DataIgnition()
        data_ignition= data_ignition.initiate_data_ignition()
        ##train_data_path,test_data_path = data_ignition.initiate_data_ignition()
        ###data_transformation_confi=DataTransformationConfig()
       ## data_transformation = DataTransformation()
        ##data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    except Exception as e:
        logging.info('custom exception')
        raise customException(e,sys)