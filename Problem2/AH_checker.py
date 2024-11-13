import requests

# Application URL
APP_URL = "http://localhost:5000"  # Change this to the application's URL

# Check the application status
try:
    response = requests.get(APP_URL)
    if response.status_code == 200:
        with open("app_health.log", "a") as log_file:
            log_file.write("Application is UP\n")
    else:
        with open("app_health.log", "a") as log_file:
            log_file.write("Application is DOWN\n")
except requests.RequestException:
    with open("app_health.log", "a") as log_file:
        log_file.write("Application is DOWN\n")
