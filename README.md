# Diabetes Prediction Web Application

An AI-powered web application that predicts diabetes risk based on health parameters using machine learning algorithms.

## 🎯 Features

- **Real-time Prediction**: Get instant diabetes risk assessment
- **Beautiful UI**: Modern, responsive design with intuitive user interface
- **High Accuracy**: 85% accuracy with 91.75% recall for diabetic cases
- **Privacy First**: No data storage - all processing is done locally
- **Educational**: Comprehensive information about health parameters and diabetes risk factors

## 🏥 Health Parameters Analyzed

The application analyzes 8 key health parameters:

1. **Number of Pregnancies** - Gestational diabetes risk factor
2. **Glucose Level** - Primary diabetes indicator
3. **Blood Pressure** - Hypertension association
4. **Skin Thickness** - Body fat estimation
5. **Insulin Level** - Glucose processing efficiency
6. **BMI** - Obesity risk factor
7. **Diabetes Pedigree Function** - Family history likelihood
8. **Age** - Age-related risk factor


## 📊 Model Performance

- **Accuracy**: 85.05%
- **Recall (Diabetic Cases)**: 91.75%
- **AUC Score**: 0.9089
- **Precision**: 81% for diabetic cases

## 🛠️ Technical Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: XGBoost, scikit-learn
- **Data Processing**: pandas, numpy
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design principles

## 📁 Project Structure

```
diabetes-prediction/
├── app.py                 # Main Flask application
├── save_model.py          # Script to save trained model
├── diabetes.csv           # Training dataset
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── index.html        # Main prediction page
│   └── about.html        # About page
├── diabetes_model.pkl    # Trained XGBoost model (generated)
├── scaler.pkl           # StandardScaler (generated)
└── pca.pkl              # PCA transformer (generated)
```

## 🔧 Model Details

### Algorithm
- **XGBoost Classifier** with optimized hyperparameters
- **Learning Rate**: 0.05
- **Number of Estimators**: 400
- **Max Depth**: 20
- **Min Child Weight**: 0.4
- **Colsample By Tree**: 0.6

### Preprocessing
- **StandardScaler**: Feature normalization
- **PCA**: Dimensionality reduction (94% variance explained)
- **SMOTETomek**: Class balancing technique

## 🎨 User Interface

The application features a modern, responsive design with:

- **Gradient Background**: Beautiful purple-blue gradient
- **Card-based Layout**: Clean, organized information display
- **Interactive Forms**: Real-time validation and feedback
- **Loading Animations**: Smooth user experience
- **Mobile Responsive**: Works perfectly on all devices

## 🔒 Privacy & Security

- **No Data Storage**: Health data is processed locally and not stored
- **Real-time Processing**: All predictions are made instantly
- **Secure Transmission**: HTTPS-ready for production deployment
- **Privacy First**: No personal information collection

## ⚠️ Important Disclaimer

This tool is designed for **educational and informational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for:

- Proper medical diagnosis and treatment
- Interpretation of your health data
- Personalized medical advice
- Management of diabetes or other health conditions

## 🚀 Deployment
🔧 Local Development
To run the app locally:

bash
```
python app.py
```

## 🌐 Deployment on Render
You can easily deploy this app on Render:

**📦 1. Prerequisites**
Push your project to a GitHub repository

Ensure you have a
```
requirements.txt file
```



**⚙️ 2. Create a Web Service**
Go to Render Dashboard

Click "New Web Service"

Connect your GitHub repo

**🛠️ 3. Configuration**
Set the following:

Setting	Value
Build Command	
```
pip install -r requirements.txt
```
Start Command	
```
gunicorn app:app
```
Environment
```
Python 3.x
```

You can also set environment variables in the "Environment" tab (e.g., API keys, DB URLs).

**🚀 Done!**
Render will:

Install dependencies

Launch your app on a public URL

Automatically redeploy on every push to your repo

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational purposes. Please ensure compliance with local regulations when using for medical applications.

## 📞 Support

For questions or support, please refer to the documentation or create an issue in the repository.

---

**Note**: This application is a demonstration of machine learning in healthcare. Always consult healthcare professionals for medical decisions.

