m_e = {'m1':(50,0,0,1), 'm2':(0,1,0,2), 'm3':(0,0,50,4), 'm4':(1,50,1,5), 'm5':(30,12,3,9)}
m_p = {'m1':0, 'm2': 0, 'm3':0, 'm4':5, 'm5':10}
s = [100,100,100,10]

def allwords(M, res, lst, n, seuil):
    if max(seuil)<=0 or n==0:
        res.append(lst)
    else:
        lst_s = seuil.copy()
        for m, e in M.items():
            if max(e)==0:
                continue
            seuil = lst_s.copy()
            for i in range(len(seuil)):
                seuil[i]-=e[i]
            temp = lst + [m]
            if min(seuil)<0 and max(seuil)==max(lst_s):
                continue
            res_t = allwords(M, res, temp, n-1, seuil)
            res = res_t
    return res

def calcul_prix(M, p):
    return [sum([p[i] for i in m]) for m in M]

def sort_dict_by_key(x):
    temp = {}
    keys = [k for k in x.keys()]
    keys.sort()
    temp.update({k: x.get(k) for k in keys})
    return temp.copy()