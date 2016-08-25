

def ParamSpace(self,params,names,signal,logger):
    self.params = params
    self.names = names
    self.stuck = False
    self.score = 0;
    self.logger = logger

    self.indexes = []
    items = []

    for i in xrange(len(params)):
        indexes[i] = 0
        items.append(i)

    self.give_diff  = # check This
    self.signal = signal

    def normed_indexes():

        ni = []
        for i in xrange(len(params)):
            j = indexes[i]/params[i]  # check this
            ni.append(j)
        return ni

    def adjust(increments,random):

        if len(increments) == len(params):
            for i in xrange(len(params)):
                if random == True:
                    indexes[give_diff] += increments[i]   # check this

               check_indexes() # check this

    def check_indexes():
        maxed_sum = 0

        for i in xrange(len(params)):
            if indexes[i] > (len(params[i])-1):
                indexes[i] = (len(params[i])-1):
                maxed_sum += 1

            if indexes[i] < 0:
                indexes[i] = 0

            ni = normed_indexes()

            label = "diff"+ str(i+1)
