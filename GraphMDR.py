import sys
import time
import Articles as Art
import word2vecForArticle as w2v
import sentence2vecForArticle as s2v
import SimilarityArticle as sim
sys.path.insert(1, '/path/to/GraphExpansion/mainGE')
sys.path.insert(2, '/path/to/SequenceRetrieval/setup')
sys.path.insert(3, '/path/to/Sub-Questions-Generation/mainSQG')

import mainGE as ge
import setup as sr
import mainSQG as sqg
execfile('mainSQG.py')
# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
count = 0
# Strips the newline sub-question
for line in Lines:
  count += 1
  execfile('mainGE.py')
  execfile('setup.py')
  


