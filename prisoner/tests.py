from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


#class PlayerBot(Bot):
#    def play_round(self):
#        yield (pages.Introduction)
#        yield (pages.Decision, {"decision": 'Cooperate'})
#        assert 'Both of you chose to Cooperate' in self.html
#        assert self.player.payoff == Constants.both_cooperate_payoff
#        yield (pages.Results)

class PlayerBot(Bot):
    def play_round(self):
        if self.subsession.round_number == 1:
            yield (pages.Instructions_1)
            yield (pages.Instructions_2)
            yield (pages.Instructions_3)
            if random.uniform(0, 1) > 0.5:
                yield (pages.Decision, {"decision": 'Action 1'})
                yield (pages.Results)
                yield (pages.EndRound)
            else:
                yield (pages.Decision, {"decision": 'Action 2'})
                yield (pages.Results)
                yield (pages.EndRound)

        else:
            if random.uniform(0, 1) > 0.5:
                yield (pages.Decision, {"decision": 'Action 1'})
                yield (pages.Results)
                yield (pages.EndRound)
            else:
                yield (pages.Decision, {"decision": 'Action 2'})
                yield (pages.Results)
                yield (pages.EndRound)