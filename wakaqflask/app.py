import sched
from wakaq import WakaQ, Queue
from flask import Flask


def create_wakaq():
  wakaq = WakaQ(
    queues=[(0, 'high-priority'), 'default-priority'],
    host="redis_cache",
    port="6379",
    concurrency="3",
    soft_timeout=180,
    hard_timeout=360,
    max_retries=3,
    max_tasks_per_worker=14,
    schedules=[],
    scheduler_log_file="/app/wakaqflask/logs/scheduler.log",
    worker_log_file="/app/wakaqflask/logs/worker.log"
  )
  return wakaq

def create_flask():
  app = Flask(__name__)

  from wakaqflask.blueprint import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
