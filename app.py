from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fruits')
def fruits():  # put application's code here
    fr = ["ვაშლი","მანგო","ავოკადო","მარწყვი"]
    return render_template('index.html',fruits=fruits)

@app.route("/<name>/<int:age>")
def user(name, age):
    return render_template('user.html',name=name, age=age)

@app.route("/admin")
def admin():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
