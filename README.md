# SER_SVM_librosa

Speech Emotion Recognition System using SVM (Support Vector Machine)

Dependencies: (OpenSMILE --> librosa), numpy, sklearn

Corpos: RAVDESS (English, 1500 audios from 24 people)

Train (Features): librosa features sets*
* flatness, zerocr, meanMagnitude, maxMagnitude, meancent, stdcent,
maxcent, stdMagnitude, pitchmean, pitchmax, pitchstd,
pitch_tuning_offset, meanrms, maxrms, stdrms,
mfccs, mfccsstd, mfccmax, chroma, mel, contrast

Result: Accuracy: 56.6%
