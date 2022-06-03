
import colorsys
import numpy as np
import matplotlib.pyplot as plt

#data from National Bureau of Statistics
# http://www.stats.gov.cn/

year=[1970,1980,1990,2000,2010,2020]
add_value={
    'agriculture':[793.3,1359.5,5017.2,14717.4,38430.8,78030.9],
    'industry':[918.1,2204.7,7744.1,45663.7,191626.5,383562.4],
    'service industry':[568.3,1023.4,6111.6,39899.1,182061.9,551973.7]
}
fig,ax=plt.subplots()
fig.subplots_adjust(bottom = 0.1)
fig.subplots_adjust(left = 0.2)
ax.stackplot(year,add_value.values(),
             labels=add_value.keys(),colors=['k','0.8','0.3'])
ax.legend(loc='upper left')
ax.set_title('The added value of the three industries')
ax.set_xlabel('Year')
ax.set_ylabel('The added value(billion)')
plt.savefig('HW5.png',dpi=300)
plt.show()