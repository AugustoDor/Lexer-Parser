// Generated from C:/Users/jojum/PycharmProjects/Lexer-Parser/python/Json/reglaslexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class reglaslexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		TRUE=1, FALSE=2, INT=3, FLOAT=4, DATE=5, STRING=6, URL=7, WS=8;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"TRUE", "FALSE", "INT", "FLOAT", "DATE", "STRING", "URL", "WS", "ESC"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "TRUE", "FALSE", "INT", "FLOAT", "DATE", "STRING", "URL", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public reglaslexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "reglaslexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 4:
			DATE_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void DATE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			4
			break;
		case 1:
			2
			break;
		case 2:
			2
			break;
		}
	}

	public static final String _serializedATN =
		"\u0004\u0000\bS\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0003\u0002 \b\u0002\u0001\u0002\u0004"+
		"\u0002#\b\u0002\u000b\u0002\f\u0002$\u0001\u0003\u0003\u0003(\b\u0003"+
		"\u0001\u0003\u0004\u0003+\b\u0003\u000b\u0003\f\u0003,\u0001\u0003\u0001"+
		"\u0003\u0004\u00031\b\u0003\u000b\u0003\f\u00032\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005A\b\u0005"+
		"\n\u0005\f\u0005D\t\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0004\u0007K\b\u0007\u000b\u0007\f\u0007L\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0000\u0000\t\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\u0000\u0001"+
		"\u0000\u0004\u0001\u000009\u0002\u0000\"\"\\\\\u0003\u0000\t\n\r\r  \u0007"+
		"\u0000//\\\\bbffnnrrttY\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0001\u0013\u0001\u0000\u0000\u0000\u0003\u0018\u0001\u0000"+
		"\u0000\u0000\u0005\u001f\u0001\u0000\u0000\u0000\u0007\'\u0001\u0000\u0000"+
		"\u0000\t4\u0001\u0000\u0000\u0000\u000b=\u0001\u0000\u0000\u0000\rG\u0001"+
		"\u0000\u0000\u0000\u000fJ\u0001\u0000\u0000\u0000\u0011P\u0001\u0000\u0000"+
		"\u0000\u0013\u0014\u0005t\u0000\u0000\u0014\u0015\u0005r\u0000\u0000\u0015"+
		"\u0016\u0005u\u0000\u0000\u0016\u0017\u0005e\u0000\u0000\u0017\u0002\u0001"+
		"\u0000\u0000\u0000\u0018\u0019\u0005f\u0000\u0000\u0019\u001a\u0005a\u0000"+
		"\u0000\u001a\u001b\u0005l\u0000\u0000\u001b\u001c\u0005s\u0000\u0000\u001c"+
		"\u001d\u0005e\u0000\u0000\u001d\u0004\u0001\u0000\u0000\u0000\u001e \u0005"+
		"-\u0000\u0000\u001f\u001e\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000"+
		"\u0000 \"\u0001\u0000\u0000\u0000!#\u0007\u0000\u0000\u0000\"!\u0001\u0000"+
		"\u0000\u0000#$\u0001\u0000\u0000\u0000$\"\u0001\u0000\u0000\u0000$%\u0001"+
		"\u0000\u0000\u0000%\u0006\u0001\u0000\u0000\u0000&(\u0005-\u0000\u0000"+
		"\'&\u0001\u0000\u0000\u0000\'(\u0001\u0000\u0000\u0000(*\u0001\u0000\u0000"+
		"\u0000)+\u0007\u0000\u0000\u0000*)\u0001\u0000\u0000\u0000+,\u0001\u0000"+
		"\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-.\u0001"+
		"\u0000\u0000\u0000.0\u0005.\u0000\u0000/1\u0007\u0000\u0000\u00000/\u0001"+
		"\u0000\u0000\u000012\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u0000"+
		"23\u0001\u0000\u0000\u00003\b\u0001\u0000\u0000\u000045\u0007\u0000\u0000"+
		"\u000056\u0006\u0004\u0000\u000067\u0005-\u0000\u000078\u0007\u0000\u0000"+
		"\u000089\u0006\u0004\u0001\u00009:\u0005-\u0000\u0000:;\u0007\u0000\u0000"+
		"\u0000;<\u0006\u0004\u0002\u0000<\n\u0001\u0000\u0000\u0000=B\u0005\""+
		"\u0000\u0000>A\b\u0001\u0000\u0000?A\u0003\u0011\b\u0000@>\u0001\u0000"+
		"\u0000\u0000@?\u0001\u0000\u0000\u0000AD\u0001\u0000\u0000\u0000B@\u0001"+
		"\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CE\u0001\u0000\u0000\u0000"+
		"DB\u0001\u0000\u0000\u0000EF\u0005\"\u0000\u0000F\f\u0001\u0000\u0000"+
		"\u0000GH\u0003\u000b\u0005\u0000H\u000e\u0001\u0000\u0000\u0000IK\u0007"+
		"\u0002\u0000\u0000JI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000"+
		"LJ\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000"+
		"\u0000NO\u0006\u0007\u0003\u0000O\u0010\u0001\u0000\u0000\u0000PQ\u0005"+
		"\\\u0000\u0000QR\u0007\u0003\u0000\u0000R\u0012\u0001\u0000\u0000\u0000"+
		"\t\u0000\u001f$\',2@BL\u0004\u0001\u0004\u0000\u0001\u0004\u0001\u0001"+
		"\u0004\u0002\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}