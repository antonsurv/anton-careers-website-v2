from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://prtxbd8xzhxs8z37vp6t:pscale_pw_b8az1K99VwUX5A79pWCcDN42EQEug2glPJCg1V3UJnT@aws.connect.psdb.cloud/antoncareers?charset=utf8mb4"

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
    for row in result.all():
      jobs.append(dict(row))
    return jobs
