from flask import Flask, render_template
from aip import get_final_output

app = Flask(__name__)

@app.route('/')
def index():
    outputs = get_final_output()
    return render_template('index.html', outputs=outputs)


if __name__ == '__main__':
    app.run(debug=True)
