"""
Program 4(d) - Mini Project – JSON-based log file analyzer
Source: Python Lab Report
"""

# Mini Project: JSON-based Log File Analyzer
import json

# Sample JSON log file created by the program
logs = [
    {"time": "09:00", "level": "INFO", "service": "auth", "msg": "Login"},
    {"time": "09:05", "level": "ERROR", "service": "pay", "msg": "Fail"},
    {"time": "09:10", "level": "WARNING", "service": "db", "msg": "Slow"},
    {"time": "09:15", "level": "ERROR", "service": "db", "msg": "Lost"},
    {"time": "09:20", "level": "INFO", "service": "auth", "msg": "Exit"},
    {"time": "09:25", "level": "ERROR", "service": "pay", "msg": "Crash"},
]
with open("logs.json", "w") as f:
    json.dump(logs, f, indent=4)

try:
    with open("logs.json", "r") as f:
        data = json.load(f)
    if not data:
        raise ValueError("Log file is empty")   # raise an exception
except (FileNotFoundError, json.JSONDecodeError, ValueError) as error:
    print("Could not analyze logs:", error)
else:
    level_count, errors_by_service = {}, {}
    for entry in data:
        lvl = entry["level"]
        level_count[lvl] = level_count.get(lvl, 0) + 1
        if lvl == "ERROR":
            svc = entry["service"]
            errors_by_service[svc] = errors_by_service.get(svc, 0) + 1

    report = {"total_logs": len(data), "level_count": level_count,
              "errors_by_service": errors_by_service}
    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)               # save the analysis

    print("===== LOG ANALYSIS REPORT =====")
    print(json.dumps(report, indent=4))
    print("\nError messages:")
    for e in data:
        if e["level"] == "ERROR":
            print(f"  [{e['time']}] {e['service']}: {e['msg']}")
finally:
    print("\nAnalysis complete.")
