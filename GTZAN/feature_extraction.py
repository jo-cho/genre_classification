import pandas as pd
import os
from ftrosa import get_all_musical_features

path = "data/GTZAN_data/genres_original/"

if __name__ == '__main__':
    genre_list = []
    for genre in os.listdir(path):
        genre_list.append(genre)

    wav_list = []
    for g in genre_list:
        genre_path = path + g + '/'
        for wav in os.listdir(genre_path):
            wav_list.append(genre_path + wav)

    df_list = []
    count = 0

    for i in wav_list:
        path_audio = i
        song_name = i.split('/')[-1].split('.wav')[0]

        df_ = get_all_musical_features(
             path_audio,
             song_name,
             start=0,
             chroma_method_list=['cqt'])
        df_list.append(df_)
        count+=1
        if count%5 == 0:
            print(count, 'songs extracted')

    df_features = pd.concat(df_list, axis=1).T

    labels=[]
    for i in df_features.index:
        labels.append(i.split('.')[0])
    df_features['genre_label'] = labels

    df_features.to_csv('data/example_features.csv')