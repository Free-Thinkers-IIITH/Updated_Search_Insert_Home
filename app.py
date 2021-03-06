from flask import Flask, render_template,request,url_for
from fetch import fetch_from_db
app = Flask(__name__)

# posts = [
#     {
#         "title": "2020 International Conference on Cyber Security and Protection of Digital Services, Cyber Security 2020, Dublin, Ireland, June 15-19, 2020",
#         "venue": "Cyber Security",
#         "publisher": "IEEE",
#         "year": "2020",
#         "type": "Editorship",
#         "key": "conf/cybersecpods/2020",
#         "ee": "https://ieeexplore.ieee.org/xpl/conhome/9136807/proceeding",
#         "url": "https://dblp.org/rec/conf/cybersecpods/2020"
#     },
#     {
#         "title": "2019 International Conference on Cyber Security and Protection of Digital Services, Cyber Security 2018, Oxford, United Kingdom, June 3-4, 2019",
#         "venue": "Cyber Security",
#         "publisher": "IEEE",
#         "year": "2019",
#         "type": "Editorship",
#         "key": "conf/cybersecpods/2019",
#         "ee": "https://ieeexplore.ieee.org/xpl/conhome/8871248/proceeding",
#         "url": "https://dblp.org/rec/conf/cybersecpods/2019"
#     },
#     {
#         "title": "2018 International Conference on Cyber Security and Protection of Digital Services, Cyber Security 2018, Glasgow, Scotland, United Kingdom, June 11-12, 2018",
#         "venue": "Cyber Security",
#         "publisher": "IEEE",
#         "year": "2018",
#         "type": "Editorship",
#         "key": "conf/cybersecpods/2018",
#         "ee": "https://ieeexplore.ieee.org/xpl/conhome/8537418/proceeding",
#         "url": "https://dblp.org/rec/conf/cybersecpods/2018"
#     },
#     {
#         "title": "Cyber Security and Resiliency Policy Framework",
#         "venue": [
#             "Cyber Security and Resiliency Policy Framework",
#             "NATO Science for Peace and Security Series, D - Information and Communication Security"
#         ],
#         "volume": "38",
#         "publisher": "IOS Press",
#         "year": "2014",
#         "type": "Editorship",
#         "access": "unavailable",
#         "key": "series/natosec/38",
#         "url": "https://dblp.org/rec/series/natosec/38"
#     }
# ]

conferences = [{"publisher": "IEEE"}, {"publisher": "IOS Press"}, {
    "publisher": "IEEE Computer Society"}, {"publisher": "Springer"}]

topics = [{"subject": "Machine Learning"}, {
    "subject": "Cyber Security"}, {"subject": "Internet of things"}]



@app.route('/')
def index():
    return render_template('index.html', theme = 1)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/ans', methods =['POST','GET'])
def login_ans():
    name = request.form['username']
    pwd = request.form['password']
    if name == "sourabh" and pwd == "1234":
        return render_template('ans.html', info="Welcome to organization Page!")
    else:
        return render_template('ans.html', info="Invalid Username/Password")

@app.route('/search', methods=['POST','GET'])
def search():
    query = request.form['search_query']
    #return render_template('ans.html', info=query)
    posts = fetch_from_db(query)
    return render_template('home.html', posts=posts, title="Paper Ranker", theme=1, conferencesList=conferences, topicList=topics)

@app.route("/org_insertion")
def about():
    return render_template('org_insertion.html', theme=1)
    
if __name__ == "__main__":
    app.run(debug=True)

