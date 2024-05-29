#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=F'{Path(__file__).parent.parent.parent.parent}/logs/importing_sys_module_demo.log'
)

import sys

if __name__ == '__main__':

  logging.debug(
    f'{type(sys)=}'
  )

  logging.debug(
    f'{type(logging)=}'
  )
  logging.debug(
    F'{logging.__file__=}'
  )
  logging.debug(
    f'{logging.__path__=}'
  )

  logging.debug(
    f'{type(Path)=}'
  )

  try:
    logging.debug(
      f'{Path.__path__=}'
    )
  except AttributeError as attributeError:
    logging.error(
      f'{attributeError=}'
    )