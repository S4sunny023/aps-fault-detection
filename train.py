from sensor.pipeline.training_pipeline import start_training_pipeline


file_path=(r"F:\aps-fault-detection-1\aps_data.csv")
print(__name__)


if __name__=="__main__":
    try:
        start_training_pipeline()
        
    except Exception as e:
        print(e)