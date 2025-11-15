from flask import Flask,render_template,request,session
from flask_pymongo import PyMongo
app = Flask(__name__)
app.secret_key = "anyrandomkey"  # required for session

mongodb_client=PyMongo(app,uri="mongodb://localhost:27017/project1")
db=mongodb_client.db

#basic route

@app.route("/")
def h():
   return '''<h1>Welcome</h1>
             <p><a href="/home">home page</p>
          '''
@app.route("/home")
def home():
    username="tharani"
    password="12345"
    return render_template("home.html",username1=username,password1=password)

@app.route("/confim",methods=['POST','GET'])
def reg():
    if request.method == "POST":
        u=request.form.get('uname')
        p=request.form.get('pword')
        session['uname'] = u
        session['pword'] = p
        db.input.insert_many([{
            "name":u,"password1":p
        }])
        return render_template ("conform.html",u=u,p=p)
    

    
@app.route("/login",methods=['POST','GET'])
def log():
    if request.method == "POST":
        u1=request.form.get('uname')
        p1=request.form.get('pword')
        #dynamic data
        u_d = session.get('uname')
        p_d = session.get('pword')

        if u_d == u1 and p_d == p1:
            message="login success"
        else:
            message="login not success"

        return render_template("home.html", message=message )   
            
        

        

@app.route("/index")
def index():
    c=["java","python","c","c++"]
    is_log_in=False
    return render_template("index.html",c_name=c,log=is_log_in)

@app.route("/about")
def a():
    return '<h1>This about computer center and good lock</h1>'

"""
#dynamic routes
1.A variable in the route<variable>.
2.A parameter passed in to the function 
eg:
@app.route('/page/<name>)
def pageMethod(name):
    -----------
    -----------
    -----------
    return ...;
"""

@app.route("/user/<name>")
def u(name):
    f=["apple","orange","banana"]
    p={"dep":"MCA","age":"25","location":"dgl"}
    return render_template("user.html",user_name=name.upper(),f_name=f,p_data=p)
    

if __name__ == '__main__':
    app.run(debug=True)        #find error