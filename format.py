import datetime
timestamp = 1672531193000 / 1000  # Convert milliseconds to seconds
dt = datetime.datetime.fromtimestamp(timestamp)

# Format the datetime object as a string
formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_date)