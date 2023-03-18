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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0253\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\6\2\u009b\n\2\r\2\16\2\u009c\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$")
        buf.write("\3$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38")
        buf.write("\38\38\38\38\38\38\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\5>\u01d0\n>\3?\3?\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\5@\u01db\n@\3@\3@\3@\3@\7@\u01e1\n")
        buf.write("@\f@\16@\u01e4\13@\3@\5@\u01e7\n@\3A\3A\5A\u01eb\nA\3")
        buf.write("A\3A\3B\3B\7B\u01f1\nB\fB\16B\u01f4\13B\3C\3C\3C\5C\u01f9")
        buf.write("\nC\3C\3C\5C\u01fd\nC\3C\3C\3C\5C\u0202\nC\3C\3C\3C\5")
        buf.write("C\u0207\nC\3C\3C\3D\3D\3D\7D\u020e\nD\fD\16D\u0211\13")
        buf.write("D\3E\3E\3E\3E\3E\3F\3F\3F\3F\3G\3G\3G\3G\7G\u0220\nG\f")
        buf.write("G\16G\u0223\13G\3G\3G\3H\3H\3I\3I\3J\3J\3J\5J\u022e\n")
        buf.write("J\3J\3J\3J\3J\7J\u0234\nJ\fJ\16J\u0237\13J\3K\3K\3K\3")
        buf.write("K\7K\u023d\nK\fK\16K\u0240\13K\3K\3K\3K\3K\3K\3K\7K\u0248")
        buf.write("\nK\fK\16K\u024b\13K\5K\u024d\nK\3K\3K\3L\3L\3L\3\u023e")
        buf.write("\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\2e\2g\63i\64k\65m\66o\67")
        buf.write("q8s9u:w;y<{=}\2\177>\u0081\2\u0083\2\u0085?\u0087\2\u0089")
        buf.write("@\u008bA\u008dB\u008f\2\u0091\2\u0093C\u0095D\u0097E\3")
        buf.write("\2\r\5\2\n\f\16\17\"\"\3\2\62;\3\2\63;\4\2\62;aa\4\2G")
        buf.write("Ggg\4\2--//\n\2$$))^^ddhhppttvv\6\2\n\f\16\17$$^^\3\2")
        buf.write("c|\3\2C\\\4\2\f\f\17\17\2\u0264\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2\177\3\2\2\2\2\u0085\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u009a\3\2\2\2\5\u00a0")
        buf.write("\3\2\2\2\7\u00a2\3\2\2\2\t\u00a4\3\2\2\2\13\u00a6\3\2")
        buf.write("\2\2\r\u00a8\3\2\2\2\17\u00aa\3\2\2\2\21\u00ac\3\2\2\2")
        buf.write("\23\u00af\3\2\2\2\25\u00b2\3\2\2\2\27\u00b5\3\2\2\2\31")
        buf.write("\u00b8\3\2\2\2\33\u00bb\3\2\2\2\35\u00bd\3\2\2\2\37\u00bf")
        buf.write("\3\2\2\2!\u00c2\3\2\2\2#\u00c5\3\2\2\2%\u00c7\3\2\2\2")
        buf.write("\'\u00c9\3\2\2\2)\u00cb\3\2\2\2+\u00cd\3\2\2\2-\u00cf")
        buf.write("\3\2\2\2/\u00d1\3\2\2\2\61\u00d3\3\2\2\2\63\u00d5\3\2")
        buf.write("\2\2\65\u00d7\3\2\2\2\67\u00d9\3\2\2\29\u00db\3\2\2\2")
        buf.write(";\u00dd\3\2\2\2=\u00df\3\2\2\2?\u00e5\3\2\2\2A\u00e8\3")
        buf.write("\2\2\2C\u00eb\3\2\2\2E\u00f0\3\2\2\2G\u00f8\3\2\2\2I\u00fc")
        buf.write("\3\2\2\2K\u0104\3\2\2\2M\u010a\3\2\2\2O\u0112\3\2\2\2")
        buf.write("Q\u0117\3\2\2\2S\u011c\3\2\2\2U\u0123\3\2\2\2W\u012c\3")
        buf.write("\2\2\2Y\u0130\3\2\2\2[\u0136\3\2\2\2]\u0139\3\2\2\2_\u013f")
        buf.write("\3\2\2\2a\u0148\3\2\2\2c\u014f\3\2\2\2e\u0154\3\2\2\2")
        buf.write("g\u015a\3\2\2\2i\u0166\3\2\2\2k\u0173\3\2\2\2m\u017d\3")
        buf.write("\2\2\2o\u0188\3\2\2\2q\u0194\3\2\2\2s\u01a1\3\2\2\2u\u01ac")
        buf.write("\3\2\2\2w\u01b8\3\2\2\2y\u01be\3\2\2\2{\u01cf\3\2\2\2")
        buf.write("}\u01d1\3\2\2\2\177\u01e6\3\2\2\2\u0081\u01e8\3\2\2\2")
        buf.write("\u0083\u01ee\3\2\2\2\u0085\u0206\3\2\2\2\u0087\u020f\3")
        buf.write("\2\2\2\u0089\u0212\3\2\2\2\u008b\u0217\3\2\2\2\u008d\u021b")
        buf.write("\3\2\2\2\u008f\u0226\3\2\2\2\u0091\u0228\3\2\2\2\u0093")
        buf.write("\u022d\3\2\2\2\u0095\u024c\3\2\2\2\u0097\u0250\3\2\2\2")
        buf.write("\u0099\u009b\t\2\2\2\u009a\u0099\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e\u009f\b\2\2\2\u009f\4\3\2\2\2\u00a0\u00a1")
        buf.write("\7-\2\2\u00a1\6\3\2\2\2\u00a2\u00a3\7,\2\2\u00a3\b\3\2")
        buf.write("\2\2\u00a4\u00a5\7/\2\2\u00a5\n\3\2\2\2\u00a6\u00a7\7")
        buf.write("\61\2\2\u00a7\f\3\2\2\2\u00a8\u00a9\7\'\2\2\u00a9\16\3")
        buf.write("\2\2\2\u00aa\u00ab\7#\2\2\u00ab\20\3\2\2\2\u00ac\u00ad")
        buf.write("\7(\2\2\u00ad\u00ae\7(\2\2\u00ae\22\3\2\2\2\u00af\u00b0")
        buf.write("\7~\2\2\u00b0\u00b1\7~\2\2\u00b1\24\3\2\2\2\u00b2\u00b3")
        buf.write("\7<\2\2\u00b3\u00b4\7<\2\2\u00b4\26\3\2\2\2\u00b5\u00b6")
        buf.write("\7?\2\2\u00b6\u00b7\7?\2\2\u00b7\30\3\2\2\2\u00b8\u00b9")
        buf.write("\7#\2\2\u00b9\u00ba\7?\2\2\u00ba\32\3\2\2\2\u00bb\u00bc")
        buf.write("\7>\2\2\u00bc\34\3\2\2\2\u00bd\u00be\7@\2\2\u00be\36\3")
        buf.write("\2\2\2\u00bf\u00c0\7>\2\2\u00c0\u00c1\7?\2\2\u00c1 \3")
        buf.write("\2\2\2\u00c2\u00c3\7@\2\2\u00c3\u00c4\7?\2\2\u00c4\"\3")
        buf.write("\2\2\2\u00c5\u00c6\7*\2\2\u00c6$\3\2\2\2\u00c7\u00c8\7")
        buf.write("+\2\2\u00c8&\3\2\2\2\u00c9\u00ca\7]\2\2\u00ca(\3\2\2\2")
        buf.write("\u00cb\u00cc\7_\2\2\u00cc*\3\2\2\2\u00cd\u00ce\7}\2\2")
        buf.write("\u00ce,\3\2\2\2\u00cf\u00d0\7\177\2\2\u00d0.\3\2\2\2\u00d1")
        buf.write("\u00d2\7=\2\2\u00d2\60\3\2\2\2\u00d3\u00d4\7<\2\2\u00d4")
        buf.write("\62\3\2\2\2\u00d5\u00d6\7?\2\2\u00d6\64\3\2\2\2\u00d7")
        buf.write("\u00d8\7.\2\2\u00d8\66\3\2\2\2\u00d9\u00da\7$\2\2\u00da")
        buf.write("8\3\2\2\2\u00db\u00dc\7\60\2\2\u00dc:\3\2\2\2\u00dd\u00de")
        buf.write("\7a\2\2\u00de<\3\2\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7{\2\2\u00e4>\3\2\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7")
        buf.write("\7h\2\2\u00e7@\3\2\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7h\2\2\u00eaB\3\2\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7n\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef\7g\2\2\u00efD\3")
        buf.write("\2\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3")
        buf.write("\7j\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6")
        buf.write("\7k\2\2\u00f6\u00f7\7v\2\2\u00f7F\3\2\2\2\u00f8\u00f9")
        buf.write("\7q\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb\7v\2\2\u00fbH\3")
        buf.write("\2\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7i\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\u0103\7t\2\2\u0103J\3\2\2\2\u0104\u0105")
        buf.write("\7h\2\2\u0105\u0106\7n\2\2\u0106\u0107\7q\2\2\u0107\u0108")
        buf.write("\7c\2\2\u0108\u0109\7v\2\2\u0109L\3\2\2\2\u010a\u010b")
        buf.write("\7d\2\2\u010b\u010c\7q\2\2\u010c\u010d\7q\2\2\u010d\u010e")
        buf.write("\7n\2\2\u010e\u010f\7g\2\2\u010f\u0110\7c\2\2\u0110\u0111")
        buf.write("\7p\2\2\u0111N\3\2\2\2\u0112\u0113\7x\2\2\u0113\u0114")
        buf.write("\7q\2\2\u0114\u0115\7k\2\2\u0115\u0116\7f\2\2\u0116P\3")
        buf.write("\2\2\2\u0117\u0118\7c\2\2\u0118\u0119\7w\2\2\u0119\u011a")
        buf.write("\7v\2\2\u011a\u011b\7q\2\2\u011bR\3\2\2\2\u011c\u011d")
        buf.write("\7u\2\2\u011d\u011e\7v\2\2\u011e\u011f\7t\2\2\u011f\u0120")
        buf.write("\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122\7i\2\2\u0122T\3")
        buf.write("\2\2\2\u0123\u0124\7h\2\2\u0124\u0125\7w\2\2\u0125\u0126")
        buf.write("\7p\2\2\u0126\u0127\7e\2\2\u0127\u0128\7v\2\2\u0128\u0129")
        buf.write("\7k\2\2\u0129\u012a\7q\2\2\u012a\u012b\7p\2\2\u012bV\3")
        buf.write("\2\2\2\u012c\u012d\7h\2\2\u012d\u012e\7q\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012fX\3\2\2\2\u0130\u0131\7y\2\2\u0131\u0132")
        buf.write("\7j\2\2\u0132\u0133\7k\2\2\u0133\u0134\7n\2\2\u0134\u0135")
        buf.write("\7g\2\2\u0135Z\3\2\2\2\u0136\u0137\7f\2\2\u0137\u0138")
        buf.write("\7q\2\2\u0138\\\3\2\2\2\u0139\u013a\7d\2\2\u013a\u013b")
        buf.write("\7t\2\2\u013b\u013c\7g\2\2\u013c\u013d\7c\2\2\u013d\u013e")
        buf.write("\7m\2\2\u013e^\3\2\2\2\u013f\u0140\7e\2\2\u0140\u0141")
        buf.write("\7q\2\2\u0141\u0142\7p\2\2\u0142\u0143\7v\2\2\u0143\u0144")
        buf.write("\7k\2\2\u0144\u0145\7p\2\2\u0145\u0146\7w\2\2\u0146\u0147")
        buf.write("\7g\2\2\u0147`\3\2\2\2\u0148\u0149\7t\2\2\u0149\u014a")
        buf.write("\7g\2\2\u014a\u014b\7v\2\2\u014b\u014c\7w\2\2\u014c\u014d")
        buf.write("\7t\2\2\u014d\u014e\7p\2\2\u014eb\3\2\2\2\u014f\u0150")
        buf.write("\7v\2\2\u0150\u0151\7t\2\2\u0151\u0152\7w\2\2\u0152\u0153")
        buf.write("\7g\2\2\u0153d\3\2\2\2\u0154\u0155\7h\2\2\u0155\u0156")
        buf.write("\7c\2\2\u0156\u0157\7n\2\2\u0157\u0158\7u\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159f\3\2\2\2\u015a\u015b\7t\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c\u015d\7c\2\2\u015d\u015e\7f\2\2\u015e\u015f")
        buf.write("\7K\2\2\u015f\u0160\7p\2\2\u0160\u0161\7v\2\2\u0161\u0162")
        buf.write("\7g\2\2\u0162\u0163\7i\2\2\u0163\u0164\7g\2\2\u0164\u0165")
        buf.write("\7t\2\2\u0165h\3\2\2\2\u0166\u0167\7r\2\2\u0167\u0168")
        buf.write("\7t\2\2\u0168\u0169\7k\2\2\u0169\u016a\7p\2\2\u016a\u016b")
        buf.write("\7v\2\2\u016b\u016c\7K\2\2\u016c\u016d\7p\2\2\u016d\u016e")
        buf.write("\7v\2\2\u016e\u016f\7g\2\2\u016f\u0170\7i\2\2\u0170\u0171")
        buf.write("\7g\2\2\u0171\u0172\7t\2\2\u0172j\3\2\2\2\u0173\u0174")
        buf.write("\7t\2\2\u0174\u0175\7g\2\2\u0175\u0176\7c\2\2\u0176\u0177")
        buf.write("\7f\2\2\u0177\u0178\7H\2\2\u0178\u0179\7n\2\2\u0179\u017a")
        buf.write("\7q\2\2\u017a\u017b\7c\2\2\u017b\u017c\7v\2\2\u017cl\3")
        buf.write("\2\2\2\u017d\u017e\7r\2\2\u017e\u017f\7t\2\2\u017f\u0180")
        buf.write("\7k\2\2\u0180\u0181\7p\2\2\u0181\u0182\7v\2\2\u0182\u0183")
        buf.write("\7H\2\2\u0183\u0184\7n\2\2\u0184\u0185\7q\2\2\u0185\u0186")
        buf.write("\7c\2\2\u0186\u0187\7v\2\2\u0187n\3\2\2\2\u0188\u0189")
        buf.write("\7t\2\2\u0189\u018a\7g\2\2\u018a\u018b\7c\2\2\u018b\u018c")
        buf.write("\7f\2\2\u018c\u018d\7D\2\2\u018d\u018e\7q\2\2\u018e\u018f")
        buf.write("\7q\2\2\u018f\u0190\7n\2\2\u0190\u0191\7g\2\2\u0191\u0192")
        buf.write("\7c\2\2\u0192\u0193\7p\2\2\u0193p\3\2\2\2\u0194\u0195")
        buf.write("\7r\2\2\u0195\u0196\7t\2\2\u0196\u0197\7k\2\2\u0197\u0198")
        buf.write("\7p\2\2\u0198\u0199\7v\2\2\u0199\u019a\7D\2\2\u019a\u019b")
        buf.write("\7q\2\2\u019b\u019c\7q\2\2\u019c\u019d\7n\2\2\u019d\u019e")
        buf.write("\7g\2\2\u019e\u019f\7c\2\2\u019f\u01a0\7p\2\2\u01a0r\3")
        buf.write("\2\2\2\u01a1\u01a2\7t\2\2\u01a2\u01a3\7g\2\2\u01a3\u01a4")
        buf.write("\7c\2\2\u01a4\u01a5\7f\2\2\u01a5\u01a6\7U\2\2\u01a6\u01a7")
        buf.write("\7v\2\2\u01a7\u01a8\7t\2\2\u01a8\u01a9\7k\2\2\u01a9\u01aa")
        buf.write("\7p\2\2\u01aa\u01ab\7i\2\2\u01abt\3\2\2\2\u01ac\u01ad")
        buf.write("\7r\2\2\u01ad\u01ae\7t\2\2\u01ae\u01af\7k\2\2\u01af\u01b0")
        buf.write("\7p\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2\7U\2\2\u01b2\u01b3")
        buf.write("\7v\2\2\u01b3\u01b4\7t\2\2\u01b4\u01b5\7k\2\2\u01b5\u01b6")
        buf.write("\7p\2\2\u01b6\u01b7\7i\2\2\u01b7v\3\2\2\2\u01b8\u01b9")
        buf.write("\7u\2\2\u01b9\u01ba\7w\2\2\u01ba\u01bb\7r\2\2\u01bb\u01bc")
        buf.write("\7g\2\2\u01bc\u01bd\7t\2\2\u01bdx\3\2\2\2\u01be\u01bf")
        buf.write("\7r\2\2\u01bf\u01c0\7t\2\2\u01c0\u01c1\7g\2\2\u01c1\u01c2")
        buf.write("\7x\2\2\u01c2\u01c3\7g\2\2\u01c3\u01c4\7p\2\2\u01c4\u01c5")
        buf.write("\7v\2\2\u01c5\u01c6\7F\2\2\u01c6\u01c7\7g\2\2\u01c7\u01c8")
        buf.write("\7h\2\2\u01c8\u01c9\7c\2\2\u01c9\u01ca\7w\2\2\u01ca\u01cb")
        buf.write("\7n\2\2\u01cb\u01cc\7v\2\2\u01ccz\3\2\2\2\u01cd\u01d0")
        buf.write("\5c\62\2\u01ce\u01d0\5e\63\2\u01cf\u01cd\3\2\2\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01d0|\3\2\2\2\u01d1\u01d2\t\3\2\2\u01d2")
        buf.write("~\3\2\2\2\u01d3\u01e7\5}?\2\u01d4\u01d5\t\4\2\2\u01d5")
        buf.write("\u01e7\5}?\2\u01d6\u01db\t\4\2\2\u01d7\u01d8\t\4\2\2\u01d8")
        buf.write("\u01d9\t\5\2\2\u01d9\u01db\5}?\2\u01da\u01d6\3\2\2\2\u01da")
        buf.write("\u01d7\3\2\2\2\u01db\u01e2\3\2\2\2\u01dc\u01dd\t\4\2\2")
        buf.write("\u01dd\u01de\t\5\2\2\u01de\u01e1\5}?\2\u01df\u01e1\5}")
        buf.write("?\2\u01e0\u01dc\3\2\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e4")
        buf.write("\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3")
        buf.write("\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e7\b@\3\2")
        buf.write("\u01e6\u01d3\3\2\2\2\u01e6\u01d4\3\2\2\2\u01e6\u01da\3")
        buf.write("\2\2\2\u01e7\u0080\3\2\2\2\u01e8\u01ea\t\6\2\2\u01e9\u01eb")
        buf.write("\t\7\2\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb")
        buf.write("\u01ec\3\2\2\2\u01ec\u01ed\5\177@\2\u01ed\u0082\3\2\2")
        buf.write("\2\u01ee\u01f2\59\35\2\u01ef\u01f1\5}?\2\u01f0\u01ef\3")
        buf.write("\2\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3")
        buf.write("\3\2\2\2\u01f3\u0084\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5")
        buf.write("\u01f6\5\177@\2\u01f6\u01f8\5\u0083B\2\u01f7\u01f9\5\u0081")
        buf.write("A\2\u01f8\u01f7\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u0207")
        buf.write("\3\2\2\2\u01fa\u01fc\5\177@\2\u01fb\u01fd\5\u0083B\2\u01fc")
        buf.write("\u01fb\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\3\2\2\2")
        buf.write("\u01fe\u01ff\5\u0081A\2\u01ff\u0207\3\2\2\2\u0200\u0202")
        buf.write("\5\177@\2\u0201\u0200\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("\u0203\3\2\2\2\u0203\u0204\5\u0083B\2\u0204\u0205\5\u0081")
        buf.write("A\2\u0205\u0207\3\2\2\2\u0206\u01f5\3\2\2\2\u0206\u01fa")
        buf.write("\3\2\2\2\u0206\u0201\3\2\2\2\u0207\u0208\3\2\2\2\u0208")
        buf.write("\u0209\bC\4\2\u0209\u0086\3\2\2\2\u020a\u020b\7^\2\2\u020b")
        buf.write("\u020e\t\b\2\2\u020c\u020e\n\t\2\2\u020d\u020a\3\2\2\2")
        buf.write("\u020d\u020c\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3")
        buf.write("\2\2\2\u020f\u0210\3\2\2\2\u0210\u0088\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2\u0212\u0213\5\67\34\2\u0213\u0214\5\u0087D\2")
        buf.write("\u0214\u0215\5\67\34\2\u0215\u0216\bE\5\2\u0216\u008a")
        buf.write("\3\2\2\2\u0217\u0218\5\67\34\2\u0218\u0219\5\u0087D\2")
        buf.write("\u0219\u021a\bF\6\2\u021a\u008c\3\2\2\2\u021b\u021c\5")
        buf.write("\67\34\2\u021c\u0221\5\u0087D\2\u021d\u021e\7^\2\2\u021e")
        buf.write("\u0220\n\b\2\2\u021f\u021d\3\2\2\2\u0220\u0223\3\2\2\2")
        buf.write("\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0224\3")
        buf.write("\2\2\2\u0223\u0221\3\2\2\2\u0224\u0225\bG\7\2\u0225\u008e")
        buf.write("\3\2\2\2\u0226\u0227\t\n\2\2\u0227\u0090\3\2\2\2\u0228")
        buf.write("\u0229\t\13\2\2\u0229\u0092\3\2\2\2\u022a\u022e\5\u008f")
        buf.write("H\2\u022b\u022e\5\u0091I\2\u022c\u022e\5;\36\2\u022d\u022a")
        buf.write("\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022c\3\2\2\2\u022e")
        buf.write("\u0235\3\2\2\2\u022f\u0234\5\u008fH\2\u0230\u0234\5\u0091")
        buf.write("I\2\u0231\u0234\5}?\2\u0232\u0234\5;\36\2\u0233\u022f")
        buf.write("\3\2\2\2\u0233\u0230\3\2\2\2\u0233\u0231\3\2\2\2\u0233")
        buf.write("\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2")
        buf.write("\u0235\u0236\3\2\2\2\u0236\u0094\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0238\u0239\7\61\2\2\u0239\u023a\7,\2\2\u023a\u023e")
        buf.write("\3\2\2\2\u023b\u023d\13\2\2\2\u023c\u023b\3\2\2\2\u023d")
        buf.write("\u0240\3\2\2\2\u023e\u023f\3\2\2\2\u023e\u023c\3\2\2\2")
        buf.write("\u023f\u0241\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0242\7")
        buf.write(",\2\2\u0242\u024d\7\61\2\2\u0243\u0244\7\61\2\2\u0244")
        buf.write("\u0245\7\61\2\2\u0245\u0249\3\2\2\2\u0246\u0248\n\f\2")
        buf.write("\2\u0247\u0246\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247")
        buf.write("\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024d\3\2\2\2\u024b")
        buf.write("\u0249\3\2\2\2\u024c\u0238\3\2\2\2\u024c\u0243\3\2\2\2")
        buf.write("\u024d\u024e\3\2\2\2\u024e\u024f\bK\2\2\u024f\u0096\3")
        buf.write("\2\2\2\u0250\u0251\13\2\2\2\u0251\u0252\bL\b\2\u0252\u0098")
        buf.write("\3\2\2\2\30\2\u009c\u01cf\u01da\u01e0\u01e2\u01e6\u01ea")
        buf.write("\u01f2\u01f8\u01fc\u0201\u0206\u020d\u020f\u0221\u022d")
        buf.write("\u0233\u0235\u023e\u0249\u024c\t\b\2\2\3@\2\3C\3\3E\4")
        buf.write("\3F\5\3G\6\3L\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    ADDOP = 2
    MULOP = 3
    SUBOP = 4
    DIVOP = 5
    MODOP = 6
    NOT = 7
    AND = 8
    OR = 9
    CONCAT = 10
    EQ = 11
    NEQ = 12
    LT = 13
    GT = 14
    LTE = 15
    GTE = 16
    LP = 17
    RP = 18
    LB = 19
    RB = 20
    LCB = 21
    RCB = 22
    SEMICOLON = 23
    COLON = 24
    ASSIGN = 25
    COMMA = 26
    DOUBLEQUOTE = 27
    DOT = 28
    UNDERSCORE = 29
    ARRAY = 30
    OF = 31
    IF = 32
    ELSE = 33
    INHERIT = 34
    OUT = 35
    INT_KEY = 36
    FLOAT_KEY = 37
    BOOL_KEY = 38
    VOID_KEY = 39
    AUTO_KEY = 40
    STRING_KEY = 41
    FUNCTION = 42
    FOR = 43
    WHILE = 44
    DO = 45
    BREAK = 46
    CONTINUE = 47
    RETURN = 48
    READINT = 49
    PRINTINT = 50
    READFLOAT = 51
    PRINTFLOAT = 52
    READBOOL = 53
    PRINTBOOL = 54
    READSTRING = 55
    PRINTSTRING = 56
    SUPER = 57
    PREVENTDEF = 58
    BOOLEAN = 59
    INT = 60
    FLOAT = 61
    STRINGLINE = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    ID = 65
    COMMENT = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'-'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'::'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "';'", "':'", "'='", "','", "'\"'", 
            "'.'", "'_'", "'array'", "'of'", "'if'", "'else'", "'inherit'", 
            "'out'", "'integer'", "'float'", "'boolean'", "'void'", "'auto'", 
            "'string'", "'function'", "'for'", "'while'", "'do'", "'break'", 
            "'continue'", "'return'", "'readInteger'", "'printInteger'", 
            "'readFloat'", "'printFloat'", "'readBoolean'", "'printBoolean'", 
            "'readString'", "'printString'", "'super'", "'preventDefault'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ADDOP", "MULOP", "SUBOP", "DIVOP", "MODOP", "NOT", "AND", 
            "OR", "CONCAT", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "LP", 
            "RP", "LB", "RB", "LCB", "RCB", "SEMICOLON", "COLON", "ASSIGN", 
            "COMMA", "DOUBLEQUOTE", "DOT", "UNDERSCORE", "ARRAY", "OF", 
            "IF", "ELSE", "INHERIT", "OUT", "INT_KEY", "FLOAT_KEY", "BOOL_KEY", 
            "VOID_KEY", "AUTO_KEY", "STRING_KEY", "FUNCTION", "FOR", "WHILE", 
            "DO", "BREAK", "CONTINUE", "RETURN", "READINT", "PRINTINT", 
            "READFLOAT", "PRINTFLOAT", "READBOOL", "PRINTBOOL", "READSTRING", 
            "PRINTSTRING", "SUPER", "PREVENTDEF", "BOOLEAN", "INT", "FLOAT", 
            "STRINGLINE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ID", "COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "WS", "ADDOP", "MULOP", "SUBOP", "DIVOP", "MODOP", "NOT", 
                  "AND", "OR", "CONCAT", "EQ", "NEQ", "LT", "GT", "LTE", 
                  "GTE", "LP", "RP", "LB", "RB", "LCB", "RCB", "SEMICOLON", 
                  "COLON", "ASSIGN", "COMMA", "DOUBLEQUOTE", "DOT", "UNDERSCORE", 
                  "ARRAY", "OF", "IF", "ELSE", "INHERIT", "OUT", "INT_KEY", 
                  "FLOAT_KEY", "BOOL_KEY", "VOID_KEY", "AUTO_KEY", "STRING_KEY", 
                  "FUNCTION", "FOR", "WHILE", "DO", "BREAK", "CONTINUE", 
                  "RETURN", "TRUE", "FALSE", "READINT", "PRINTINT", "READFLOAT", 
                  "PRINTFLOAT", "READBOOL", "PRINTBOOL", "READSTRING", "PRINTSTRING", 
                  "SUPER", "PREVENTDEF", "BOOLEAN", "DIGIT", "INT", "EXP", 
                  "DEC", "FLOAT", "STRING", "STRINGLINE", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "LOWERCASE", "UPPERCASE", "ID", "COMMENT", 
                  "ERROR_CHAR" ]

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
            actions[62] = self.INT_action 
            actions[65] = self.FLOAT_action 
            actions[67] = self.STRINGLINE_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_' , '')
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_' , '')
     

    def STRINGLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


