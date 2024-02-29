from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformationConfig, DataTransformation
import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.Start_data_ingestion()

        datatransformation = DataTransformation()
        datatransformation.initiate_data_transormation(train_data_path, test_data_path)

    except Exception as e:
        logging.info("Zero exception error")
        raise CustomException(e, sys)