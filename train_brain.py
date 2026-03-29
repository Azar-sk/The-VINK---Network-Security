import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder
import joblib  # To save the model

def train_detective_model():
    print("🕵️ Loading case files (datasets)...")
    train = pd.read_csv('UNSW_NB15_training-set.csv')
    test = pd.read_csv('UNSW_NB15_testing-set.csv')

    # Drop columns that don't help detection
    drop_cols = ['id', 'attack_cat']
    train = train.drop(columns=drop_cols)
    test = test.drop(columns=drop_cols)

    # Encode categorical text into numbers
    cat_cols = ['proto', 'service', 'state']
    le = LabelEncoder()
    
    for col in cat_cols:
        # We combine both to ensure all possible labels are captured
        combined_data = pd.concat([train[col], test[col]], axis=0).astype(str)
        le.fit(combined_data)
        train[col] = le.transform(train[col].astype(str))
        test[col] = le.transform(test[col].astype(str))

    # Split Features (X) and Target (y)
    X_train = train.drop('label', axis=1)
    y_train = train['label']
    X_test = test.drop('label', axis=1)
    y_test = test['label']

    print("🧠 Training the Brain (XGBoost)... this might take a minute.")
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        use_label_encoder=False,
        eval_metric='logloss'
    )
    
    model.fit(X_train, y_train)

    # Check accuracy
    score = model.score(X_test, y_test)
    print(f"✅ Training Complete! Detection Accuracy: {score:.2%}")

    # Save the 'Brain' and the 'Encoder' for the UI to use later
    joblib.dump(model, 'detective_model.pkl')
    print("💾 Model saved as 'detective_model.pkl'")

if __name__ == "__main__":
    train_detective_model()