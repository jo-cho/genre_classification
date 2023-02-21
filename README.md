# Musical Genre Classification

---

# With GTZAN Data

Musical genre classification with GTZAN dataset
- Data source: https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

Notebook 1. [Feature Analysis](https://github.com/jo-cho/genre_classification/blob/main/GTZAN/feature_analysis.ipynb)

Notebook 2. [Machine Learning Classification](https://github.com/jo-cho/genre_classification/blob/main/GTZAN/ml_classification.ipynb)

Notebook 3. [Song Similarity](https://colab.research.google.com/github/jo-cho/genre_classification/blob/main/GTZAN/song_similarity.ipynb)

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

- You can also find these notebooks at my Kaggle codes:
  - https://www.kaggle.com/code/jojothepizza/genre-classification-and-musical-features-analysis
  - https://www.kaggle.com/code/jojothepizza/similarity-between-songs-using-audio-features
  
---

# With FMA Data

Musical genre classification with FMA dataset
- Data source: https://www.kaggle.com/datasets/imsparsh/fma-free-music-archive-small-medium

Notebook 1. [ML Classification](https://github.com/jo-cho/genre_classification/blob/main/FMA/genre_classification_with_fma_data.ipynb)


---


