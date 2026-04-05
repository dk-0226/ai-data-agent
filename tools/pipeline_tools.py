import random

def get_failed_jobs():
    return [
        {"job_id":1, "error": "Schema mismatch: expected int but got string"},
        {"job_id":2, "error": "Null values found in NON NULL columns"},
        {"job_id":3, "error": "Out of memory error in Spark job"}
]

def retry_job(job_id):
    return f"Job {job_id} retried successfully!"

def get_logs(job_id):
    logs = {
        1: "Column 'amount' type mismatch",
        2: "Column 'user_id' contains null",
        3: "Executor lost due to memory pressure"
    }
    return logs.get(job_id, "No logs found")


