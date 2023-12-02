from flask import Flask, render_template, request
from db import databasemanager
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/addinfo")
def form():
    return render_template('addinfo.html')

@app.route("/read_form", methods=['POST'] )
def read_form():
    History = databasemanager('history.db')
    History.query("""CREATE TABLE IF NOT EXISTS Histori(
	"id"	INTEGER UNIQUE,
	"name"	text,
	"photo"	text,
    "imlink"	text,
	"linkya"	text,
	"descrip"	text,
	"excurs"	text,
	PRIMARY KEY("id" AUTOINCREMENT)
);""")
    data= request.form
    print(data)
    name =  data['name']
    photo= data['photo']
    imlink = data['imlink']
    linkya = data['linkya']
    descrip= data['descrip']
    excurs = data['excurs']
    place =(name,photo,imlink,linkya,descrip,excurs)
    History.query('''INSERT INTO Histori(name,photo,imlink,linkya,descrip,excurs)VALUES (?,?,?,?,?,?)''',place)
    return render_template('read_form.html')
@app.route("/item")
def item(): 
    try:     
        History = databasemanager('history.db')
        places = History.fetchall("""SELECT * FROM Histori""")
        print(places)
    except:
        places=[("НЕТ ДАННЫХ","НЕТ ДАННЫХ","НЕТ ДАННЫХ")]
    return render_template('item.html',places=places)

@app.route("/getpage<page_id>")
def getpage(page_id): 
    try:     
        History = databasemanager('history.db')
        places = History.fetchall(f"SELECT * FROM Histori WHERE id=={page_id}")
        print(places)
    except:
        return render_template("error.html")    
    return render_template('testpage.html',places=places)

if __name__=="__main__":
    app.run(debug=True)