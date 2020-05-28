from flask import Flask, render_template
import random
app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    broj = random.randint(0,1000)
    return render_template('index.html',broj=broj)

if __name__ == "__main__":
    app.run(debug=True)