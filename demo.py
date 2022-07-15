from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuartion
from housing.component.data_transformation import DataTransformation
import os


def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed")
        # data_validation_config = Configuartion().get_data_transformation_config()
        # print(data_validation_config)
        # schema_file_path = r"C:\pyt\ML_Project\config\schema.yaml"
        # file_path = r"C:\pyt\ML_Project\housing\artifact\data_ingestion\2022-07-04-16-05-14\ingested_data\train\housing.csv"

        # df = DataTransformation.load_data(file_path=file_path, schema_file_path= schema_file_path)
        # print(df.columns)


        


    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()