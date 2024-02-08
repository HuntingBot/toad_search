import golly as g

# Parameters
bx = 16
by = 16
min_lifespan = 200
min_lifespan_dh = 80

# Do not change this
patt_count = 0
meth_count = 0

def random_soup():
	global bx, by
	while 1:
		g.new("Looking for methuselahs...")
		g.select([0, 0, bx, by])
		g.randfill(37)
		run_patt(g.getcells(g.getrect()))


def kill_gliders():
	if g.empty():
		return
	pat = g.getcells(g.getrect())
	glider_phase_1 = 1244187411
	glider_phase_2 = -1688977488
	for i in range(-1, 2):
		for j in range(-1, 2):
			for k in range(-1, 2):
				for l in range(-1, 2):
					# g.warn(' '.join([str(i), str(j), str(k), str(l)]))
					if (i or j) and (not (i and j)) and (k or l) and (not (k and l)) and (not (i and k)) and (not (j and l)):
						newpat = g.transform(pat, 0, 0, i, j, k, l)
						g.addlayer()
						g.setname("Glider-killing")
						g.putcells(newpat)
						g.select([g.getrect()[0], g.getrect()[1], 3, 3])
						#g.warn("a")
						c = g.hash([g.getrect()[0], g.getrect()[1], 3, 3])
						if glider_phase_1 == c or glider_phase_2 == c:
							g.select([g.getrect()[0], g.getrect()[1], 3, 3])
							g.clear(0)
							g.update()
							#g.warn("a")
							newpat = g.getcells(g.getrect())
							for loop in range(3):
								newpat = g.transform(newpat, 0, 0, i, j, k, l)
							g.dellayer()
							g.new("Looking for methuselahs...")
							g.putcells(newpat)
							continue
						#g.warn("a")
						g.dellayer()

def run_patt(patt):
	global patt_count, meth_count, min_lifespan
	g.new("Looking for methuselahs...")
	g.reset()
	g.update()
	patt_count += 1
	#patt = g.parse(known_cells + "!")
	#g.note(known_cells[1:] + "!")
	g.putcells(patt)
	g.update()
	hashlist = {}
	while 1:
		if g.empty():
			if int(g.getgen()) > min_lifespan_dh:
				meth_count += 1
				newlifespan = int(g.getgen())
				g.new("Saving methuselah")
				g.putcells(patt)
				g.save("diehard-" + str(newlifespan) + ".rle", "rle")
				g.update()
				#max_final_pop = newpop
			break
		if g.hash(g.getrect()) in hashlist:
			if hashlist[g.hash(g.getrect())] > min_lifespan:
				meth_count += 1
				newlifespan = hashlist[g.hash(g.getrect())]
				g.new("Saving methuselah")
				g.putcells(patt)
				g.save("methuselah-" + str(newlifespan) + ".rle", "rle")
				g.update()
				#max_final_pop = newpop
			break
		else:
			hashlist[g.hash(g.getrect())] = int(g.getgen())
			g.run(1)
		"""
		except:
			# Pattern dies
			if int(g.getgen()) > min_lifespan:
				meth_count += 1
				newlifespan = int(g.getgen())
				g.new("Saving methuselah")
				g.putcells(patt)
				try:
					g.save("diehard-" + str(newlifespan) + ".rle", "rle")
				except:
					pass
				g.update()
				#max_final_pop = newpop
			break"""
		if int(g.getgen()) % 60 == 59:
			kill_gliders()
	#g.warn(str(hashlist))
	g.show(str(patt_count) + " patterns tested, " + str(meth_count) + " methuselahs found")

g.autoupdate(True)
random_soup()
#run_patt("$3o$2o$o!")
