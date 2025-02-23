import pandas as pd
import pickle
import os
from sklearn.tree import DecisionTreeClassifier

def load_data(df):
    df = pd.read_csv(df)
    return df

def train_model(X_train, y_train):
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    return model

def save_model(model, model_dir):
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'model.pickle')
    
    with open(model_path, 'wb') as file:  # Use 'file' instead of 'model_path'
        pickle.dump(model, file)
    
    print(f'Model saved at {model_path}')


def main():
    # Load data
    train_path = "/Users/santoshkumar/Data_science/dvc-pipeline-tweet/data/processed/train_bow.csv"
    train_df = load_data(train_path)

    # Split data
    X_train = train_df.drop('label', axis=1)
    y_train = train_df['label']
    print('Data loaded successfully')
    print("X_train shape: ", X_train.shape)

    # Train model
    model = train_model(X_train, y_train)
    print('Model trained successfully')
    save_model(model, 'models')

if __name__ == '__main__':
    main()
        

    
