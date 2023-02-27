import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 1010))

    # def test_1(self):
    #     self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\r\\"" """ ,
    #                                    "He asked me: \"Where is John?\r\",<EOF>", 1005))

    def test_1(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \t" """, "This is a string containing tab 	,<EOF>", 1005))

    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = "BOOLEAN int 1.12INTEGER sTRIng not 12and for"
        expect = "BOOLEAN,int,1.12,INTEGER,sTRIng,not,12,and,for,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = "vJozdpl3p1iOcRiAI12 dUB 1.NM 2cY2"
        expect = "vJozdpl3p1iOcRiAI12,dUB,1.,NM,2,cY2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = "break continue else for if return do while"
        expect = "break,continue,else,for,if,return,do,while,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_simple_program4(self):
        """Simple program: int main() {} """
        input = "[ ] { } ( ) ; ,"
        expect = "[,],{,},(,),;,,,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))

    def test_simple_program5(self):
        """Simple program: int main() {} """
        input = "1. .1 1.e1 1E-2 1.0e1 3.14 1_32.32"
        expect = "1.,.,1,1.e1,1E-2,1.0e1,3.14,132.32,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_simple_program6(self):
        """Simple program: int main() {} """
        input = "1>2?3311"
        expect = "1,>,2,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 106))

    def test_simple_program7(self):
        """Simple program: int main() {} """
        input = "{{{{{{{{{int a= 10;}}}}}}}}}"
        expect = "{,{,{,{,{,{,{,{,{,int,a,=,10,;,},},},},},},},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))

    def test_simple_program8(self):
        """Simple program: int main() {} """
        input = """"abc"""
        expect = "Unclosed String: abc"
        self.assertTrue(TestLexer.test(input, expect, 108))

    def test_simple_program9(self):
        """Simple program: int main() {} """
        input = """ "Hi, this is illegall escape \i" """
        expect = """Hi, this is illegall escape \i,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 109))

    def test_simple_program10(self):
        """Simple program: int main() {} """
        input = "+ - * / % ! || && != == < > <= >= ="
        expect = "+,-,*,/,%,!,||,&&,!=,==,<,>,<=,>=,=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 110))

    def test_simple_program11(self):
        """Simple program: int main() {} """
        input = "_abc123"
        expect = "_abc123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))

    def test_simple_program12(self):
        """Simple program: int main() {} """
        input = "1abc"
        expect = "1,abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))

    def test_simple_program13(self):
        """Simple program: int main() {} """
        input = "my-var"
        expect = "my,-,var,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))

    def test_simple_program14(self):
        """Simple program: int main() {} """
        input = "abc#"
        expect = "abc,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 114))

    def test_simple_program15(self):
        """Simple program: int main() {} """
        input = "_Var_nAMW_4"
        expect = "_Var_nAMW_4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))

    def test_simple_program16(self):
        """Simple program: int main() {} """
        input = "VarNamQW_3"
        expect = "VarNamQW_3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))

    def test_simple_program17(self):
        """Simple program: int main() {} """
        input = "_var_namAWQ2"
        expect = "_var_namAWQ2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test_simple_program18(self):
        """Simple program: int main() {} """
        input = "var_naIJJHme1"
        expect = "var_naIJJHme1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))

    def test_simple_program19(self):
        """Simple program: int main() {} """
        input = "TrUE"
        expect = "TrUE,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))

    # def test_simple_program20(self):
    #     """Simple program: int main() {} """
    #     input = """Hello, World!"""
    #     expect = "Hello, World!,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 120))

    def test_simple_program21(self):
        """Simple program: int main() {} """
        input = """"He said, \\"Hello, World!\\"""
        expect = """Unclosed String: He said, \\"Hello, World!"""
        self.assertTrue(TestLexer.test(input, expect, 121))

    # def test_simple_program22(self):
    #     """Simple program: int main() {} """
    #     input = """ "He said, "Hello, World!" joij " """
    #     expect = "He said, \"Hello, World!\" joij ,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 122))

    def test_simple_program23(self):
        """Simple program: int main() {} """
        input = "1E+0.1"
        expect = "1E+0,.,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 123))

    def test_simple_program24(self):
        """Simple program: int main() {} """
        input = "1_234.56"
        expect = "1234.56,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 124))

    def test_simple_program25(self):
        """Simple program: int main() {} """
        input = "1e-3"
        expect = "1e-3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 125))

    def test_simple_program26(self):
        """Simple program: int main() {} """
        input = "1e3"
        expect = "1e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 126))

    def test_simple_program27(self):
        """Simple program: int main() {} """
        input = "1a2b3c"
        expect = "1,a2b3c,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))

    def test_simple_program28(self):
        """Simple program: int main() {} """
        input = "0123"
        expect = "0,123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 128))

    def test_simple_program29(self):
        """Simple program: int main() {} """
        input = "1_2_3_4"
        expect = "1234,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))

    def test_simple_program30(self):
        """Simple program: int main() {} """
        input = "1_234"
        expect = "1234,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 130))

    def test_simple_program31(self):
        """Simple program: int main() {} """
        input = "123"
        expect = "123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 131))

    def test_simple_program32(self):
        """Simple program: int main() {} """
        input = "0"
        expect = "0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 132))

    def test_simple_program33(self):
        """Simple program: int main() {} """
        input = "true"
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 133))

    def test_simple_program34(self):
        """Simple program: int main() {} """
        input = "TrUE"
        expect = "TrUE,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 134))

    def test_simple_program35(self):
        """Simple program: int main() {} """
        input = """Hello \b\r\n"""
        expect = "Hello,Error Token "
        self.assertTrue(TestLexer.test(input, expect, 135))

    def test_simple_program36(self):
        """Simple program: int main() {} """
        input = """aFG[@WQS{QBW7Y6]le$5"""
        expect = "aFG,[,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test_simple_program37(self):
        """Simple program: int main() {} """
        input = "rdad 40oBhenK292aWfTSFt6"
        expect = "rdad,40,oBhenK292aWfTSFt6,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 137))

    def test_simple_program38(self):
        """Simple program: int main() {} """
        input = "Void TRUe 1.12VAR45 ARRay OF 12REAL"
        expect = "Void,TRUe,1.12,VAR45,ARRay,OF,12,REAL,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test_simple_program39(self):
        """Simple program: int main() {} """
        input = """dlsd+1ds-*dmdsa/<>mdks"""
        expect = "dlsd,+,1,ds,-,*,dmdsa,/,<,>,mdks,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 139))

    def test_simple_program40(self):
        """Simple program: int main() {} """
        input = """lsddl<>=1<>=112>=<=d1"""
        expect = "lsddl,<,>=,1,<,>=,112,>=,<=,d1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 140))

    def test_simple_program41(self):
        """Simple program: int main() {} """
        input = """13ek3<9e=9eend<>=Edasdndm<=>erE"""
        expect = "13,ek3,<,9,e,=,9,eend,<,>=,Edasdndm,<=,>,erE,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_simple_program42(self):
        """Simple program: int main() {} """
        input = """djeiwjd1A<=>12>=<=d"""
        expect = "djeiwjd1A,<=,>,12,>=,<=,d,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))

    def test_simple_program43(self):
        """Simple program: int main() {} """
        input = """<-mod>=not+mod+and+not"""
        expect = "<,-,mod,>=,not,+,mod,+,and,+,not,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test_simple_program44(self):
        """Simple program: int main() {} """
        input = """=or<=<><>=-<=>"""
        expect = "=,or,<=,<,>,<,>=,-,<=,>,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_simple_program45(self):
        """Simple program: int main() {} """
        input = """not<>=and>=mod<=-and"""
        expect = "not,<,>=,and,>=,mod,<=,-,and,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 145))

    def test_simple_program46(self):
        """Simple program: int main() {} """
        input = "e--12 e12 E-15 99e 1 1. 1"
        expect = "e,-,-,12,e12,E,-,15,99,e,1,1.,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 146))

    def test_simple_program47(self):
        """Simple program: int main() {} """
        input = "/*12.e0 -101*/ 11.E //11.1e2"
        expect = "11.,E,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_simple_program48(self):
        """Simple program: int main() {} """
        input = "/*1.e0 - 101* {11.E} //22.12\n"
        expect = "/,*,1.e0,-,101,*,{,11.,E,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_simple_program49(self):
        """Simple program: int main() {} """
        input = "13ek3<9e=9eendE//dasd1.ndm<>d1.02erE"
        expect = "13,ek3,<,9,e,=,9,eendE,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

    def test_simple_program50(self):
        """Simple program: int main() {} """
        input = "{abc<>xyzb>cv} /*12mds<>dsd=/*dsd*/*/*"
        expect = "{,abc,<,>,xyzb,>,cv,},*,/,*,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test_simple_program51(self):
        """Simple program: int main() {} """
        input = "//abc{abc<>xyzb>cv}"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_simple_program52(self):
        """Simple program: int main() {} """
        input = """/*-101*/ 11.+12*#$"""
        expect = "11.,+,12,*,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 152))

    def test_simple_program53(self):
        """Simple program: int main() {} """
        input = """(C*$=22Pta!0=&o"""
        expect = "(,C,*,Error Token $"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_unclose_String7(self):
        self.assertTrue(
            TestLexer.test("""\".Hub`22Y\"<{;}\"Y`=DxXhZKh""", ".Hub`22Y,<,{,;,},Unclosed String: Y`=DxXhZKh", 154))

    def test_unclose_String8(self):
        self.assertTrue(TestLexer.test("""\"ULxM*`~.~+C_DISD2""", "Unclosed String: ULxM*`~.~+C_DISD2", 155))

    def test_unclose_String9(self):
        self.assertTrue(
            TestLexer.test("""{SRs}\"Nk8U;\"rA\"@Y3*\"oV\"bh1""", "{,SRs,},Nk8U;,rA,@Y3*,oV,Unclosed String: bh1", 156))

    def test_unclose_String10(self):
        self.assertTrue(TestLexer.test("""\"o|F&)LqX\"+>X+\"#Fft""", "o|F&)LqX,+,>,X,+,Unclosed String: #Fft", 157))

    def test_integer_real1(self):
        self.assertTrue(TestLexer.test("1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42",
                                       "1.2,1.,.,1,1e2,1.2E-2,1.2e-2,.,1E2,9.0,12e8,0.33E-3,128e-42,<EOF>", 158))

    def test_integer_real2(self):
        self.assertTrue(TestLexer.test("9.0 12e8 0.33E-3 128e-42", "9.0,12e8,0.33E-3,128e-42,<EOF>", 159))

    def test_integer_real3(self):
        self.assertTrue(
            TestLexer.test("11.0 12.e8 0.11+E-3 145Ee-42", "11.0,12.e8,0.11,+,E,-,3,145,Ee,-,42,<EOF>", 160))

    def test_integer_real4(self):
        self.assertTrue(TestLexer.test(".11E2 1.11 .33 1.e12 1E-15", ".,11E2,1.11,.,33,1.e12,1E-15,<EOF>", 161))

    def test_integer_real5(self):
        self.assertTrue(TestLexer.test("e--12 e12 E-15 99e 1 1. 1", "e,-,-,12,e12,E,-,15,99,e,1,1.,1,<EOF>", 162))

    def test_integer_real6(self):
        self.assertTrue(
            TestLexer.test("e-12.1 11.e11 12..12 2. .2 11e11 .1e-3",
                           "e,-,12.1,11.e11,12.,.,12,2.,.,2,11e11,.,1e-3,<EOF>",
                           120))

    def test_integer_real7(self):
        self.assertTrue(TestLexer.test("12.e0 -101 11.E 11.1e2", "12.e0,-,101,11.,E,11.1e2,<EOF>", 167))

    def test_comment1(self):
        self.assertTrue(TestLexer.test("/*12.e0 -101*/ 11.E //11.1e2", "11.,E,<EOF>", 168))

    def test_comment2(self):
        self.assertTrue(TestLexer.test("/*12.e0} -101*/ {11.E} 11.1e2", "{,11.,E,},11.1e2,<EOF>", 169))

    def test_comment3(self):
        self.assertTrue(TestLexer.test("{abc} //1.abc", "{,abc,},<EOF>", 170))

    def test_comment4(self):
        self.assertTrue(TestLexer.test("/*1.e0 - 101* {11.E} //22.12\n", "/,*,1.e0,-,101,*,{,11.,E,},<EOF>", 171))

    def test_comment5(self):
        self.assertTrue(TestLexer.test("/*12.e0\nabc*/ -101*/ 11.1e2", "-,101,*,/,11.1e2,<EOF>", 172))

    def test_comment6(self):
        self.assertTrue(TestLexer.test("13ek3<9e=9eendE//dasd1.ndm<>d1.02erE", "13,ek3,<,9,e,=,9,eendE,<EOF>", 173))

    def test_comment7(self):
        self.assertTrue(TestLexer.test("//dasd1.ndm\n<>d1.02erE", "<,>,d1,.,0,2,erE,<EOF>", 174))

    def test_comment8(self):
        self.assertTrue(
            TestLexer.test("{abc<>xyzb>cv} /*12mds<>dsd=/*dsd*/*/*", "{,abc,<,>,xyzb,>,cv,},*,/,*,<EOF>", 175))

    def test_comment9(self):
        self.assertTrue(TestLexer.test("//abc{abc<>xyzb>cv}", "<EOF>", 176))

    def test_comment10(self):
        self.assertTrue(TestLexer.test("abc{abc<>x//yzb>cv}", "abc,{,abc,<,>,x,<EOF>", 177))

    def test_comment11(self):
        self.assertTrue(TestLexer.test("/*abc{abc<>x//yzb>cv}*/", "<EOF>", 178))

    def test_error_char1(self):
        self.assertTrue(TestLexer.test("""/*-101*/ 11.+12*#$""", "11.,+,12,*,Error Token #", 179))

    def test_error_char2(self):
        self.assertTrue(TestLexer.test("""Arj4AORqwExkrCxZPi`:""", "Arj4AORqwExkrCxZPi,Error Token `", 180))

    def test_error_char3(self):
        self.assertTrue(TestLexer.test("""o~jvhs'Ty{*(0Ay0s&n|""", "o,Error Token ~", 181))

    def test_error_char4(self):
        self.assertTrue(TestLexer.test("""(C*$=22Pta!0=&o""", "(,C,*,Error Token $", 182))

    def test_error_char5(self):
        self.assertTrue(TestLexer.test(""";J~%IbnQL!x-OBd""", ";,J,Error Token ~", 183))

    def test_error_char6(self):
        self.assertTrue(TestLexer.test("""b(9KZ|YBraRCF""", "b,(,9,KZ,Error Token |", 184))

    def test_error_char7(self):
        self.assertTrue(TestLexer.test("""kz-70S9+0s)f<)`s0gg""", "kz,-,70,S9,+,0,s,),f,<,),Error Token `", 185))

    def test_error_char8(self):
        self.assertTrue(TestLexer.test("""C+9and+EG9{?r2v}hFAX@>""", "C,+,9,and,+,EG9,{,Error Token ?", 186))

    def test_error_char9(self):
        self.assertTrue(TestLexer.test("""pQ*6'q0+Y@}f(^9Xn""", "pQ,*,6,Error Token '", 187))

    def test_error_char10(self):
        self.assertTrue(TestLexer.test("""aFG[@WQS{QBW7Y6]le$5""", "aFG,[,Error Token @", 188))

    def test_unclose_String1(self):
        self.assertTrue(TestLexer.test("""\"bacxyc""", "Unclosed String: bacxyc", 163))

    def test_unclose_String2(self):
        self.assertTrue(
            TestLexer.test("""NmkobYn{!}+I1+\"`YS2h.J(""""", "NmkobYn,{,!,},+,I1,+,Unclosed String: `YS2h.J(", 164))

    def test_unclose_String3(self):
        self.assertTrue(TestLexer.test("""\"acnv \" \"abc""", "acnv ,Unclosed String: abc", 165))

    def test_unclose_String4(self):
        self.assertTrue(
            TestLexer.test("""\"acms!,lds \" {\"abc\"} 123\"abc""", "acms!,lds ,{,abc,},123,Unclosed String: abc", 166))

    def test_unclose_String5(self):
        self.assertTrue(
            TestLexer.test("""a+11.2+\"mam.123\" 12 \"%^&""", "a,+,11.2,+,mam.123,12,Unclosed String: %^&", 189))

    def test_unclose_String6(self):
        self.assertTrue(
            TestLexer.test("""38n\"[#Ffs?0ED\"0.\"T`#!7n""", "38,n,[#Ffs?0ED,0.,Unclosed String: T`#!7n", 190))

    def test_string9(self):
        self.assertTrue(TestLexer.test("""\"d4444444444\"""", "d4444444444,<EOF>", 191))

    def test_string10(self):
        self.assertTrue(
            TestLexer.test("""\"(IFq+lq(\"IhK6we(*.*)GdvS{(}""", "(IFq+lq(,IhK6we,(,*,.,*,),GdvS,{,(,},<EOF>", 192))

    def test_operator1(self):
        self.assertTrue(TestLexer.test("""ddsls<l>02>=d1s<=123""", "ddsls,<,l,>,0,2,>=,d1s,<=,123,<EOF>", 193))

    def test_operator2(self):
        self.assertTrue(TestLexer.test("""dlsd+1ds-*dmdsa/<>mdks""", "dlsd,+,1,ds,-,*,dmdsa,/,<,>,mdks,<EOF>", 194))

    def test_operator3(self):
        self.assertTrue(TestLexer.test("""lsddl<>=1<>=112>=<=d1""", "lsddl,<,>=,1,<,>=,112,>=,<=,d1,<EOF>", 194))

    def test_operator4(self):
        self.assertTrue(
            TestLexer.test("""13ek3<9e=9eend<>=Edasdndm<=>erE""", "13,ek3,<,9,e,=,9,eend,<,>=,Edasdndm,<=,>,erE,<EOF>",
                           195))

    def test_operator5(self):
        self.assertTrue(TestLexer.test("""djeiwjd1A<=>12>=<=d""", "djeiwjd1A,<=,>,12,>=,<=,d,<EOF>", 196))

    def test_operator6(self):
        self.assertTrue(TestLexer.test("""<-mod>=not+mod+and+not""", "<,-,mod,>=,not,+,mod,+,and,+,not,<EOF>", 197))

    def test_operator7(self):
        self.assertTrue(TestLexer.test("""*and<=>mod</<=""", "*,and,<=,>,mod,<,/,<=,<EOF>", 198))

    def test_operator8(self):
        self.assertTrue(TestLexer.test("""=or<=<><>=-<=>""", "=,or,<=,<,>,<,>=,-,<=,>,<EOF>", 199))

    def test_operator9(self):
        self.assertTrue(TestLexer.test("""not<>=and>=mod<=-and""", "not,<,>=,and,>=,mod,<=,-,and,<EOF>", 200))

    def test_operator10(self):
        self.assertTrue(TestLexer.test("""mod<=<===mod/<=<""", "mod,<=,<=,==,mod,/,<=,<,<EOF>", 2001))
    # def test_simple_program54(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 154))
    #
    # def test_simple_program55(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 155))
    #
    # def test_simple_program56(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 156))
    #
    # def test_simple_program57(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 157))
    #
    # def test_simple_program58(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 158))
    #
    # def test_simple_program59(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 159))
    #
    # def test_simple_program60(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 160))
    #
    # def test_simple_program61(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 161))
    #
    # def test_simple_program62(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 162))
    #
    # def test_simple_program63(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 163))
    #
    # def test_simple_program64(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 164))
    #
    # def test_simple_program65(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 165))
    #
    # def test_simple_program66(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 166))
    #
    # def test_simple_program67(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 167))
    #
    # def test_simple_program68(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 168))
    #
    # def test_simple_program69(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 169))
    #
    # def test_simple_program70(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 170))
    #
    # def test_simple_program71(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 171))
    #
    # def test_simple_program72(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 172))
    #
    # def test_simple_program73(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 173))
    #
    # def test_simple_program74(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 174))
    #
    # def test_simple_program75(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 175))
    #
    # def test_simple_program76(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 176))
    #
    # def test_simple_program77(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 177))
    #
    # def test_simple_program78(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 178))
    #
    # def test_simple_program79(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 179))
    #
    # def test_simple_program80(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 180))
    #
    # def test_simple_program81(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 181))
    #
    # def test_simple_program82(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 182))
    #
    # def test_simple_program83(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 183))
    #
    # def test_simple_program84(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 184))
    #
    # def test_simple_program85(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 185))
    #
    # def test_simple_program86(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 186))
    #
    # def test_simple_program87(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 187))
    #
    # def test_simple_program88(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 188))
    #
    # def test_simple_program89(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 189))
    #
    # def test_simple_program90(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 190))
    #
    # def test_simple_program91(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 191))
    #
    # def test_simple_program92(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 192))
    #
    # def test_simple_program93(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 193))
    #
    # def test_simple_program94(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 194))
    #
    # def test_simple_program95(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 195))
    #
    # def test_simple_program96(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 196))
    #
    # def test_simple_program97(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 197))
    #
    # def test_simple_program98(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 198))
    #
    # def test_simple_program99(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 199))
    #
    # def test_simple_program100(self):
    #     """Simple program: int main() {} """
    #     input = """main: function void() {
    #         a,b,c,d: string= 1,2,3,4;
    #         }"""
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 200))