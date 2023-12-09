#!/usr/bin/python3

from input import input
import sys

RED = 'red'
GREEN = 'green'
BLUE = 'blue'

def part1(lines: [str]):
  quantities = {
    RED: 12,
    GREEN: 13,
    BLUE: 14
  }

  def game_id_if_possible(line: str):
    game, reveals = line.split(': ')
    _, game_id = game.split(' ')

    for reveal in reveals.split('; '):
      for color_reveal in reveal.split(', '):
        quantity, color = color_reveal.split(' ')
        if int(quantity) > quantities[color]:
          return 0
        
    return int(game_id)
  
  game_id_sum = 0
  for line in lines:
    game_id_sum += game_id_if_possible(line)

  return game_id_sum

def part2(lines: [str]):
  def game_power(line: str):
    min_quantities = {
      RED: 0,
      GREEN: 0,
      BLUE: 0
    }
    _, reveals = line.split(': ')
    
    for reveal in reveals.split('; '):
      for color_reveal in reveal.split(', '):
        quantity, color = color_reveal.split(' ')
        if int(quantity) > min_quantities[color]: 
          min_quantities[color] = int(quantity)

    return min_quantities[RED] * min_quantities[GREEN] * min_quantities[BLUE]

  game_power_sum = 0
  for line in lines:
    game_power_sum += game_power(line)

  return game_power_sum

def main():
  _, part = sys.argv
  lines = input.split('\n')

  if (int(part) == 1):
    print(part1(lines))
  else:
    print(part2(lines))

main()