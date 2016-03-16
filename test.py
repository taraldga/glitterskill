import numpy as np
import matplotlib.pyplot as plt
#create big-expensive-figure
#ioff()      # turn updates off
title('now how much would you pay?')
xticklabels(fontsize=20, color='green')
draw()      # force a draw
savefig('alldone', dpi=300)
close()
ion()      # turn updating back on
plot(rand(20), mfc='g', mec='r', ms=40, mew=4, ls='--', lw=3)