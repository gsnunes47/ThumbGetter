from flask import Flask, render_template, redirect
from forms import UrlYoutube

app = Flask(__name__)
app.config["SECRET_KEY"] = "c401f29fac31b7c2972f29d97a4f37c6" 

url = ''
img = ''

@app.route('/', methods=["GET", "POST"])
def homepage():
    form = UrlYoutube()
    if form.validate_on_submit():
        url = str(form.url.data)
        id = url.split('v=')[1]
        #return redirect(f'https://i3.ytimg.com/vi/{id}/maxresdefault.jpg')
    return render_template("home.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
