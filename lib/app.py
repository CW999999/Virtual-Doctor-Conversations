from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BartTokenizer, BartForConditionalGeneration
import torch


app = Flask(__name__)

print("current directory:", os.getcwd())
print("catalogue file:", os.listdir())

# Data loading and preprocessing
data = pd.read_excel('dis dataset(3).xlsx', engine='openpyxl')
tfidf_vectorizer = TfidfVectorizer(max_features=1500)
tfidf_features = tfidf_vectorizer.fit_transform(data['Symptom']).toarray()
model = SentenceTransformer('all-MiniLM-L6-v2')
bert_embeddings = model.encode(data['Symptom'].tolist())
features = np.hstack((tfidf_features, bert_embeddings))

# Clustering and anomaly detection
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(features)
data['Cluster'] = clusters
iso_forest = IsolationForest(random_state=42)
anomalies = iso_forest.fit_predict(features)
data['Anomaly'] = anomalies == -1


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Load BART model and word divider
bart_model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
bart_tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

@app.route('/predict', methods=['POST'])
def predict():
    symptom = request.json['symptom']
    similar_symptoms, similarity_scores = find_similar_symptoms(symptom)
    sorted_indices = np.argsort(similarity_scores)[::-1]  
    similar_symptoms = similar_symptoms.iloc[sorted_indices]
    similarity_scores = similarity_scores[sorted_indices]

    highest_similarity_symptom = similar_symptoms.iloc[0]
    highest_similarity_score = similarity_scores[0]
    highest_similarity_score_percent = highest_similarity_score * 100

    treatment_summary = summarize_treatment(highest_similarity_symptom['Treatment recommendation'])

    # Explicitly creating a sorted dictionary combining similar symptoms with their scores
    symptoms_and_scores = {similar_symptoms.iloc[i]['Disease name']: f"{similarity_scores[i]:.2f}" for i in range(len(similarity_scores))}

    response = {
        "Five diseases with symptoms similar to those you describe and how similar they are": symptoms_and_scores,
        "The disease most similar to the one you described and its probability": f"{highest_similarity_symptom['Disease name']} {highest_similarity_score_percent:.2f}%",
        "Summary of treatment recommendations": treatment_summary,
        "Data clustering and anomaly detection results:": data[['Disease name', 'Cluster', 'Anomaly']].to_dict()
    }
    
    return jsonify(response)



def find_similar_symptoms(input_symptom, n_results=5):
    input_embedding = model.encode([input_symptom])[0]
    input_feature = np.hstack((tfidf_vectorizer.transform([input_symptom]).toarray()[0], input_embedding))
    similarity_scores = cosine_similarity([input_feature], features)[0]
    top_indexes = np.argsort(similarity_scores)[-n_results:]
    return data.iloc[top_indexes], similarity_scores[top_indexes]

def summarize_treatment(treatment_text):
    paragraphs = treatment_text.split("\n")
    input_text = ""
    output_text = ""
    for paragraph in paragraphs:
        if len(input_text) + len(paragraph) < 1024:
            input_text += paragraph + "\n"
        else:
            inputs = bart_tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
            summary_ids = bart_model.generate(inputs['input_ids'], num_beams=5, early_stopping=True)
            output_text += bart_tokenizer.decode(summary_ids[0], skip_special_tokens=True) + "\n"
            input_text = paragraph + "\n"

    if input_text: 
        inputs = bart_tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = bart_model.generate(inputs['input_ids'], num_beams=7, early_stopping=True)
        output_text += bart_tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return output_text.strip()

if __name__ == '__main__':
    app.run(debug=True)

