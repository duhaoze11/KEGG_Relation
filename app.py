from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    gene1 = request.form.get('gene1')
    gene2 = request.form.get('gene2')
    prompt = request.form.get('prompt')
    llms = request.form.getlist('llm')
    return f"Gene 1: {gene1}, Gene 2: {gene2}, Prompt: {prompt}, LLMs: {', '.join(llms)}"

if __name__ == '__main__':
    app.run(debug=True)
