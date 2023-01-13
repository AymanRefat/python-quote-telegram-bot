from helpers import BaseFeature
from . import commands as cmds
from . import queries as qs


class QuotesFeature(BaseFeature):
    commands = [cmds.QuoteCommand]
    queries = [qs.RandomQuoteQuery, qs.TodayQuoteQuery]
