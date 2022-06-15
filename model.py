import covasim as cv
import numpy as np

class opioid(cv.Intervention):

    def __init__(self, parameters, *args, **kwargs):
        super().__init__(**kwargs) # NB: This line must be included
        self.prob_alpha     = parameters['alpha']
        self.prob_beta      = parameters['beta']
        self.prob_gamma     = parameters['gamma']
        self.prob_epsilon   = parameters['epsilon']
        self.prob_theta1    = parameters['theta1']
        self.prob_theta2    = parameters['theta2']
        self.prob_theta3    = parameters['theta3']
        self.prob_xi        = parameters['xi']
        self.prob_nu        = parameters['nu']
        self.prob_sigma     = parameters['sigma']
        return

    def initialize(self, sim):
        super().initialize() # NB: This line must also be included
        self.susceptible_opioid     = np.zeros(sim.npts)
        self.prescription_opioid    = np.zeros(sim.npts)
        self.addicted_opioid        = np.zeros(sim.npts)
        self.heroin_opioid          = np.zeros(sim.npts)
        self.recovered_opioid       = np.zeros(sim.npts)
        self.tvec                   = sim.tvec # Copy the time vector into this intervention
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
