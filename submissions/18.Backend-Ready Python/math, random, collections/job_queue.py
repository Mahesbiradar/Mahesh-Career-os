"""
Exercise C3 — Background Job Queue
Build job_queue.py.

Requirements:
- Create a queue using deque.
- Add five jobs.
- Process jobs in FIFO order (first in, first out).
- Handle an empty queue without crashing.
- Maintain a history of the last three completed jobs using a bounded deque.
- Print the remaining queue and history after processing.
Distinguish the pending queue from the completed-job history.

"""

from collections import deque


jobs = ["login","order_created","payment_received","email_sent","order_delevered"]


def job_queue(jobs_list):

    pending_queue = deque()

    history_queue = deque(maxlen=3)

    print("--- 1. Adding Jobs to Queue ---")
    for job in jobs_list:
        pending_queue.append(job)
    print(f"Initial Pending Queue: {list(pending_queue)}\n")

    for i in range(5):

        if pending_queue:

            current_job = pending_queue.popleft()

            history_queue.append(current_job)

            print(f"Processed: {current_job} -> Added to History")

    # --- Print Status After Processing ---
    print("\n--- 3. Queue State After Processing ---")
    print(f"Pending Queue: {list(pending_queue)}")
    print(f"Completed Job History  : {list(history_queue)}\n")



    # Try popping one more time from the empty queue to prove it won't crash
    if len(pending_queue) > 0:
        pending_queue.popleft()
    else:
        print("✅ Safe Catch: Queue is completely empty! Aborted .popleft() to prevent application crash.")


job_queue(jobs)
job_queue([])



