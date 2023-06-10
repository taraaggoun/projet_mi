################################### INCLUDES ###################################

import sys
import math
import time
import multiprocessing
import matplotlib.pyplot as plt

sys.path.insert(0, '../algorithmes/')
sys.path.insert(0, '../algorithmes/util/')
import Fermat
import Kraitchik
import generator
import DivisionsSuccessives as ds

############################## PRIVATE FUNCTIONS ##############################

def _tostring(algo):
	if algo == Fermat:
		return "Fermat"
	if algo == Kraitchik:
		return "Crible Quadratique"
	if algo == ds:
		return "Divisions Successives"

def _get_vals(algo, n_tab):
	times = []
	x_tab = []
	for n in n_tab:
		start_time = time.time()
		p = multiprocessing.Process(target=algo.all_divider, args=(n,))
		p.start()
		p.join(5) # attend que le thread fini ou 2sec
		if p.is_alive():
			p.kill()
		else:
			times.append(time.time() - start_time)
			x_tab.append(math.ceil(math.log10(n)))
	return (x_tab, times)

##################################### MAIN #####################################

algos = [Fermat, Kraitchik, ds]
colors = {Kraitchik : 'midnightblue', Fermat : 'darkgreen', ds : 'darkred'}
def main():
	n_tab = []

	min = 2
	max = 2
	for i in range(10):
		min = max
		max = math.pow(10, i+1)
		for i in range(10):
			n_tab.append(generator.generator(min, max))

	for algo in algos:
		(x_tab, y_tab) =_get_vals(algo, n_tab)
		plt.plot(x_tab, y_tab, 'o', label=_tostring(algo), color=colors[algo])
		plt.legend()

	plt.xlabel('nombre de chiffres')
	plt.ylabel('temps en secondes')
	plt.savefig("graphique.png")
	plt.show()
	plt.close()

if __name__ == "__main__": 
    main()

################################################################################
