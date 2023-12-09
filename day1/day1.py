#!/usr/bin/python3

from input import input
import sys
import math

def part1(lines: [str]):

  def get_first_digit(strSequence: str):
    for i in range(len(strSequence)):
      if strSequence[i].isdigit():
        return strSequence[i]
    return 0
      
  def get_last_digit(strSequence: str):
    for i in range(len(strSequence)-1, -1, -1):
      if strSequence[i].isdigit():
        return strSequence[i]
    return 0

  calibration_sum = 0
  for line in lines:
    calibration_sum += int(f'{get_first_digit(line)}{get_last_digit(line)}')

  return calibration_sum

def part2(lines: [str]):
  def get_queries():
    return [
      ('1', 1),
      ('one', 1),
      ('2', 2),
      ('two', 2),
      ('3', 3),
      ('three', 3),
      ('4', 4),
      ('four', 4),
      ('5', 5),
      ('five', 5),
      ('6', 6),
      ('six', 6),
      ('7', 7),
      ('seven', 7),
      ('8', 8),
      ('eight', 8),
      ('9', 9),
      ('nine', 9),
    ]

  def get_first_digit(line: str):
    first_index = math.inf
    first_value = 0

    for substr, value in get_queries():
      index = line.find(substr)
      if index == -1: continue

      if index < first_index:
        first_index = index
        first_value = value

    return first_value
  
  def get_last_digit(line: str):
    last_index = -1
    last_value = 0

    for substr, value in get_queries():
      index = line.rfind(substr)

      if index > last_index:
        last_index = index
        last_value = value

    return last_value

  calibration_sum = 0
  for line in lines:
    calibration_sum += int(f'{get_first_digit(line)}{get_last_digit(line)}')

  return calibration_sum

def main():
  _, part = sys.argv
  lines = input.split('\n')

  if (int(part) == 1):
    print(part1(lines))
  else:
    print(part2(lines))

main()