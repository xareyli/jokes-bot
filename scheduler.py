from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler()

_started = False

workers = {}


def schedule_task(task_id, fn, once_in, *args):
    global _started

    workers[str(task_id)] = [scheduler.add_job(fn, "interval", hours=once_in, args=args), fn, args]

    if not _started:
        scheduler.start()
        _started = True


def update_worker_interval(worker_id, new_hours):
    try:
        worker = workers[str(worker_id)]
        worker[0].remove()

        schedule_task(worker_id, worker[1], new_hours, *worker[2])
    except:
        return False
