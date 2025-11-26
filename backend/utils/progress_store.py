progress = {}

def set_progress(job_id, value):
    progress[job_id] = value

def get_progress(job_id):
    return progress.get(job_id, 0)
