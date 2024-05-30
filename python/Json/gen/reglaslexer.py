# Generated from reglaslexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,83,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,2,3,2,32,8,2,1,2,4,2,35,8,2,11,2,12,2,36,1,3,3,3,40,8,3,1,3,
        4,3,43,8,3,11,3,12,3,44,1,3,1,3,4,3,49,8,3,11,3,12,3,50,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,65,8,5,10,5,12,5,68,
        9,5,1,5,1,5,1,6,1,6,1,7,4,7,75,8,7,11,7,12,7,76,1,7,1,7,1,8,1,8,
        1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,0,1,0,4,1,0,48,57,
        2,0,34,34,92,92,3,0,9,10,13,13,32,32,7,0,47,47,92,92,98,98,102,102,
        110,110,114,114,116,116,89,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,
        7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,19,
        1,0,0,0,3,24,1,0,0,0,5,31,1,0,0,0,7,39,1,0,0,0,9,52,1,0,0,0,11,61,
        1,0,0,0,13,71,1,0,0,0,15,74,1,0,0,0,17,80,1,0,0,0,19,20,5,116,0,
        0,20,21,5,114,0,0,21,22,5,117,0,0,22,23,5,101,0,0,23,2,1,0,0,0,24,
        25,5,102,0,0,25,26,5,97,0,0,26,27,5,108,0,0,27,28,5,115,0,0,28,29,
        5,101,0,0,29,4,1,0,0,0,30,32,5,45,0,0,31,30,1,0,0,0,31,32,1,0,0,
        0,32,34,1,0,0,0,33,35,7,0,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,
        1,0,0,0,36,37,1,0,0,0,37,6,1,0,0,0,38,40,5,45,0,0,39,38,1,0,0,0,
        39,40,1,0,0,0,40,42,1,0,0,0,41,43,7,0,0,0,42,41,1,0,0,0,43,44,1,
        0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,48,5,46,0,0,47,
        49,7,0,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,
        0,51,8,1,0,0,0,52,53,7,0,0,0,53,54,6,4,0,0,54,55,5,45,0,0,55,56,
        7,0,0,0,56,57,6,4,1,0,57,58,5,45,0,0,58,59,7,0,0,0,59,60,6,4,2,0,
        60,10,1,0,0,0,61,66,5,34,0,0,62,65,8,1,0,0,63,65,3,17,8,0,64,62,
        1,0,0,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,
        67,69,1,0,0,0,68,66,1,0,0,0,69,70,5,34,0,0,70,12,1,0,0,0,71,72,3,
        11,5,0,72,14,1,0,0,0,73,75,7,2,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,
        74,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,6,7,3,0,79,16,1,0,0,
        0,80,81,5,92,0,0,81,82,7,3,0,0,82,18,1,0,0,0,9,0,31,36,39,44,50,
        64,66,76,4,1,4,0,1,4,1,1,4,2,6,0,0
    ]

class reglaslexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    INT = 3
    FLOAT = 4
    DATE = 5
    STRING = 6
    URL = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "INT", "FLOAT", "DATE", "STRING", "URL", "WS" ]

    ruleNames = [ "TRUE", "FALSE", "INT", "FLOAT", "DATE", "STRING", "URL", 
                  "WS", "ESC" ]

    grammarFileName = "reglaslexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.DATE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def DATE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            4
     

        if actionIndex == 1:
            2
     

        if actionIndex == 2:
            2
     


