#! /usr/bin/python3.12

from pathlib import Path

import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S.%s",
  filemode='+a',
  filename=F'{Path(__file__).parent.parent.parent.parent}/logs/sys.stdin_demo.log'
)

from typing import Literal

import sys

if __name__ == '__main__':

  print(f'Enter your name: ')
  sample_input_name: Literal[str] = sys.stdin.readline()
  logging.debug(
    F'The name you entered is "{sample_input_name}"'
  )