from sensor.pipeline.training_pipeline import start_training_pipeline
from sensor.pipeline.batch_prediction import start_batch_prediction

file_path=(r"F:\aps-fault-detection-1\aps_data.csv")

print(__name__)

if __name__=="__main__":
    
    try:
        output_file=start_batch_prediction(input_file_path=file_path)
        print(output_file)
          
        

    except Exception as e:
        print(e)
