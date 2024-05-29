#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=F'{Path(__file__).parent.parent.parent.parent}/logs/sys.path_demo.log'
)

import sys

if __name__ == '__main__':

  for arg in sys.path:
    logging.debug(
      f'Argument: {arg}'
    )