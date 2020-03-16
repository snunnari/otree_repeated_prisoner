from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random
import time

class Introduction(Page):
    timeout_seconds = 100

class Instructions_1(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class Instructions_2(Page):

    def vars_for_template(self):
        continuation_chance = int(round(Constants.delta * 100))
        return dict(continuation_chance=continuation_chance, die_threshold_plus_one=continuation_chance+1,)

    def is_displayed(self):
        return self.subsession.round_number == 1

class Instructions_3(Page):
    def vars_for_template(self):
        continuation_chance = int(round(Constants.delta * 100))
        return dict(continuation_chance=continuation_chance, die_threshold_plus_one=continuation_chance+1,)

    def is_displayed(self):
        return self.subsession.round_number == 1

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return {
            'my_decision': me.decision,
            'opponent_decision': opponent.decision,
            'same_choice': me.decision == opponent.decision,
            'both_cooperate': me.decision == "Action 1" and opponent.decision == "Action 1",
            'both_defect': me.decision == "Action 2" and opponent.decision == "Action 2",
            'i_cooperate_he_defects':me.decision == "Action 1" and opponent.decision == "Action 2",
            'i_defect_he_cooperates':me.decision == "Action 2" and opponent.decision == "Action 1",
        }

class EndRound(Page):
    timeout_seconds = 100
    def vars_for_template(self):
        continuation_chance = int(round(Constants.delta * 100))
        if self.subsession.round_number in Constants.last_rounds:
            dieroll = random.randint(continuation_chance+1, 100)
        else:
            dieroll =  random.randint(1, continuation_chance)
        return dict(dieroll=dieroll, continuation_chance=continuation_chance, die_threshold_plus_one=continuation_chance+1,)

    def after_all_players_arrive(self):
        elapsed_time = time.time() - self.session.vars['start_time']
        if Constants.time_limit == True and elapsed_time > Constants.time_limit_seconds and self.subsession.round_number in Constants.last_rounds:
            self.session.vars['alive'] = False

class End(Page):
    def is_displayed(self):
        return self.session.vars['alive'] == False or self.subsession.round_number == Constants.last_round

page_sequence = [
    #Introduction,
    Instructions_1,
    Instructions_2,
    Instructions_3,
    Decision,
    ResultsWaitPage,
    Results,
    EndRound,
    End
]
