# CKD Prediction System

CKD Prediction System is a Flask-based machine learning web application that predicts the possibility of Chronic Kidney Disease using patient health parameters. The system takes medical inputs such as age, blood pressure, sugar level, pus cell status, pus cell clumps, sodium level, hemoglobin, hypertension, and diabetes mellitus, then uses a trained machine learning model to predict whether the patient may have CKD.

The project uses Python, Flask, Pandas, NumPy, and Scikit-learn. The machine learning model is trained using the `kidney_disease.csv` dataset. The application preprocesses the dataset by handling missing values, cleaning text values, encoding categorical columns, and splitting the data into training and testing sets. Several classifiers are included in the project, such as Support Vector Machine, Decision Tree, Random Forest, Naive Bayes, and K-Nearest Neighbors. The web prediction route uses the Random Forest classifier for prediction.

The application provides a web interface where users can enter patient details and receive a prediction result. It also stores every prediction record in `dataset/records.csv` along with the date and time. An admin user can log in and view saved prediction records through the records page. The project also includes pages for login, diet information, frequently asked questions, prediction results, and record display.

The main file of the project is `server.py`, which handles Flask routes, user login, prediction requests, result rendering, and record display. The `models.py` file contains the machine learning training and classifier logic. The `writeCsv.py` file is used to save prediction records into the CSV file. The `templates` folder contains the HTML pages, while the `static` folder contains CSS, JavaScript, images, and vendor frontend files.

To run the project, install the required packages such as Flask, Pandas, NumPy, and Scikit-learn. After installing the dependencies, start the application by running `python server.py`. The application runs on port `5006`, and it can be opened in the browser using `http://localhost:5006`.

The login system supports two sample users. The patient login uses username `patient` and password `patient`, while the admin login uses username `admin` and password `admin`. The patient can access the prediction form, and the admin can view stored prediction records.

This project is useful for demonstrating how machine learning can be used in healthcare prediction systems. It can be improved further by saving a trained model file, adding stronger authentication, improving form validation, using a database instead of CSV files, adding charts for prediction history, and improving model accuracy with better feature selection and tuning.

This project is for educational purposes only and should not be used as a replacement for professional medical diagnosis.

Developed by Mithun Ravi.
