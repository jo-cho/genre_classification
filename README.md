# Musical Genre Classification
Musical genre classification with GTZAN dataset
- Data source: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

Notebook 1. [Feature Analysis](https://github.com/jo-cho/genre_classification/blob/main/feature_analysis.ipynb)

Notebook 2. [Machine Learning Classification](https://github.com/jo-cho/genre_classification/blob/main/ml_classification.ipynb)

---

# Musical Feature Analysis and Genre Classification
## These notebooks
- see how to extract features from audio data (.wav)
- analyze features
- genre classification with three machine learning models: SVM, Random Forest and XGBoost
- interpret the results

## What is different from other notebooks?

- models with hyperparameter tuning
- proper train/test split
  - it ensures that the excerpts from same song are not both included in train and test set
  - many notebooks using this data make this mistake
- interpretation of the results showing misclassified genre pairs
  - is it really misclassified? what if the song has very similar musical characteristics despite its specified genre?

---

- You can also find these notebooks at:
  - https://www.kaggle.com/code/jojothepizza/genre-classification-and-musical-features-analysis


