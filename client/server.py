from flask import Flask,render_template
import sqlite3 as sql
from flask.json import jsonify

app=Flask(__name__)

@app.route('/',methods=['GET'])
def alldata():
    conn=sql.connect('demo.db')
    cur=conn.execute("select * from movie")
    li=[]
    for row in cur:
        l=[]
        for j in row:
            l.append(j)
        li.append(l)
    return jsonify({'result':li})

@app.route('/<name>',methods=['GET'])
def findrow(name):
    q="select * from movie where field2= ?" 
    param=(str(name),)
    conn=sql.connect('demo.db')
    cur=conn.execute(q,param)
    print(cur)
    l=[]
    for i in cur:
        li=[]
        for j in i:
            li.append(j)
        l.append(li)
    print(l)
    return jsonify({'result':l})


@app.route('/view')
def view():
    li=[]
    conn=sql.connect('demo.db')
    cur=conn.execute("select * from movie")
    for row in cur:
        l=[]
        for j in row:
            l.append(j)
        li.append(l)
    return render_template('list.html',rows=li)

if __name__ == '__main__':
    app.run(port=4000,debug=True)
