from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'cable_database.db')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xasibgvt:wVz0PlRqg0nmrFIihLQfeAeuYdeRmYp2@mouse.db.elephantsql.com/xasibgvt'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:BPd8eK2UGK5YaD2gVIow@containers-us-west-105.railway.app:7486/railway'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'


db = SQLAlchemy(app)
class Cable(db.Model):
    __tablename__ = 'cable'
    id = db.Column(db.Integer, primary_key=True)
    family_name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    rca_id = db.Column(db.String, nullable=False)
    email = db.Column(db.String(80), unique=True)
    cable_ID = db.Column(db.String(120), nullable=False)

    def __init__(self, name, email, cable_ID):
        self.name = name
        self.email = email 
        self.cable_ID = cable_ID

class Missing(db.Model):
    # __tablename__ = 'missing'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String, nullable=False)
    cable_ID = db.Column(db.Integer)
    isSolved = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, cable_id, owner, isSolved=False):
        self.cable_ID = cable_id
        self.owner = owner
        self.isSolved = isSolved

with app.app_context():
    db.create_all()
        
# database functions
def query_cable_byName(name):
    # name prep.
    finame = name.split(' ')[0].capitalize()
    fname = name.split(' ')[1:]
    for i in range(len(fname)):
        fname[i] = fname[i].capitalize()
    fname = " ".join(fname)
    print(finame, fname)

    try:
        return Cable.query.filter_by(family_name=finame, first_name=fname).first()
    except Exception as e:
        return 'error ' + str(e)

def query_cable_byRcaId(ID):
    try:
        return Cable.query.filter_by(rca_id=ID).first()
    except Exception as e:
        return 'error ' + str(e)

def query_cable_byCableId(cable_id):
    try:
        return Cable.query.filter_by(cable_ID=cable_id).first()
    except Exception as e:
        return 'error ' + str(e)




def add_missing(cable_id, owner):
    check = Missing.query.filter_by(cable_ID=cable_id, isSolved=False).first()
    if check is None:
        new = Missing(cable_id, owner)
        db.session.add(new)
        db.session.commit()

def update_missing(id):
    missing = Missing.query.get_or_404(id)
    missing.isSolved = True
    db.session.add(missing)
    db.session.commit()
def get_missing():
    data = Missing.query.filter_by(isSolved=False).all()
    print(data)
    if data:
        return data
    else:
        return False

# end
 
@app.route('/')
def home():
    if request.args.get('status'):
        status = request.args.get('status')
    else:
        status = None
    # print(Missing.query.filter_by(cable_ID='dhcdbjc').first())
    # # data = Cable.query.all()
    # # for i in data:
    # #     print(i.family_name, i.first_name, i.rca_id)
    # # print(query_cable_byName('ishimwe mugisha benjamin'))
    # print(query_cable_byRcaId('RCA04053WZN').first_name)
    popup = {
        'status': 'ok',
        'content': None
    }
    if status == 'not-found-query':
        popup['status'] = 'True'
        popup['content'] = {
            'msg1': {
                'text': "we couldn't find what you were looking for, please try again",
                'style': '.bad'
            }
        }
    elif status == 'success-report':
        popup['status'] = 'True'
        popup['content'] = {
            'msg1': {
                'text': "we have successfully reported the missing cable",
                'style': '.good'
            }
        }
    elif status == 'success-notify':
        popup['status'] = 'True'
        popup['content'] = {
            'msg1': {
                'text': "we have successfully notified the owner",
                'style': '.good'
            }
        }



    return render_template('index.html', popup=popup)


@app.route('/query/getcable', methods=['POST'])
def getCable():
    if request.method == 'POST':
        name = request.form.get('name')
        if name[:3] == 'RCA':
            data = query_cable_byRcaId(name)
        else:
            data = query_cable_byName(name)
        if data is not None:
            try:
                if 'error' in data.split(' '):
                    print(data)
                    return redirect(url_for('home'))
                    # go to result page
            except:
                return render_template('index-results-a.html', data=data)
        else:
            return redirect(url_for('home', status='not-found-query'))
            
            
            


@app.route('/query/getowner', methods=['POST'])
def getOwner():
    if request.method == 'POST':
        cable_id = request.form.get('cable_id')
        data = query_cable_byCableId(cable_id)
        if data is not None:
            try:
                if 'error' in data.split(' '):
                    print(data)
                    return redirect(url_for('home'))
                    # go to result page
            except:
                return render_template('index-results-a.html', data=data)
        else:
            return redirect(url_for('home', status='not-found-query'))

            
@app.route('/notify')
def notify_page():
    return render_template('notify-form.html')

@app.route('/notif/resolve', methods=['POST'])
def notify():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        slack = request.form.get('slack')

        return redirect(request.url)
    


@app.route('/missing')
def missing():
    data = get_missing()
    return render_template('missing.html', data=data)


@app.route('/missing/report/<name>/<cable_id>')
def report_missing(name, cable_id,):
    add_missing(name, cable_id)
    return redirect(url_for('home', status='success-report'))


@app.route('/missing/resolve/<id>')
def resolve_missing(id):
    update_missing(id)
    return redirect(url_for('missing'))




            


if __name__ == '__main__':
    app.run(debug=True)