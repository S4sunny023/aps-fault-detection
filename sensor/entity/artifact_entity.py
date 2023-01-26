
from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str  

class DataTransformationArtiArtifact:...
class ModelTrainingArtifact:...
class ModelTraiingArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact:...
