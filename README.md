# Musical Genre Classification
Musical genre classification with GTZAN dataset
- Data source: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

Notebook 1. [Feature Analysis](https://github.com/jo-cho/genre_classification/blob/main/feature_analysis.ipynb)

Notebook 2. [Machine Learning Classification](https://github.com/jo-cho/genre_classification/blob/main/ml_classification.ipynb)

Notebook 3. [Song Similarity](https://colab.research.google.com/github/jo-cho/Genre_Classification_GTZAN_Dataset/blob/main/song_similarity.ipynb)

---

# Musical Feature Analysis and Genre Classification
## These notebooks
- see how to extract features from audio data (.wav)
- analyze features
- genre classification with three machine learning models: SVM, Random Forest and XGBoost
- interpret the classification results
- compute similarity between songs using different distances: cosine, euclidean, correlation

## What is different from other notebooks using GTZAN dataset?

- models with hyperparameter tuning
- proper train/test split
  - it ensures that the excerpts from same song are not both included in train and test set
  - many notebooks are making this mistake
- interpretation of the results showing misclassified genre pairs
  - is it really misclassified? what if the song has very similar musical characteristics despite its specified genre?

---

- You can also find these notebooks at my Kaggle codes:
  - https://www.kaggle.com/code/jojothepizza/genre-classification-and-musical-features-analysis
  - https://www.kaggle.com/code/jojothepizza/similarity-between-songs-using-audio-features
