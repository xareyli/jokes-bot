from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler()

_started = False


def schedule_task(fn, once_in, *args):
    global _started

    scheduler.add_job(fn, "interval", hours=once_in, args=args)

    if not _started:
        scheduler.start()
        _started = True
