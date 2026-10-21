"""
Exercise M3 — Batch Planning
Build batch_planner.py.

Requirements:
- Accept a total number of jobs and a batch size.
- Calculate the number of batches required.
- Calculate how many jobs remain in the final batch.
- Validate the inputs.
- Include a case where the jobs divide evenly and another where there is a remainder.
Use math.ceil() for the batch count. For the final batch size, think about what remainder arithmetic tells you when division is exact.

"""

import math

def batch_planner(total_jobs,batch_size):


    try:

        total_job = float(total_jobs) 

        size = float(batch_size)

    except ValueError:

        raise TypeError("The totaljobs and batch size shoud be integer")

    if total_job < 0:

        raise ValueError("Total jobs cannot be negative.")

    if size <= 0:

        raise ValueError("Batch size must be greater than zero.")
    
    if total_job == 0:
        return 0, 0

    required_batches = math.ceil(total_job/size)

    remainder = total_job % size

    final_batch = size if remainder == 0 else remainder


    return required_batches, final_batch


 
test_scenarios = [
    # (total_jobs, batch_size, explanation)
    (100, 10, "Evenly divided case"),
    (105, 10, "Case with a remainder"),
    (0, 10,   "Zero jobs edge case"),
    (3, 10,   "Fewer jobs than batch size"),
    ("50", "5", "String conversion test"),
    (-10, 5,  "Invalid negative jobs"),
    (100, 0,  "Invalid zero batch size")
]


for jobs,size,desc  in test_scenarios:

    try:

        batches, last_size = batch_planner(jobs, size)

        print(f"SUCCESS [{desc}]:\n  Inputs: {jobs} jobs, size {size} -> Batches: {batches}, Last Batch Size: {last_size}\n")

    except (TypeError,ValueError) as e:

        print(f"REJECTED [{desc}]:\n  Inputs: {jobs} jobs, size {size} -> Error: {e}\n")








