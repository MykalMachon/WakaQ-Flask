from flask import Blueprint
from wakaqflask.tasks import add_numbers
from random import randint

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def get_main():
  x = randint(0,9)
  y = randint(0,9)

  add_numbers.delay(x, y)
  return f'adding {x} and {y} together'