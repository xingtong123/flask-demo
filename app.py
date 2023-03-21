import sys
from pathlib import Path
from flask import Flask, render_template

# sys.path.append(str(Path(__file__).parent.parent.absolute()))  # 加载backend项目根路径

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("test.html")


if __name__ == "__main__":
    print(app.url_map)
    app.run(host='0.0.0.0', port=5555, debug=True)
