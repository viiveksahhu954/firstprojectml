from src.mlproject.logger import logging
from src.mlproject.exception import customException
import sys
from src.mlproject.components.data_ignition import DataIgnition
from src.mlproject.components.data_ignition import DataIgnitionConfi



if __name__=="__main__":
    logging.info("the execution has started")

    try:
        data_ignition =DataIgnition()
        data_ignition.initiate_data_ignition()

    except Exception as e:
        logging.info('custom exception')
        raise customException(e,sys)