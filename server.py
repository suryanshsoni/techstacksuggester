from flask import Flask , render_template , send_from_directory
app = Flask(__name__ , static_url_path='')


@app.route('/templates/<path:path>')
def send_sjicstatic_template(path):
    return send_from_directory('templates', path)
@app.route('/img/<path:path>')

def send_sjicstaticimg_template(path):
    return send_from_directory('templates/img', path)



@app.route("/")
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.run('0.0.0.0')
