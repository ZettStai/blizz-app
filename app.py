# app.py

from flask import Flask         # import flask
app = Flask(__name__)           # create an app instance

from datetime import datetime

@app.route("/")                 # at the end point /
def timenow():
        my_date = datetime.now()
        return({"date": my_date.isoformat()})

if __name__ == "__main__":      # on running python app.py
        app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))     # run the flask app
