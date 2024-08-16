# MBTI Personality Classifier
This project aims to classify personality types based on the MBTI (Myers-Briggs Type Indicator) using an Artificial Neural Network (ANN) implemented in PyTorch. Additionally, various traditional machine learning models were trained and evaluated to compare their performance with the ANN model.

## Project Structure
* model.pth: The trained PyTorch model file for the ANN.
* app.py: The main application script that serves the UI for predicting personality types.
* notebooks: Model_building_checkpoint.ipynb: Jupyter notebook for training and evaluating all machine learning models, including the ANN.
* images/: Contains all the images used in the UI.
## How to Run
1. Clone the Repository

git clone https://github.com/raunakgola/Know-your-personality.git

2. Install Dependencies
Ensure you have Python 3.8+ and pip installed. Install the required libraries:

pip install -r requirements.txt

3. Train the Models (Optional)
If you want to retrain the models or experiment with different configurations, open the train_models.ipynb notebook:

jupyter notebook model_building_checkpoint.ipynb
This notebook includes the code to train and evaluate various models, including the ANN.

4. Run the Application
To start the web application, run:

streamlit run app.py
The app will be available at http://127.0.0.1:5000/ in your web browser.

## Model Performance
Several machine learning models were trained and evaluated for personality classification:

Logistic Regression
Support Vector Machine (SVM)
Decision Tree
K-Nearest Neighbors (KNN)
Naive Bayes
Random Forest
Artificial Neural Network (ANN) [PyTorch]
### Results
The ANN model provided the best overall performance with an accuracy of 95.67% on the test set, capturing the complexity of the MBTI personality classification.
Random Forest and SVM also performed well, with accuracies of 80% and 94.42% respectively, offering simpler yet effective alternatives.
### Conclusion
While traditional machine learning models like Random Forest and SVM offer solid performance, the ANN model, with its ability to capture non-linear patterns in the data, outperforms them in this specific task. The trained ANN model is saved in the model.pth file and is used for predictions in the app.

## UI Design
The UI of the application is simple and user-friendly, allowing users to input text and receive predictions on their MBTI personality type. All images used in the UI are stored in the images folder.
There is a sidebar having question and user just answer by clicking the button in terms of how much you agree with the question.

## Model Architecture
![Screenshot 2024-08-11 172752](https://github.com/user-attachments/assets/d6e8d24c-194f-4185-a283-7767ec74d1f1)


## Application
1. Mental Health and Counseling
Personality classification can also play a role in mental health and counseling. Counselors and therapists can use personality insights to better understand their clients and tailor their approaches to suit individual needs. This application can improve the effectiveness of counseling sessions and contribute to better mental health outcomes.

2. Social Media and Online Communities
In social media and online communities, personality classification can be used to personalize user experiences. For example, social media platforms can recommend content, friends, or groups based on a user's personality type. This personalization can enhance user engagement and satisfaction, leading to a more enjoyable and relevant online experience.

3. Customer Support and Interaction
Companies can use personality classification to improve customer support interactions. By understanding the personality type of a customer, support agents can tailor their communication style to better suit the customer's preferences. This approach can lead to more positive customer experiences and higher satisfaction rates.

