#!/usr/bin/python3

from input import input
import sys

def part1(lines: list[str]):
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