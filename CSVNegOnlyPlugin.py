import sys
#import numpy
#from plugins.CSV2GML.CSV2GMLPlugin import *
from CSV2GML.CSV2GMLPlugin import *



class CSVNegOnlyPlugin(CSV2GMLPlugin):
   def output(self, filename):
      filestuff = open(filename, 'w')
      filestuff.write("name\tweight\n")

      for i in range(self.n):
         self.bacteria[i] = self.bacteria[i].strip()
         if str.isdigit(self.bacteria[i]):
            self.bacteria[i] = 'X' + self.bacteria[i]
      for i in range(self.n):
         for j in range(self.n):
               bac1 = self.bacteria[i].strip()
               bac2 = self.bacteria[j].strip()
               if (bac1[0] == '\"'):
                   bac1 = bac1[1:len(bac1)-1]
                   bac2 = bac2[1:len(bac2)-1]
               if (i != j and float(self.ADJ[i][j]) < 0):
                     filestuff.write(bac1+' '+'('+'pp'+')'+' '+bac2+'\t'+str(self.ADJ[i][j])+'\n')


