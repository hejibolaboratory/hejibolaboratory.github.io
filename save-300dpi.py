import numpy as np 	# import numpy
import pylab as pl		# import pylab interface
fig = pl.figure()
times = np.arange ( 0, 5, 0.01 ) 	# define x-vector
fun  = lambda x : np.cos (20 *x) * np.exp (- pl.absolute(x) )
		# define some function fun (x)
pl.plot ( times, fun(times) ) 	# plot fun (t) vs. t
pl.xlabel ('time' ) 		# creating x-label
pl.ylabel ('position')		# creating y-label
pl.title ( 'damped oscillation') 	# setting the title

fig.set_size_inches(30.,18.)
## ensuare the figure is saved in 300 dpi, high resolution enough for publication purposes.
pl.savefig('/Users/ucdlab/Desktop/Course /Python - 大数据 /清华Python 2022/Graph-matpotlib/300dpi.png', dpi=300)
pl.show()

