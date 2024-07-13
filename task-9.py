"""9.	Using pandas, write a Python function to clean and preprocess a given DataFrame, which involves handling missing values, normalizing numerical columns, and encoding categorical columns."""

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

def clean_and_preprocess(df):
    # Separate features into numerical and categorical
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
    # Define pipelines for numerical and categorical data
    numerical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),  # Handle missing values by replacing with mean
        ('scaler', StandardScaler())  # Normalize numerical columns
    ])
    
    categorical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),  # Handle missing values by replacing with most frequent
        ('onehot', OneHotEncoder(handle_unknown='ignore'))  # Encode categorical columns
    ])
    
    # Combine pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_pipeline, numerical_cols),
            ('cat', categorical_pipeline, categorical_cols)
        ]
    )
    
    # Fit and transform the DataFrame
    df_cleaned = preprocessor.fit_transform(df)
    
    # Get feature names after transformation
    num_feature_names = numerical_cols
    cat_feature_names = preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols)
    
    # Combine all feature names
    feature_names = list(num_feature_names) + list(cat_feature_names)
    
    # Create a new DataFrame with the cleaned data
    df_cleaned = pd.DataFrame(df_cleaned, columns=feature_names)
    
    return df_cleaned

# Example DataFrame
data = {
    'Age': [25, 30, 35, None, 40],
    'Salary': [50000, 60000, None, 80000, 90000],
    'Department': ['HR', 'Finance', 'IT', 'Finance', None],
    'Gender': ['Male', 'Female', None, 'Female', 'Male']
}

df = pd.DataFrame(data)

# Apply the cleaning and preprocessing function
df_cleaned = clean_and_preprocess(df)

# Show the cleaned DataFrame
print(df_cleaned)
