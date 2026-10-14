import os
import time

user = os.environ.get("USER_NAME", "ayesha077")
print(f"=== DevOps Midterm Task Started for {user} ===")
print("System Status: All services are running fine.")

for i in range(1, 4):
    print(f"Processing step {i}...")
    time.sleep(1)

print("=== Task Successfully Completed ===")