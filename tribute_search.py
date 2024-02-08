import golly as g
def is_stable():
 if not g.getrect(): return True
 hsh = g.hash(g.getrect())
 g.duplicate()
 g.run(2)
 if not g.getrect():
  g.dellayer()
  return False
 res = hsh == g.hash(g.getrect())
 g.dellayer()
 return res
def find1():
 x = 1
 while x <= 100000:
  g.run(x)
  if is_stable():
   return x
  x *= 2
def find2(est):
 g.reset()
 x, span = est, 0
 while x:
  g.duplicate()
  g.run(x)
  if not is_stable():
   g.dellayer()
   g.run(x)
   span += x
  else:
   g.dellayer()
  x = x // 2
 return span

import golly as g

# Parameters
bx = 4
by = 3
cells = 114514
min_lifespan = 500

# Do not change this
patt_count = 0
meth_count = 0

def run_patt(known_cells):
 global patt_count, meth_count, min_lifespan
 g.new("Looking for methuselahs...")
 g.reset()
 g.update()
 patt_count += 1
 patt = g.parse(known_cells + "!")
 g.putcells(patt)
 g.update()
 newlifespan = find2(find1())
 #g.note(str(newlifespan))
 if newlifespan > min_lifespan:
  meth_count += 1
  g.new("Saving methuselah")
  g.putcells(patt)
  g.save("methuselah-" + str(newlifespan) + ".rle", "rle")
  g.update()

def dfs(known_cells, depth, cell_count):
	global bx, by
	if cells == cell_count or depth >= bx * by:
		run_patt(known_cells)
		return
	if depth % bx == 0:
		dfs(known_cells + "$b", depth + 1, cell_count)
		dfs(known_cells + "$o", depth + 1, cell_count + 1)
		return
	dfs(known_cells + "b", depth + 1, cell_count)
	dfs(known_cells + "o", depth + 1, cell_count + 1)

g.autoupdate(True)
dfs("3o$3o$3o$3o$3o", 0, 0)
#run_patt("3o$3o$3o$3o$3o!")
