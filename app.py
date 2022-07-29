from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler


app = Flask(__name__,template_folder='template')
model = pickle.load(open("Finalised_model.pickle","rb"))

@app.route("/",methods=["GET"])
def Home_page():
    return render_template("index.html")

standard_to = StandardScaler()

@app.route("/predict",methods =["POST"])
def prediction_page():
    if request.method == "POST":
        Pclass = float(request.form["Pclass"])
        Sex = request.form["Sex"]
        if Sex =="male":
            Sex = 0
        else:
            Sex = 1
        Age= float(request.form["Age"])
        SibSp = float(request.form["SibSp"])
        Parch = float(request.form["Parch"])
        Fare = float(request.form["Fare"])

        prediction = model.predict([[Pclass, Sex, Age, SibSp , Parch, Fare]])
        if prediction == 1:
            return render_template("result.html", prediction_texts="Passenger Survived")
        else:
            return render_template("result.html", prediction_texts="Passenger Died")

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)


