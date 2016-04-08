from pymarkovchain import MarkovChain
import argparse
import time
import sys

parser = argparse.ArgumentParser(description='Spew some dank memes.')
parser.add_argument('-n', '--num', type=int, default=1, help='Number of memes to spit. 0 is infinite.')
parser.add_argument('-t', '--time', type=int, default=10, help='Interval to rip memes when looping.')

args = parser.parse_args()

def mkdb():
  mc = MarkovChain('./markov')
  with open('yaks.txt') as input:
    mc.generateDatabase(input.read())
  return mc

if args.num > 0:
  mc = mkdb()
  for x in range(args.num):
    print(mc.generateString())
else:
  while True:
    mc = mkdb()
    print(mc.generateString())
    time.sleep(args.time)
