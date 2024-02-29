from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_ingestion import DataIngestion
import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.Start_data_ingestion()
    except Exception as e:
        logging.info("Zero exception error")
        raise CustomException(e, sys)