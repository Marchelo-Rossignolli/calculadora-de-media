import numpy as np 


def calculate(list):

    if len(list) != 9 :
        raise ValueError("Lista deve conter 9 números")

    list = np.array(list).reshape((3,3))

    calculations = {}
    
    calculations['media'] = [list.mean(axis=0).tolist(), list.mean(axis=1).tolist(), np.mean(list).tolist()]
    calculations['variancia']= [list.var(axis =0).tolist(),list.var(axis =1).tolist(),np.var(list).tolist()] 
    calculations['desvio_pd'] = [list.std(axis =0).tolist(),list.std(axis =1).tolist(),np.std(list).tolist()]   
    calculations['max'] = [list.max(axis =0).tolist(),list.max(axis =1).tolist(),np.max(list).tolist()] 
    calculations['min']= [list.min(axis =0).tolist(),list.min(axis =1).tolist(),np.min(list).tolist()] 
    calculations['soma'] = [list.sum(axis =0).tolist(),list.sum(axis =1).tolist(),np.sum(list).tolist()]


    return calculations

print(calculate([12, 10, 21, 2000, 11, 0, 7, 17, 69]))