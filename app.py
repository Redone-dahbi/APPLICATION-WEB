from flask import Flask, render_template
from data_analysis import get_data

app = Flask(__name__)
LAYOUT = "layout.html"

@app.route("/")
def get_df():
    return render_template(LAYOUT, table = get_data())


'''
@app.route("/bonjour/<string:name>")
def bonjour(name : str):
    return render_template('base.html',prénom = name)
'''

if __name__ == "__main__":
    app.run(debug = True)