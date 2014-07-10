import ptree.test
import matrix_asymmetric.views as views
from matrix_asymmetric.utilities import ParticipantMixIn, ExperimenterMixIn
import random


class ParticipantBot(ParticipantMixIn, ptree.test.ParticipantBot):

    def play(self):

        # random decision
        self.submit(views.Decision, {"decision": random.choice(range(1, 3))})

        #  results
        self.submit(views.Results)


class ExperimenterBot(ExperimenterMixIn, ptree.test.ExperimenterBot):

    def play(self):
        pass