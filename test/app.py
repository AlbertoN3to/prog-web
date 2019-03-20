from flask import Flask, request, jsonify , session , redirect ,url_for , escape
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

app.secret_key = 'aishdfuiahisd'
app.run(port=3003)
@app.route('/')
def index():
    if 'username' in session:
        return '''
            <p><h1>Logged in as %s</h1>
            <p><input type=submit value=teste>
            ''' % escape(session['username'])   
    return 'You are not logged in'


@app.route("/query/<queryconta>/abc")
def test(queryconta):
    # if args == "a":
    return jsonify(dict(data=[queryconta]))
    # else:
    #     return "jjjj"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        if verify_password('neto',request.form['password']):
            return redirect(url_for('index'))
        else:
            return '''
        <form method="post">
            <h5>Wrong Login<h5>
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''       
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''   

@auth.verify_password
def verify_password(username, password):
    if username == 'neto' and password == 'teste1':
        return True
    return False

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))    


@app.route('/media',methods=["POST"])
def media():
    if request.method == 'POST':
        input = request.get_json()
        return jsonify({"media":input["n1"]+input["n2"]})
        