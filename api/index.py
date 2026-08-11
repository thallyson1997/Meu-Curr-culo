import os
import yaml
from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

def load_data():
    data_path = os.path.join(os.path.dirname(__file__), '../data/resume.yaml')
    with open(data_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

@app.route('/')
def index():
    resume_data = load_data()
    return render_template('index.html', **resume_data)

# if __name__ == '__main__':
#    app.run(debug=True)
