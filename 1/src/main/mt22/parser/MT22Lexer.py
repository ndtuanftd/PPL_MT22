# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01bf\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\7\25\u00f3\n\25\f\25\16\25\u00f6\13\25\3\25\5\25\u00f9")
        buf.write("\n\25\3\25\3\25\3\25\5\25\u00fe\n\25\3\25\3\25\3\26\3")
        buf.write("\26\5\26\u0104\n\26\3\26\6\26\u0107\n\26\r\26\16\26\u0108")
        buf.write("\3\27\3\27\3\27\5\27\u010e\n\27\3\27\7\27\u0111\n\27\f")
        buf.write("\27\16\27\u0114\13\27\3\27\5\27\u0117\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0122\n\30\3\31")
        buf.write("\3\31\3\31\3\31\7\31\u0128\n\31\f\31\16\31\u012b\13\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\5\32\u0134\n\32\3")
        buf.write("\33\3\33\5\33\u0138\n\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\78\u017b\n8\f8\168\u017e\138\39\69\u0181\n9\r9\16")
        buf.write("9\u0182\39\39\3:\3:\3:\3:\7:\u018b\n:\f:\16:\u018e\13")
        buf.write(":\3:\3:\3:\3:\3:\3;\3;\3;\3;\7;\u0199\n;\f;\16;\u019c")
        buf.write("\13;\3;\3;\3<\3<\3<\3=\3=\3=\3=\7=\u01a7\n=\f=\16=\u01aa")
        buf.write("\13=\3=\3=\3>\3>\7>\u01b0\n>\f>\16>\u01b3\13>\3>\3>\7")
        buf.write(">\u01b7\n>\f>\16>\u01ba\13>\3>\3>\3?\3?\5\u018c\u01b1")
        buf.write("\u01b8\2@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\2-\27/\30\61\31\63\2\65\2\67\329\33;\34=\35?\36A\37C")
        buf.write(" E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\2m")
        buf.write("\2o\64q\65s\66u\67w8y9{:}\2\3\2\16\4\2GGgg\4\2--//\3\2")
        buf.write("\63;\4\2$$^^\t\2))^^ddhhppttvv\7\2\n\f\16\17$$))^^\3\2")
        buf.write("\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4\2")
        buf.write("\f\f\17\17\n\2$$))^^ddhhppttvv\2\u01cd\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\3\177\3\2\2")
        buf.write("\2\5\u0084\3\2\2\2\7\u008a\3\2\2\2\t\u0092\3\2\2\2\13")
        buf.write("\u0095\3\2\2\2\r\u009b\3\2\2\2\17\u00a0\3\2\2\2\21\u00a4")
        buf.write("\3\2\2\2\23\u00ad\3\2\2\2\25\u00b0\3\2\2\2\27\u00b8\3")
        buf.write("\2\2\2\31\u00bf\3\2\2\2\33\u00c6\3\2\2\2\35\u00cc\3\2")
        buf.write("\2\2\37\u00d1\3\2\2\2!\u00d5\3\2\2\2#\u00de\3\2\2\2%\u00e1")
        buf.write("\3\2\2\2\'\u00e9\3\2\2\2)\u00fd\3\2\2\2+\u0101\3\2\2\2")
        buf.write("-\u0116\3\2\2\2/\u0121\3\2\2\2\61\u0123\3\2\2\2\63\u0133")
        buf.write("\3\2\2\2\65\u0137\3\2\2\2\67\u0139\3\2\2\29\u013b\3\2")
        buf.write("\2\2;\u013d\3\2\2\2=\u013f\3\2\2\2?\u0141\3\2\2\2A\u0143")
        buf.write("\3\2\2\2C\u0145\3\2\2\2E\u0148\3\2\2\2G\u014b\3\2\2\2")
        buf.write("I\u014e\3\2\2\2K\u0151\3\2\2\2M\u0153\3\2\2\2O\u0156\3")
        buf.write("\2\2\2Q\u0158\3\2\2\2S\u015b\3\2\2\2U\u015e\3\2\2\2W\u0160")
        buf.write("\3\2\2\2Y\u0162\3\2\2\2[\u0164\3\2\2\2]\u0166\3\2\2\2")
        buf.write("_\u0168\3\2\2\2a\u016a\3\2\2\2c\u016c\3\2\2\2e\u016e\3")
        buf.write("\2\2\2g\u0170\3\2\2\2i\u0172\3\2\2\2k\u0174\3\2\2\2m\u0176")
        buf.write("\3\2\2\2o\u0178\3\2\2\2q\u0180\3\2\2\2s\u0186\3\2\2\2")
        buf.write("u\u0194\3\2\2\2w\u019f\3\2\2\2y\u01a2\3\2\2\2{\u01ad\3")
        buf.write("\2\2\2}\u01bd\3\2\2\2\177\u0080\7c\2\2\u0080\u0081\7w")
        buf.write("\2\2\u0081\u0082\7v\2\2\u0082\u0083\7q\2\2\u0083\4\3\2")
        buf.write("\2\2\u0084\u0085\7d\2\2\u0085\u0086\7t\2\2\u0086\u0087")
        buf.write("\7g\2\2\u0087\u0088\7c\2\2\u0088\u0089\7m\2\2\u0089\6")
        buf.write("\3\2\2\2\u008a\u008b\7d\2\2\u008b\u008c\7q\2\2\u008c\u008d")
        buf.write("\7q\2\2\u008d\u008e\7n\2\2\u008e\u008f\7g\2\2\u008f\u0090")
        buf.write("\7c\2\2\u0090\u0091\7p\2\2\u0091\b\3\2\2\2\u0092\u0093")
        buf.write("\7f\2\2\u0093\u0094\7q\2\2\u0094\n\3\2\2\2\u0095\u0096")
        buf.write("\7h\2\2\u0096\u0097\7n\2\2\u0097\u0098\7q\2\2\u0098\u0099")
        buf.write("\7c\2\2\u0099\u009a\7v\2\2\u009a\f\3\2\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7n\2\2\u009d\u009e\7u\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\16\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2")
        buf.write("\7q\2\2\u00a2\u00a3\7t\2\2\u00a3\20\3\2\2\2\u00a4\u00a5")
        buf.write("\7h\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8")
        buf.write("\7e\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab")
        buf.write("\7q\2\2\u00ab\u00ac\7p\2\2\u00ac\22\3\2\2\2\u00ad\u00ae")
        buf.write("\7k\2\2\u00ae\u00af\7h\2\2\u00af\24\3\2\2\2\u00b0\u00b1")
        buf.write("\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\u00b5\7i\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7")
        buf.write("\7t\2\2\u00b7\26\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\u00be\7p\2\2\u00be\30\3\2\2\2\u00bf\u00c0")
        buf.write("\7u\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\32")
        buf.write("\3\2\2\2\u00c6\u00c7\7y\2\2\u00c7\u00c8\7j\2\2\u00c8\u00c9")
        buf.write("\7k\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb\7g\2\2\u00cb\34")
        buf.write("\3\2\2\2\u00cc\u00cd\7x\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7k\2\2\u00cf\u00d0\7f\2\2\u00d0\36\3\2\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4\7v\2\2\u00d4 \3")
        buf.write("\2\2\2\u00d5\u00d6\7e\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7k\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd\7g\2\2\u00dd\"")
        buf.write("\3\2\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7h\2\2\u00e0$")
        buf.write("\3\2\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7j\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7v\2\2\u00e8&\3\2\2\2\u00e9\u00ea")
        buf.write("\7c\2\2\u00ea\u00eb\7t\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed")
        buf.write("\7c\2\2\u00ed\u00ee\7{\2\2\u00ee(\3\2\2\2\u00ef\u00f0")
        buf.write("\5-\27\2\u00f0\u00f4\5a\61\2\u00f1\u00f3\5k\66\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3")
        buf.write("\2\2\2\u00f7\u00f9\5+\26\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9")
        buf.write("\3\2\2\2\u00f9\u00fe\3\2\2\2\u00fa\u00fb\5-\27\2\u00fb")
        buf.write("\u00fc\5+\26\2\u00fc\u00fe\3\2\2\2\u00fd\u00ef\3\2\2\2")
        buf.write("\u00fd\u00fa\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\b")
        buf.write("\25\2\2\u0100*\3\2\2\2\u0101\u0103\t\2\2\2\u0102\u0104")
        buf.write("\t\3\2\2\u0103\u0102\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\u0106\3\2\2\2\u0105\u0107\5k\66\2\u0106\u0105\3\2\2\2")
        buf.write("\u0107\u0108\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3")
        buf.write("\2\2\2\u0109,\3\2\2\2\u010a\u0117\5m\67\2\u010b\u0112")
        buf.write("\t\4\2\2\u010c\u010e\7a\2\2\u010d\u010c\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\5k\66\2")
        buf.write("\u0110\u010d\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3")
        buf.write("\2\2\2\u0112\u0113\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0115\u0117\b\27\3\2\u0116\u010a\3\2\2\2\u0116")
        buf.write("\u010b\3\2\2\2\u0117.\3\2\2\2\u0118\u0119\7v\2\2\u0119")
        buf.write("\u011a\7t\2\2\u011a\u011b\7w\2\2\u011b\u0122\7g\2\2\u011c")
        buf.write("\u011d\7h\2\2\u011d\u011e\7c\2\2\u011e\u011f\7n\2\2\u011f")
        buf.write("\u0120\7u\2\2\u0120\u0122\7g\2\2\u0121\u0118\3\2\2\2\u0121")
        buf.write("\u011c\3\2\2\2\u0122\60\3\2\2\2\u0123\u0129\7$\2\2\u0124")
        buf.write("\u0125\7^\2\2\u0125\u0128\13\2\2\2\u0126\u0128\n\5\2\2")
        buf.write("\u0127\u0124\3\2\2\2\u0127\u0126\3\2\2\2\u0128\u012b\3")
        buf.write("\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012c")
        buf.write("\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d\7$\2\2\u012d")
        buf.write("\u012e\b\31\4\2\u012e\62\3\2\2\2\u012f\u0130\7^\2\2\u0130")
        buf.write("\u0134\t\6\2\2\u0131\u0132\7)\2\2\u0132\u0134\7$\2\2\u0133")
        buf.write("\u012f\3\2\2\2\u0133\u0131\3\2\2\2\u0134\64\3\2\2\2\u0135")
        buf.write("\u0138\n\7\2\2\u0136\u0138\5\63\32\2\u0137\u0135\3\2\2")
        buf.write("\2\u0137\u0136\3\2\2\2\u0138\66\3\2\2\2\u0139\u013a\7")
        buf.write("-\2\2\u013a8\3\2\2\2\u013b\u013c\7/\2\2\u013c:\3\2\2\2")
        buf.write("\u013d\u013e\7,\2\2\u013e<\3\2\2\2\u013f\u0140\7\61\2")
        buf.write("\2\u0140>\3\2\2\2\u0141\u0142\7\'\2\2\u0142@\3\2\2\2\u0143")
        buf.write("\u0144\7#\2\2\u0144B\3\2\2\2\u0145\u0146\7(\2\2\u0146")
        buf.write("\u0147\7(\2\2\u0147D\3\2\2\2\u0148\u0149\7~\2\2\u0149")
        buf.write("\u014a\7~\2\2\u014aF\3\2\2\2\u014b\u014c\7?\2\2\u014c")
        buf.write("\u014d\7?\2\2\u014dH\3\2\2\2\u014e\u014f\7#\2\2\u014f")
        buf.write("\u0150\7?\2\2\u0150J\3\2\2\2\u0151\u0152\7>\2\2\u0152")
        buf.write("L\3\2\2\2\u0153\u0154\7>\2\2\u0154\u0155\7?\2\2\u0155")
        buf.write("N\3\2\2\2\u0156\u0157\7@\2\2\u0157P\3\2\2\2\u0158\u0159")
        buf.write("\7@\2\2\u0159\u015a\7?\2\2\u015aR\3\2\2\2\u015b\u015c")
        buf.write("\7<\2\2\u015c\u015d\7<\2\2\u015dT\3\2\2\2\u015e\u015f")
        buf.write("\7*\2\2\u015fV\3\2\2\2\u0160\u0161\7+\2\2\u0161X\3\2\2")
        buf.write("\2\u0162\u0163\7]\2\2\u0163Z\3\2\2\2\u0164\u0165\7_\2")
        buf.write("\2\u0165\\\3\2\2\2\u0166\u0167\7}\2\2\u0167^\3\2\2\2\u0168")
        buf.write("\u0169\7\177\2\2\u0169`\3\2\2\2\u016a\u016b\7\60\2\2\u016b")
        buf.write("b\3\2\2\2\u016c\u016d\7.\2\2\u016dd\3\2\2\2\u016e\u016f")
        buf.write("\7=\2\2\u016ff\3\2\2\2\u0170\u0171\7<\2\2\u0171h\3\2\2")
        buf.write("\2\u0172\u0173\7?\2\2\u0173j\3\2\2\2\u0174\u0175\t\b\2")
        buf.write("\2\u0175l\3\2\2\2\u0176\u0177\7\62\2\2\u0177n\3\2\2\2")
        buf.write("\u0178\u017c\t\t\2\2\u0179\u017b\t\n\2\2\u017a\u0179\3")
        buf.write("\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017dp\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0181")
        buf.write("\t\13\2\2\u0180\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0185\b9\5\2\u0185r\3\2\2\2\u0186\u0187\7\61\2")
        buf.write("\2\u0187\u0188\7,\2\2\u0188\u018c\3\2\2\2\u0189\u018b")
        buf.write("\13\2\2\2\u018a\u0189\3\2\2\2\u018b\u018e\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018f\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018f\u0190\7,\2\2\u0190\u0191\7")
        buf.write("\61\2\2\u0191\u0192\3\2\2\2\u0192\u0193\b:\5\2\u0193t")
        buf.write("\3\2\2\2\u0194\u0195\7\61\2\2\u0195\u0196\7\61\2\2\u0196")
        buf.write("\u019a\3\2\2\2\u0197\u0199\n\f\2\2\u0198\u0197\3\2\2\2")
        buf.write("\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019b\u019d\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e")
        buf.write("\b;\5\2\u019ev\3\2\2\2\u019f\u01a0\13\2\2\2\u01a0\u01a1")
        buf.write("\b<\6\2\u01a1x\3\2\2\2\u01a2\u01a8\7$\2\2\u01a3\u01a4")
        buf.write("\7^\2\2\u01a4\u01a7\t\r\2\2\u01a5\u01a7\n\7\2\2\u01a6")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2")
        buf.write("\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3")
        buf.write("\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\b=\7\2\u01acz\3")
        buf.write("\2\2\2\u01ad\u01b1\7$\2\2\u01ae\u01b0\13\2\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b4\u01b8\5}?\2\u01b5\u01b7\13\2\2\2\u01b6\u01b5\3")
        buf.write("\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb")
        buf.write("\u01bc\b>\b\2\u01bc|\3\2\2\2\u01bd\u01be\t\7\2\2\u01be")
        buf.write("~\3\2\2\2\30\2\u00f4\u00f8\u00fd\u0103\u0108\u010d\u0112")
        buf.write("\u0116\u0121\u0127\u0129\u0133\u0137\u017c\u0182\u018c")
        buf.write("\u019a\u01a6\u01a8\u01b1\u01b8\t\3\25\2\3\27\3\3\31\4")
        buf.write("\b\2\2\3<\5\3=\6\3>\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    FLOAT = 5
    ELSE = 6
    FOR = 7
    FUNCTION = 8
    IF = 9
    INT = 10
    RETURN = 11
    STRING = 12
    WHILE = 13
    VOID = 14
    OUT = 15
    CONTINUE = 16
    OF = 17
    INHERIT = 18
    ARRAY = 19
    FLOATLIT = 20
    INTLIT = 21
    BOOLLIT = 22
    STRINGLIT = 23
    ADDOP = 24
    SUBOP = 25
    MULOP = 26
    DIVOP = 27
    MODOP = 28
    NEGOP = 29
    ANDOP = 30
    OROP = 31
    EQOP = 32
    NEQOP = 33
    LTOP = 34
    LEOP = 35
    GTOP = 36
    GEOP = 37
    STRINGCONCAT = 38
    LB = 39
    RB = 40
    LSB = 41
    RSB = 42
    LCB = 43
    RCB = 44
    DOT = 45
    COMMA = 46
    SM = 47
    COLON = 48
    ASSIGN = 49
    ID = 50
    WS = 51
    BLOCKCOMMENT = 52
    LINECOMMENT = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'float'", "'else'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", 
            "':'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "FLOAT", "ELSE", "FOR", "FUNCTION", 
            "IF", "INT", "RETURN", "STRING", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "FLOATLIT", "INTLIT", "BOOLLIT", "STRINGLIT", 
            "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NEGOP", "ANDOP", 
            "OROP", "EQOP", "NEQOP", "LTOP", "LEOP", "GTOP", "GEOP", "STRINGCONCAT", 
            "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "SM", 
            "COLON", "ASSIGN", "ID", "WS", "BLOCKCOMMENT", "LINECOMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "FLOAT", "ELSE", "FOR", 
                  "FUNCTION", "IF", "INT", "RETURN", "STRING", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "FLOATLIT", 
                  "EXPORNENT", "INTLIT", "BOOLLIT", "STRINGLIT", "ESC_SEQ", 
                  "SUB_STRING", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                  "NEGOP", "ANDOP", "OROP", "EQOP", "NEQOP", "LTOP", "LEOP", 
                  "GTOP", "GEOP", "STRINGCONCAT", "LB", "RB", "LSB", "RSB", 
                  "LCB", "RCB", "DOT", "COMMA", "SM", "COLON", "ASSIGN", 
                  "DIGIT", "ZERO", "ID", "WS", "BLOCKCOMMENT", "LINECOMMENT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[19] = self.FLOATLIT_action 
            actions[21] = self.INTLIT_action 
            actions[23] = self.STRINGLIT_action 
            actions[58] = self.ERROR_CHAR_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    self.text = self.text.replace('_', '')
                
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    self.text = self.text.replace('_', '')
                
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    self.text = self.text[1:-1]
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    self.text = self.text[1:]
                    raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                    self.text = self.text[1:]
                    raise IllegalEscape(self.text)
                
     


