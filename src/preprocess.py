import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Get the dataset and preprocess it
def Preprocess_Data():
    # Load dataset
    dataset = pd.read_csv("./Mall_Customers.xls")
    dataset = dataset.drop("CustomerID", axis=1)

    # Define preprocessing for numeric columns
    numeric_features = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    numeric_transformer = MinMaxScaler()

    # Define preprocessing for categorical columns
    categorical_features = ['Genre']
    categorical_transformer = OneHotEncoder(drop='first')

    # Define/join the preprocessors
    preprocessor = ColumnTransformer(
        transformers=[
            ('numeric', numeric_transformer, numeric_features),
            ('categorical', categorical_transformer, categorical_features)
        ]
    )

    # Apply preprocessing
    dataset_processed = preprocessor.fit_transform(dataset)
    dataset_processed = pd.DataFrame(dataset_processed, columns=['Age', 'Annual Income', 'Spending Score', 'Genre_Male'])

    # Return the processed dataset and the original loaded dataset
    return dataset_processed, dataset
