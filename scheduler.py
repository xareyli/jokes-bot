from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler()

_started = False

workers = {}


def schedule_task(task_id, fn, once_in, *args):
    global _started

    workers[str(task_id)] = scheduler.add_job(fn, "interval", hours=once_in, args=args)

    if not _started:
        scheduler.start()
        _started = True
