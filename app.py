from src.mlproject.logger import logging
from src.mlproject.exception import customException
import sys
from src.mlproject.components.data_ignition import DataIgnition
from src.mlproject.components.data_ignition import DataIgnitionConfi
from src.mlproject.components.data_transformation import DataTransformationConfig
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_tranier import ModelTrainerConfig
from src.mlproject.components.model_tranier import ModelTrainer


if __name__=="__main__":
    logging.info("the execution has started")

    try:
        data_ignition =DataIgnition()
        ##data_ignition= data_ignition.initiate_data_ignition()
        train_data_path,test_data_path = data_ignition.initiate_data_ignition()
        ###data_transformation_confi=DataTransformationConfig()
        data_transformation = DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)


        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        

    except Exception as e:
        logging.info('custom exception')
        raise customException(e,sys)