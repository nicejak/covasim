import covasim as cv
import numpy as np

class protect_elderly(cv.Intervention):

    def __init__(self, start_day=None, end_day=None, age_cutoff=70, rel_sus=0.0, *args, **kwargs):
        super().__init__(**kwargs) # NB: This line must be included
        self.start_day   = start_day
        self.end_day     = end_day
        self.age_cutoff  = age_cutoff
        self.rel_sus     = rel_sus
        return

    def initialize(self, sim):
        super().initialize() # NB: This line must also be included
        self.start_day   = sim.day(self.start_day) # Convert string or dateobject dates into an integer number of days
        self.end_day     = sim.day(self.end_day)
        self.days        = [self.start_day, self.end_day]
        self.elderly     = sim.people.age > self.age_cutoff # Find the elderly people here
        self.exposed     = np.zeros(sim.npts) # Initialize results
        self.tvec        = sim.tvec # Copy the time vector into this intervention
        return

    def apply(self, sim):
        self.exposed[sim.t] = sim.people.exposed[self.elderly].sum()

        # Start the intervention
        if sim.t == self.start_day:
            sim.people.rel_sus[self.elderly] = self.rel_sus

        # End the intervention
        elif sim.t == self.end_day:
            sim.people.rel_sus[self.elderly] = 1.0

        return

    def plot(self):
        pl.figure()
        pl.plot(self.tvec, self.exposed)
        pl.xlabel('Day')
        pl.ylabel('Number infected')
        pl.title('Number of elderly people with active COVID')
        return
