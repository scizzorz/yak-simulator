from difflib import SequenceMatcher
from pymarkovchain import MarkovChain
import argparse
import sys

def similar(a, b):
  return SequenceMatcher(None, a, b).ratio()

parser = argparse.ArgumentParser(description='Spew some dank memes.')
parser.add_argument('-n', '--num', type=int, default=1,
                    help='Number of memes to spit. 0 is infinite.')
parser.add_argument('-s', '--similarity', type=float, default=1.0,
                    help='Reject memes until they\'re at most this dank.')
parser.add_argument('-l', '--length', type=int, default=0,
                    help='Reject memes until they\'re at least this long.')

args = parser.parse_args()

def mkdb():
  mc = MarkovChain('./markov')
  with open('yaks.txt') as input:
    mc.generateDatabase(input.read())
  with open('yaks.txt') as input:
    yaks = [l.strip() for l in input]
  return mc, yaks

def mkstr(mc, yaks):
  res = mc.generateString()
  sim = 0.0
  for yak in yaks:
    new_sim = similar(res.split(), yak.split())
    if new_sim > sim:
      sim = new_sim

  return res, sim

if args.num > 0:
  mc, yaks = mkdb()
  for x in range(args.num):
    sim = args.similarity
    yak = ''
    while sim >= args.similarity or len(yak.split()) < args.length:
      yak, sim = mkstr(mc, yaks)
    print('{:.2f} {}'.format(sim, yak))
else:
  while True:
    mc, yaks = mkdb()
    sim = args.similarity
    while sim >= args.similarity or len(yak.split()) < args.length:
      yak, sim = mkstr(mc, yaks)
    print('{:.2f} {}'.format(sim, yak))
