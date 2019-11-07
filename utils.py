import datetime

def tosql(v):
  if v is None:
    return "null"
  elif isinstance(v, bool):
    return 1 if v else 0
  elif isinstance(v, str):
    return "'" + v + "'"
  elif isinstance(v, datetime.datetime):
    return "'" + str(v) + "'::date"
  elif isinstance(v, datetime.date):
    return "'" + str(v) + "'::date"
  elif isinstance(v, datetime.time):
    return "'" + str(v) + "'::time"
  elif callable(v):
    return v.__name__
  else:
    return str(v)
