
#Implementing Facade Pattern Design
class Facade:
    def operations(self, rate):
        #Aquí van las otras operaciones del CRUD
        mxn = mxn_rate(rate)
        usd = usd_rate(rate)
        jpy = jpy_rate(rate)

        return mxn, usd, jpy
    
    
def mxn_rate(rate):
    return rate['rates']['MXN']
    
def usd_rate(rate):
    return rate['rates']['USD']
    
def jpy_rate(rate):
    return rate['rates']['JPY']