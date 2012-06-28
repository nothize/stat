import io
import sys
import re

if len(sys.argv) > 1:
	print(sys.argv[1])
	f = io.open(sys.argv[1])
	
	lines = f.readlines()
	s = "".join(lines).replace("\n", "")
	s = s[s.find("<")+1:s.find("]")].strip()
	s = re.sub("[<>\[\]]", "", s)
	
	lines = s.split(" ")
	
	vs = []
	ps = []
	automatch = []
	i = 0
	for p in lines:
		if len(p) == 0:
			continue
		if p[0] == 'Y':
			automatch.append(i)
			p = p[1:]
#			continue

		line = p.split("-")
		vol = int(line[0].replace(",", ""))
		price = float(line[1])
		vs.append(vol)
		ps.append(price)
		i = i + 1

		print i, price, vol/1000

#	print sum(vs)

	spread = 20
	for i in xrange(len(vs)-spread):
		for j in xrange(i+1,i+spread):
			if i >= 229 and j <= 349:
				if abs(sum(vs[i:j]) - 15040000) < 100000 and abs(sum(ps[i:j])/(j-i) - 0.023) < 0.001:
#					print i, j, (j-i), sum(vs[i:j]), sum(ps[i:j]) / (j-i)
					""
			
		
	print len(vs)