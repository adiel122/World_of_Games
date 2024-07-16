from flask import Flask, render_template_string, redirect
import os

app = Flask(__name__)

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

# HTML templates
SUCCESS_HTML = """
<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is <div id="score">{{ score }}</div></h1>
</body>
</html>
"""

ERROR_HTML = """
<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1><div id="score" style="color:red">{{ error }}</div></h1>
</body>
</html>
"""

def read_score():
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                score = file.read().strip()
                return int(score)
        else:
            return 0
    except Exception as e:
        print(f"An error occurred while reading the score: {e}")
        return BAD_RETURN_CODE

@app.route('/')
def index():
    return redirect('/score')

@app.route('/score')
def score_server():
    score = read_score()
    if score == BAD_RETURN_CODE:
        return render_template_string(ERROR_HTML, error="Error reading the score.")
    else:
        return render_template_string(SUCCESS_HTML, score=score)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
