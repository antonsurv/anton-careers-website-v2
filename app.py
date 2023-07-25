from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_anton():
  jobs_list = load_jobs_from_db()
  return render_template('home.html', 
                         jobs=jobs_list,
                         company_name='Anton')

@app.route("/api/jobs")
def list_job():
  jobs_list = load_jobs_from_db()
  return jsonify(jobs_list)

@app.route("/job/<id>")
def show_job(id):
  job = load_jobs_from_db(id)
  return jsonify(job)


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)