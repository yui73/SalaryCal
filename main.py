from Income import Income
from cal import calCombine,calSplit,calPro

income = Income([1100,1100,1100,1100,1100,1100,1100,1100,1100,1100,1100,1100],[1100,1100,1100,1100,1100,1100,1100,1100,1100,1100,1100,1100],[0.08,0.02,0.005,0.07],400,5000,1100)
# print(calCombine(income))
# print(calSplit(income))
calPro(income)