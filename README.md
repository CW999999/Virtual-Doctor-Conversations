# Virtual Doctor – Conversations

### Project Description

+ Projec title: Virtual Doctor - Conversations
+ Team members
	+ Wenhe Chen
	+ Yawen Zhou

+ Project summary
  + Objective: The main issues addressed by the project are the inefficiencies and high costs associated with traditional medical consultations. Patients often have to wait a long time for a doctor's appointment, which can delay diagnosis and treatment. In addition, the financial burden of medical consultations can be significant. Through the introduction of a remote chat doctor system, this project aims to improve access to medical services, reduce waiting times, and reduce costs, thereby reducing pressure on the traditional medical system. This issue is critical because it directly impacts patient care and health outcomes. Faster and more cost-effective access to diagnosis and treatment can significantly improve patient satisfaction and health management. Furthermore, the current global trend is towards digital health solutions, which makes the project highly relevant and timely.
  + Solution: The solution involves a complex data analysis and symptom diagnosis system built using Python. The main components of the system include:
    + Data preprocessing and feature extraction: Generate features from symptom data using 'TF-IDf Vectorizer' and 'SentenceTransformer'.
    + Clustering and anomaly detection: Use 'KMeans clustering' and 'Isolation Forest' to identify patterns and outliers in the data.
    + Similarity search: Implements cosine similarity to identify diseases whose symptoms are similar to those described by the user.
    + Natural Language Processing (NLP): Use the 'BART model' to generate concise summaries of treatment recommendations based on the most relevant disease matches.
  + Main results and findings: The combination of TF-IDF and BERT embedding can effectively capture the semantic and contextual nuances of symptoms, improving the accuracy of similarity search. Clustering helps identify common patterns in symptom data that can be used to classify patient problems more effectively. Anomaly detection helps identify abnormal or rare symptoms that may indicate a less common disease or an error in data entry. The NLP component provides a clear, concise summary of treatment recommendations, enhancing user understanding and compliance.
  + Future extensions and new applications:
    + Expansion of datasets: The inclusion of more significant, more diverse datasets can improve the accuracy and applicability of the system to a broader range of diseases.
    + Multilingual support: Adding support for multiple languages makes the system accessible to a broader range of users.
    + Integration with real-time data: Linking systems to real-time health monitoring devices enables proactive health management.
    + Custom user profiles: Develop user profiles that store medical records for personalized diagnosis and treatment plans.
    + Deploy as a mobile app: Create a mobile app to increase accessibility and ease of use, ensuring that users can access medical advice on the go.

  
+ Example: When the user types in the chat box: I'm not feeling well and can't go to work or do normal activities. I have a slight fever. I have been coughing with a sore throat and a runny nose. I'm not hungry and I can't eat any food. I seem to have lost my sense of taste and eat without taste. Next, the user needs to click Send to send the message. Our remote virtual doctor will then automatically respond to a comprehensive analysis based on the symptoms described by the user: Five diseases with symptoms similar to those you describe and how similar they are: Catarrh: 0.33, Coronavirus (COVID-19): 0.49, Flu: 0.32, Hay fever: 0.32, Sore throat: 0.36. The disease most similar to the one you described and its probability:  Coronavirus (COVID-19) 49.47%. Summary of treatment recommendations: drink fluids like water to keep yourself hydrated and get plenty of rest. Wear loose,  comfortable clothing – don't try to make yourself too cold. Take over-the-counter medications like paracetamol – always follow the manufacturer's instructions. If the user clicks the FRESH button, all chat history will be cleared.

<div align="center">
  <img src="https://github.com/CW999999/Virtual-Doctor-Conversations/blob/main/figs/Web%20appearance.png" width="400" height="423">
</div>
<div align="center">
  <img src="https://github.com/CW999999/Virtual-Doctor-Conversations/blob/main/figs/Similarity%20Scores%20of%20Similar%20Symptoms%20and%20Diseases.png" width="400" height="320">
</div>

+ How to use: Run the 'python app.py' on the terminal and then open this link http://127.0.0.1:5000 in the local browser.
+ PPT: https://docs.google.com/presentation/d/1BdKhgO89_cjfFRD0iPgPIdvMS3TGQ29WpVZmPpK-DcA/edit?usp=sharing


 This folder is orgarnized as follows.

```
Virtual Doctor–Conversations/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

