#NOTE: 'render_template' uses jinja. visit jinga documentation to see more about template handling.
from flask import Flask
from flask import request
from flask import render_template                                               #To import the html files.
from flask import jsonify
import json
import psycopg2

app = Flask("Job site")


conn = psycopg2.connect("dbname=naukri")


@app.route("/")
def index():
    cur = conn.cursor()
    cur.execute("select count(*) from job_openings;")                           #query
    no_of_jobs = cur.fetchall()[0][0]                                           #get data
    return render_template("main.html",njobs=no_of_jobs)                        #render



@app.route("/jobs")
def jobs():
    ret = []

    cur = conn.cursor()
    cur.execute("select title,company_name,jd_text from job_openings;")         #query

    jobs_list = cur.fetchall()                                                  #get data

    return render_template("jobslist.html",jobs=jobs_list)                      #render


@app.route("/api")
def api():
    print(request.headers)
    if request.headers.get("appId") !="109":
        return jsonify({"Error":"Need appId to work"})
    else:
        x = {'name':'Dheeraj','language':'python3'}
        return jsonify(x)


@app.route('/home_jsonify')
def home_jsonify():
    Dictionary ={'username':'eduCBA' , 'account':'Premium' , 'validity':'2709 days'}
    return jsonify(Dictionary)


if __name__ == "__main__":                                                      #This is used so that this file can be run as anormal python file instead of 2 extra commands in the command line('export FLASK_APP=form_naukri_db','flask run').
    app.run()                                                                   #if 'app.run(debug=True)' then the debugger mode will be ON while running this file.
