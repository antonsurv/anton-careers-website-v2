from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={
                         "ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                         }
                       }
                      )


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.mappings():
      jobs.append(dict(row))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from jobs where id = :val"),
    val=id)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
    

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))

#   result_dicts = []
#   for row in result.all():
#     result_dicts.append(dict(row._mapping))
  
#   print(result_dicts)

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))

#   result_dicts = []
#   for row in result.mappings():
#     result_dicts.append(dict(row))
  
#   print(result_dicts)

# def load_jobs_from_db(id):
#   with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))

#     result_dicts = []
#     for row in result.all():
#         result_dicts.append(dict(row._mapping))

#     print(result_dicts)