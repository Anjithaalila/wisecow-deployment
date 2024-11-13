
import psutil

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

with open("system_health.log", "a") as log_file:
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_file.write(f"ALERT: CPU usage is above {CPU_THRESHOLD}%: {cpu_usage}%\n")

    # Check Memory usage
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        log_file.write(f"ALERT: Memory usage is above {MEMORY_THRESHOLD}%: {memory_usage}%\n")

    # Check Disk usage
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        log_file.write(f"ALERT: Disk usage is above {DISK_THRESHOLD}%: {disk_usage}%\n")
