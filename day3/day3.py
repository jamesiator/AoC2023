#!/usr/bin/python3

from input import input
import sys

def part1(lines: list[str]):
  
  def sum_neighboring_numbers(row: int, col: int):
    pass
  
  schematic_sum = 0
  for i in range(lines):
    for j in range(len(lines[i])):
      if lines[i][j] != '.' and not lines[i][j].isdigit():
        schematic_sum += sum_neighboring_numbers(i, j)

  return 0

def part2(lines: list[str]):
  return 0

def main():
  _, part = sys.argv
  lines = input.split('\n')

  if (part == 1):
    print(part1(lines))
  else:
    print(part2(lines))

main()