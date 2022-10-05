from wakaqflask.app import create_wakaq
from time import sleep
from random import randint

# create an instance of wakaq
wakaq = create_wakaq()

# create the tasks to be imported in the flask app
@wakaq.task(queue='high-priority', max_retries=5)
def add_numbers(x, y):
  sleep_interval = randint(0,5)
  sleep(sleep_interval)
  print(f"{x} + {y} = {x+y}")
  return