class Calculator:
    #allowing the class to take in initial data
    def __init__(self, data):
        assert all(isinstance(x, (int, float)) for x in data), "list can only be numbers"
        
        self.data = data
        self.update_stats()
        
#Function to update all of these statistics when it gets data    
    def update_stats(self):
        self.length = len(self.data)
        self.mean = self.calc_mean()
        self.median = self.calc_median()
        self.variance = self.calc_var()
        self.standev = self.calc_std()
    
    def calc_mean(self):
        mean = sum(self.data) / len(self.data)
        return mean
    
    def calc_median(self):
        #self.data.sort()
        if len(self.data) % 2 != 0:
            return self.data[int(len(self.data)/2)]
        elif len(self.data) %2 == 0:
            datum1 = self.data[int((len(self.data))/2)]
            datum2 = self.data[int(((len(self.data))-1 )/2)]
            median = (datum1 + datum2) / 2
            return median
    
    def calc_var(self):
        # get the mean
        n = self.length
        mean = self.mean
        # substract each value from the mean and raise the value power of 2
        variance  = list(map(lambda x: (x-mean)**2/(n-1) ,self.data))
        var_sum = sum(variance)
        return var_sum
    
    def calc_std(self): 
        return self.variance**0.5
    
    def add_data(self, new_data):
        self.data.extend(new_data)  #allows a list to be combined with initial list
        self.update_stats()
        return
    def remove_data(self, index = None):
        del(self.data[index])   # will delete 
        #del(self.data, index)  #disregard, sean's initial recommendation
        self.update_stats()