from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     age = request.args.get('age')
     absences = request.args.get('absences')
     health = request.args.get('health')
     studytime = request.args.get('studytime')
     traveltime = request.args.get('traveltime')
     Walc = request.args.get('Walc')
     goout = request.args.get('goout')
     famrel = request.args.get('famrel')

     data = [[age],[absences],[health],[studytime],[traveltime],[Walc],[goout],[famrel]]
     query_df = pd.DataFrame({ 'age' : pd.Series(age) , 'absences' : pd.Series(absences) , 'health' : pd.Series(health) , 'studytime' : pd.Series(studytime) , 'traveltime' : pd.Series(traveltime) , 'Walc' : pd.Series(Walc) , 'goout' : pd.Series(goout) , 'famrel' : pd.Series(famrel)})
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)