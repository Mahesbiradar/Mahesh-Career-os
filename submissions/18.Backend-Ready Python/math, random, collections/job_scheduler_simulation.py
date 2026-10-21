"""
Exercise R2 — Weighted Job Selection
Build job_scheduler_simulation.py.

Requirements:
- Select a job type from normal, priority, and critical.
- Assign different weights to the three job types.
- Simulate at least 1,000 selections.
- Count the occurrences of each type.
- Explain why the observed percentages may differ from the intended proportions.
Use random.choices() and a frequency dictionary. Do not expect exact percentages from a finite random sample.

"""


import random

job_type = ["normal", "priority", "critical"]


total_job_types = list(random.choices(job_type,weights=[2.3,3.7,4],k=1000))


freq_jobs = {}

for choice in total_job_types:

    freq_jobs[choice] = freq_jobs.get(choice,0)+1

print(f"{'Job Type':<10} | {'Count':<5} | {'Actual %':<8} | {'Expected %'}")
print("-" * 45)
print(f"normal     | {freq_jobs.get('normal', 0):<5} | {freq_jobs.get('normal', 0)/10:.1f}%    | 23.0%")
print(f"priority   | {freq_jobs.get('priority', 0):<5} | {freq_jobs.get('priority', 0)/10:.1f}%    | 37.0%")
print(f"critical   | {freq_jobs.get('critical', 0):<5} | {freq_jobs.get('critical', 0)/10:.1f}%    | 40.0%")

    
# explanation: Because random selection involves luck (chance), not exact math.

