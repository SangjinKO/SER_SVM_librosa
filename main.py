import os
import Librosa_Feature #Feature Extraction
from ML_Model import SVM_Model, MLP_Model # SVM, MLP - Train & Evaluate
from Config import Config #File Path

print ("TEST-SVM using librosa for SAVEE")
print ("FEATURE: 21 features including MFCC, pitch, magnitude, etc")


def Train(save_model_name: str):
    Config.save_model_name = save_model_name
    x_train, x_test, y_train, y_test = Librosa_Feature.get_data(Config.DATA_PATH, Config.TRAIN_FEATURE_PATH_LIBROSA, train=True)
    model = SVM_Model()
    model.train(x_train, y_train)
    model.evaluate(x_test, y_test)
    model.save_model(save_model_name)

    return model


## Trainig & Validating
Train("SVM_LIBROSA")

# print("test:", Config.CLASS_LABELS_MAP['01'])