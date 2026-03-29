import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def prepare_data(file_path):
    df = pd.read_csv(file_path)
    
    # 1. Drop columns that don't help with detection (like 'id')
    if 'id' in df.columns:
        df = df.drop('id', axis=1)
    
    # 2. Handle Categorical Columns: proto, service, state
    # We use LabelEncoding to turn 'tcp' -> 1, 'udp' -> 2, etc.
    categorical_cols = ['proto', 'service', 'state']
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col].astype(str))
        
    # 3. Separate Features (X) and Target (y)
    # 'label' is 0 for Normal, 1 for Attack
    X = df.drop(['label', 'attack_cat'], axis=1)
    y = df['label']
    
    # 4. Scaling: Ensure values like 'duration' and 'bytes' are on the same scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, X.columns

print("Ready to process UNSW-NB15!")