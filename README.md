Fire Weather FWI Prediction:

This project involves building a machine learning model to predict the Fire Weather Index (FWI),
a critical indicator used to assess fire danger in forested areas. The FWI system evaluates fire
risk based on environmental factors such as temperature, humidity, wind speed, and rainfall

🚀 Features
Predicts Fire Weather Index (FWI) based on multiple environmental features.
Handles missing data, feature engineering, and preprocessing for robust predictions.
A user-friendly web interface built with Flask for FWI predictions.
Integrated data visualization for better insights into fire danger levels.



Fire Weather FWI Prediction/
│
├── app.py                     # Main Flask application
├── requirements.txt           # List of dependencies
├── README.md                  # Project documentation
├── templates/
│   ├── home.html              # Main user interface for the application and prdicion \results
│   └── index.html            # Interface
├── static/
│   ├── styles.css             # Custom CSS for UI styling
│   └── images/                # Images and icons for the app
├── models/
│   └── ridge.pkl,scaler.pkl               # Pre-trained machine learning model
├── data/
│   └── Algerian_forest_fires_cleaned_dataset.csv       # Dataset used for model training
├── notebooks/
│   └── Forest Fire EDA.ipynb,modeltraing.ipynb    # Jupyter notebook for data exploration
└── src/
    ├── preprocess.py          # Data preprocessing scripts
    ├── train.py               # Model training script
    └── utils.py               # Utility functions
    
🧑‍💻 How to Use
1. Clone the Repository
[git clone https://github.com/yourusername/fire-weather-fwi-prediction.git]
cd fire-weather-fwi-prediction
2. Install Dependencies
Install all required packages listed in the requirements.txt file:
[pip install -r requirements.txt]
3. Run the Application
Start the Flask web server:
python app.py
Access the application in your browser at: http://127.0.0.1:5000/
if code does not support port:5000 then change port (port==5500)

1. Machine Learning Pipeline
Model Used: [e.g., Linear Regression, Ridge Regression, etc.]
Features:
Temperature (°C)
Relative Humidity (RH)
Wind Speed (Ws)
Rainfall (Rain)
FFMC, DMC, ISI indices
Target Variable: Fire Weather Index (FWI)


3. Web Interface
Users input environmental parameters via a form.
Results are displayed as predicted FWI values.

4. Data Visualization
Jupyter notebooks (notebooks/data_analysis.ipynb) provide exploratory data analysis (EDA), showcasing relationships between features and the target variable.
📊 Dataset
Source: [https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++#]

Description:
Contains historical weather and fire index data.
Includes multiple environmental factors influencing fire risks.

🛠️ Tools & Technologies
Programming Language: Python
Libraries:
Flask for web application
pandas, NumPy for data manipulation
scikit-learn for machine learning
Matplotlib, Seaborn for data visualization
Deployment: Flask local server (future plans for cloud deployment)

🖥️ Screenshots
Home Page
   ![Screenshot (117)](https://github.com/user-attachments/assets/a377635e-4a04-44d4-be18-f04ea0016ff8)
   

🚀 Future Enhancements
Add a real-time weather data integration using APIs.
Deploy the application on a cloud platform like AWS, Azure, or Heroku.
Improve the prediction model by integrating deep learning techniques.
🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (feature/your-feature-name).
Commit your changes and open a pull request.
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

💡 Acknowledgments
[Source Dataset Provider]
Project inspired by real-world forest fire risk management applications.
