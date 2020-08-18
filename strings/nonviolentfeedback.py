import argparse

p = argparse.ArgumentParser()
p.add_argument('--string', help='string')
args = p.parse_args()
s = args.string
print(s.replace(s[s.find('not'):s.find('good')+len('good')],'improvable'))
