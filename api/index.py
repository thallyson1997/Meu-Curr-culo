import os
import yaml
from flask import Flask, render_template

# Definindo o diretório base para localizar templates e dados corretamente no Vercel
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, '..', 'templates')
static_dir = os.path.join(base_dir, '..', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

def load_data():
    data_path = os.path.join(base_dir, '..', 'data', 'resume.yaml')
    with open(data_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

@app.route('/')
def index():
    resume_data = load_data()
    return render_template('index.html', **resume_data)

# if __name__ == '__main__':
#    app.run(debug=True)
