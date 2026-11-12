from flask import Flask, request, render_template, flash, redirect, session, abort
from models import Model
from writeCsv import write_to_csv
from datetime import datetime
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('login.html')


@app.route('/diet', methods=['GET'])
def diet():
    return render_template('diet.html')


@app.route('/faq', methods=['GET'])
def faq():
    return render_template('faq.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'patient' and request.form['username'] == 'patient':
        session['logged_in'] = True
        session['role'] = 'patient'
        return render_template('index.html')

    elif request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
        session['role'] = 'admin'
        return redirect('/displayrecords')

    else:
        return render_template('loginerror.html')


@app.route('/displayrecords', methods=['GET'])
def displayrecords():
    if not session.get('logged_in') or session.get('role') != 'admin':
        return redirect('/login')

    records_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'dataset',
        'records.csv'
    )

    df = pd.read_csv(records_path)

    return render_template(
        'displayrecords.html',
        tables=[df.to_html(classes='data', header=True, index=False)]
    )


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    bp = int(request.form['bp'])
    sugar = int(request.form['sugar'])
    pc = int(request.form['pc'])
    pcc = int(request.form['pcc'])
    sodium = int(request.form['sodium'])
    hemo = float(request.form['hemo'])
    htn = int(request.form['htn'])
    db = int(request.form['db'])

    values = [age, bp, sugar, pc, pcc, sodium, hemo, htn, db]

    print(values)

    model = Model()
    classifier = model.randomforest_classifier()
    prediction = classifier.predict([values])

    print(f"Kidney disease = {prediction[0]}")

    time = datetime.now().strftime("%m/%d/%Y (%H:%M:%S)")

    write_to_csv(
        time, age, bp, sugar, pc, pcc,
        sodium, hemo, htn, db, prediction[0]
    )

    return render_template("result.html", result=prediction[0])


@app.route('/health')
def health():
    return "Kidney Disease Prediction Application is Running!"


app.secret_key = os.environ.get(
    'SECRET_KEY',
    'kidney-project-local-secret-key'
)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5006))
    app.run(host='0.0.0.0', port=port, debug=False)