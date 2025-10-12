import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

print("Loading local data...")
# Read from our new local CSV file
df = pd.read_csv('imdb_data.csv')

# Separate features (reviews) and target (sentiment)
X = df['review']
y = df['sentiment']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Vectorizing text data...")
# Convert text data into numerical vectors
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("Training the model...")
# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

print(f"Model Accuracy: {model.score(X_test_vec, y_test):.4f}")

print("Saving model and vectorizer...")
# Save the trained model and the vectorizer to disk
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Training complete and artifacts saved.")