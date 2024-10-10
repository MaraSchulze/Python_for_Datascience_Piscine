import datetime

start = datetime.datetime(1970, 1, 1)
now = datetime.datetime.now()

span = now - start
seconds = span.total_seconds()
print(f"Seconds since January 1, 1970: {seconds:,} or {seconds:.2e} in \
scientific notation")
print(now.strftime("%b %d %Y"))
