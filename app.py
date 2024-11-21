from flask import Flask, render_template, request
import requests


all_posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    return render_template('index.html', posts=all_posts)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'POST':
        form_data = request.form
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    post = all_posts[post_id - 1]
    return render_template('post.html', post=post)



if __name__ == '__main__':
    app.run(debug=True)
