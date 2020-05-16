from flask import Flask,render_template,request
import sqlite3 as sql

app=Flask(__name__)

@app.route('/')
def view():
    return render_template('front.html')

@app.route('/search',methods=["GET","POST"])
def validate():
    if request.method=="POST":
        conn=sql.connect('MOVIE.db')
        data=request.form['list']
        text =request.form['mname']
        if data=="all":
            li=[]
            cur=conn.execute("select * from movie")
            for row in cur:
                l=[]
                for j in row:
                    l.append(j)
                li.append(l)
            return render_template('full.html',res=li)        
        if data=="part":
            q="select * from movie where title = ?"
            param=(str(text),)
            cur=conn.execute(q,param)
            li=[]
            for row in cur:
                l=[]
                for j in row:
                    l.append(j)
                li.append(l)
            return render_template('full.html',res=li)



if __name__ == '__main__':
    app.run(debug=True)
    