from datetime import datetime, timedelta
from threading import Timer

x=datetime.today()
y = x.replace(day=x.day, hour=8, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()

def main():
	exec(open("getData.py").read())
	exec(open("postImg.py").read())


t = Timer(secs, main)
t.start()