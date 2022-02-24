import numpy as np
import matplotlib.pyplot as plot

def bar_avg(data, nazwa):
    dane = data.sort_values(by=['avg_income'])
    xy = len(dane['id'])
    plot.bar(x=np.arange(xy), height=dane['avg_income'], align='center')
    if xy == 16:
        labels = dane['Nazwa']
        plot.xticks(np.arange(xy),labels, rotation='vertical')
    plot.ylabel('Avg_Income')
    plot.title(nazwa)
    # fig = plot.gcf()
    # fig.set_size_inches(10, 8)
    plot.show()

def pie_diff(data, nazwa):
     plot.pie(x=(data['Różnica'] > 0).value_counts(), autopct='%1.1f%%')
     plot.title(nazwa)
     plot.legend(loc='lower center', labels=['Większe dochody w 2020', 'Większe dochody w 2019'])
     plot.gcf().set_size_inches(8, 8)
     plot.show()