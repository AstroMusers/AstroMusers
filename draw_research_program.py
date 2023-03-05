import os
import networkx as nx
import numpy as np

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

'''
Generate a graph of repositories and papers
'''

# future namespace
# nicomedia


typefileplot = 'png'

figr, axis = plt.subplots(figsize=(8, 6))

grap = nx.DiGraph()

grap.add_edges_from([ \
                     ('tdpy', 'lygos'), \
                     ('tdpy', 'miletos'), \
                     ('tdpy', 'pcat'), \
                     ('tdpy', 'ephesos'), \
                     ('tdpy', 'pergamon'), \
                     ('tdpy', 'tdgu'), \
                     ('tdpy', 'assos'), \
                     ('tdpy', 'mergen'), \
                     ('tdpy', 'sardis'), \
                     ('tdpy', 'gordion'), \
                     ('tdpy', 'abydos'), \
                     ('tdpy', 'termessos'), \
                     
                     ('ephesos', 'lygos'), \
                     ('ephesos', 'miletos'), \
                     ('ephesos', 'termessos'), \
                     
                     ('pcat', 'miletos'), \
                     ('pcat', 'lygos'), \
                     
                     ('lygos', 'miletos'), \
                     
                     ('miletos', 'troia'), \
                     ('miletos', 'hattusa'), \
                     ('miletos', 'sardis'), \
                     ('miletos', 'abydos'), \
                     ('miletos', 'termessos'), \
                     
                     ('mergen', 'troia'), \
                     ('mergen', 'hattusa'), \
                     ('mergen', 'tdgu'), \
                     ('mergen', 'sardis'), \
                     ('mergen', 'assos'), \
                     ('mergen', 'gordion'), \
                     
                     ('pergamon', 'troia'), \
                     ('pergamon', 'hattusa'), \
                     ('pergamon', 'tdgu'), \
                     ('pergamon', 'sardis'), \
                     ('pergamon', 'abydos'), \
                    ])

posi = nx.drawing.nx_agraph.graphviz_layout(grap, \
                                            #prog='neato', \
                                            #prog='fdp', \
                                            prog='dot', \
                                            #root='pcat', \
                                           )

nx.draw(grap, posi, \
                    with_labels=True, \
                    node_size=4000, \
                    node_color="none", font_color='firebrick', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))

plt.tight_layout()

pathbase = os.environ['ASTROMUSERS_DATA_PATH'] + '/imag/'
path = pathbase + 'research_program.%s' % typefileplot
print('Writing to %s...' % path)
plt.savefig(path, dpi=300)
plt.close()


# Repositories
figr, axis = plt.subplots(figsize=(6, 6))

grap = nx.DiGraph()

grap.add_edges_from([ \
                     # work in progress 
                     ('Black hole search', 'miletos'), \
                     ('FaintStar', 'ephesos'), \
                     ('Exoplanet search', 'ephesos'), \
                     ('pergamon', 'sardis'), \
                     ('pergamon', 'abydos'), \
                    ])

posi = nx.drawing.nx_agraph.graphviz_layout(grap, \
                                            #prog='neato', \
                                            #prog='fdp', \
                                            prog='dot', \
                                            #root='pcat', \
                                           )

nx.draw(grap, posi, \
                    with_labels=True, \
                    node_size=4000, \
                    node_color="none", font_color='firebrick', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))

plt.tight_layout()

pathbase = os.environ['ASTROMUSERS_DATA_PATH'] + '/imag/'
path = pathbase + 'papers.%s' % typefileplot
print('Writing to %s...' % path)
plt.savefig(path, dpi=300)
plt.close()



# Computing Major at WashU Physics

figr, axis = plt.subplots(figsize=(6, 6))

grap = nx.DiGraph()

grap.add_edges_from([ \
                     # work in progress 
                     ('Fundamentals of Computation (Physics 1xx)', 'Introduction Computational Methods (Physics 2xx)'), \
                     ('Introduction to Computational Methods (Physics 2xx)', 'Programing in Physics (Physics 3xx)'), \
                     ('Introduction to Computational Methods (Physics 2xx)', 'Computational Astrophysics (Physics 4xx)'), \
                     ('Introduction to Computational Methods (Physics 2xx)', 'Statistical Methods (Physics 4xx)'), \
                    ])

posi = nx.drawing.nx_agraph.graphviz_layout(grap, \
                                            #prog='neato', \
                                            #prog='fdp', \
                                            prog='dot', \
                                            #root='pcat', \
                                           )

nx.draw(grap, posi, \
                    with_labels=True, \
                    node_size=4000, \
                    node_color="none", font_color='firebrick', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.2'))

plt.tight_layout()

pathbase = os.environ['ASTROMUSERS_DATA_PATH'] + '/imag/'
path = pathbase + 'computing_major.%s' % typefileplot
print('Writing to %s...' % path)
plt.savefig(path, dpi=300)
plt.close()






