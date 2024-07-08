# Introduction
This repo's goal is to create the models used in the project. Each folder represents one model with preprocessing, explanatory analysis of the dataset, model selection, and a script that builds the model.

# Installation
The dependency management is done by Poetry, so it is needed for the whole process.

If you just cloned the project, cd to the ml_scripts_eda folder:

```
cd ml_scripts_eda
```

Run this to create the virtual environment and activate it:
```
poetry install
poetry shell
```

# Datasets

You can find more information and download the datasets that i used to train the models through the links below:

- credit_score_data_1.csv: https://www.kaggle.com/datasets/sujithmandala/credit-score-classification-dataset
- credit_score_data_2.csv: https://www.kaggle.com/datasets/parisrohan/credit-score-classification/data 

Each dataset represents a folder:


credit_score_data_1.csv -> [credit_score_1](./credit_score_1/)

credit_score_data_2.csv -> [credit_score_2](./credit_score_2/)