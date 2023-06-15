# Brain Tumor Classification Repository

This repository contains code and data for the Brain Tumor Classification project. The project aims to develop and evaluate a deep learning model for accurate and efficient detection and classification of brain tumors using computer vision techniques. The model leverages pretrained models such as VGG16, VGG19, and ResNet50, and explores the impact of trainable layers on performance. Additionally, the repository includes data processing utilities to preprocess the input data for model training and evaluation.

## Files

- **new-data-processed:** Processed data for testing the model on new, unseen brain tumor images. Purpose: To evaluate the model's performance on previously unseen data.

- **new-data-raw:** Raw, unprocessed data for testing the model on new brain tumor images. Purpose: To provide the raw input data for preprocessing and subsequent evaluation.

- **original-data:** Original dataset used for training and testing the brain tumor classification model. Purpose: To serve as the initial dataset for model development and evaluation.

- **brain-tumor-classification-new-data.ipynb:** Jupyter Notebook containing code for testing the model on new, unseen brain tumor images. Purpose: To evaluate the model's performance on new data and analyze its effectiveness.

- **brain-tumor-classification-reproduction.ipynb:** Jupyter Notebook containing code for reproducing the brain tumor classification model. Purpose: To validate and reproduce the existing brain tumor classification model implemented by others.

- **brain-tumor-classification-trainable-layers.ipynb:** Jupyter Notebook containing code for evaluating the impact of trainable layers on model performance. Purpose: To study and analyze the effect of varying the number of trainable layers in the model.

- **brain_tumor_classification-ResNet50.ipynb:** Jupyter Notebook implementing the brain tumor classification model using the ResNet50 architecture. Purpose: To explore an alternative deep learning model architecture and compare its performance with other models.

- **brain_tumor_classification_VGG19.ipynb:** Jupyter Notebook implementing the brain tumor classification model using the VGG19 architecture. Purpose: To explore an alternative deep learning model architecture and compare its performance with other models.

- **data_processing.py:** Python module containing utility functions for preprocessing the input data. Purpose: To provide data preprocessing functionality for preparing the input data for model training and evaluation.

The original notebook was created on [Kaggle](https://www.kaggle.com/code/mushfirat/brain-tumor-classification-accuracy-96)
