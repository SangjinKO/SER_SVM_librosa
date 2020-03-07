class Config:

    save_model_name = ''

    DATA_PATH = 'E:\EMOTION\RAVDESS_labeled'
    CLASS_LABELS = ("1Neutral", "2Calm","3Happy", "4Sad", "5Angry", "6Fearful", "7Disgust","8Surprised")
    CLASS_LABELS_MAP= {
        '01': '1Neutral',
        '02': '2Calm',
        '03': '3Happy',
        '04': '4Sad',
        '05': '5Angry',
        '06': '6Fearful',
        '07': '7Disgust',
        '08': '8Surprised'
    }

    #Feature
    FEATURE_PATH = 'Features/'

    # librosa
    TRAIN_FEATURE_PATH_LIBROSA = FEATURE_PATH + 'SVM_LIBROSA.p'
    PREDICT_FEATURE_PATH_LIBROSA = FEATURE_PATH + 'SVM_LIBROSA.p'

    # Model
    MODEL_PATH = 'Models/'