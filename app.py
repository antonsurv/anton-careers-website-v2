from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Jakarta, Indonesia',
    'salary': 'Rp. 1.000.000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Bandung, Indonesia',
    'salary': 'Rp. 2.000.000'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Jayapura, Indonesia',
    'salary': 'Rp. 3.000.000'
  },
  {
    'id': 4,
    'title': 'Frontend Engineer',
    'location': 'Wamena, Indonesia',
    'salary': 'Rp. 4.000.000'
  }
]

@app.route("/")
def hello_anton():
    return render_template('home.html',
                           jobs=JOBS,
                          company_name='Anton')

@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)