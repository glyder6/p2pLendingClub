import numpy as np

class GrayRelationWeight:
    def __init__(self,rMatrix,wlist):
        self.__matrix = np.swapaxes(rMatrix,0,1)
        self.__wlist = wlist
    
    def getSortList(self):
        indexlist = []
        import copy
        sortlist = copy.deepcopy(self.__grwlist)
        sortlist.sort(reverse = True)
        for _element in self.__grwlist:
            indexlist.append(sortlist.index(_element) + 1)
        return indexlist
    
    def ComputeResult(self):
        self.__grwlist = []
        for col in self.__matrix:
            _grw = 0.0
            for index in range(len(col)):
                _grw += col[index] * self.__wlist[index]  
            self.__grwlist.append(_grw)    
        templist = []
        templist.append(self.__grwlist)
        templist.append(self.getSortList())          
        return templist
    
