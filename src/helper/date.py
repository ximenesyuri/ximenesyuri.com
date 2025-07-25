from datetime import datetime

def _year():
  return datetime.now().year

def _now():
  return datetime.now().strftime("%Y/%m/%d at %H:%M")
