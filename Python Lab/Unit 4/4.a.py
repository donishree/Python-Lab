"""
Program 4(a) - Lab Exercise 1 – Log file reader program
Source: Python Lab Report
"""

# Lab Exercise 1: Log file reader program

# Sample log file created by the program so that it can run on its own
sample_log = [
    "2026-10-23 09:00:01 INFO Server started",
    "2026-10-23 09:05:12 INFO User Asha logged in",
    "2026-10-23 09:10:45 WARNING Disk usage at 85%",
    "2026-10-23 09:15:30 ERROR Database connection failed",
    "2026-10-23 09:20:10 INFO Backup completed",
    "2026-10-23 09:25:55 ERROR File not found: report.pdf",
]
with open("app.log", "w") as file:
    file.write("\n".join(sample_log) + "\n")

try:
    with open("app.log", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error: log file not found.")
else:
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    print("------ LOG FILE CONTENTS ------")
    for number, line in enumerate(lines, start=1):
        print(f"{number}: {line.rstrip()}")
        for level in counts:
            if f" {level} " in line:
                counts[level] += 1

    print("\nTotal log entries:", len(lines))
    for level, total in counts.items():
        print(f"{level:<8}: {total}")

    print("\nERROR lines only:")
    for line in lines:
        if " ERROR " in line:
            print("  ", line.strip())
finally:
    print("\nLog reading finished.")
