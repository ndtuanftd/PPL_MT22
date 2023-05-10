# import unittest
# from TestUtils import TestChecker
# from AST import *
#
# class CheckerSuite(unittest.TestCase):
#     def testVardecl0(self):
#         input = "x, y, z: integer = 1, 2, 3;"
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 400))
#     def testVardecl1(self):
#         input = """a: array[10,1] of integer = {1,2,3};
#             a: auto = 10 ;
#         """
#         expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([10, 1], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
#         self.assertTrue(TestChecker.test(input, expect, 401))
#     def testVardecl2(self):
#         input = "x, y, z: integer = 1, 2, 3; k:auto;"
#         expect = "Invalid Variable: k"
#         self.assertTrue(TestChecker.test(input, expect, 402))
#
#     def testEntryPoint3(self):
#         input = """
#         foo1: function integer(z: auto, y: string) {
#             if (z == 1)
#
#             return 1;
#         }
#         foo: function auto(b: integer, c: string) inherit foo1 {
#         preventDefault();
#     d: string = "abc";
#         }
# main:function void() {
#   return 0;
# }
#         """
#         expect = "Type mismatch in statement: ReturnStmt(IntegerLit(0))"
#         self.assertTrue(TestChecker.test(input,expect, 403))
#
#     def testFuncCall4(self):
#         input = """
#         foo: function auto(b: integer, c: string) {
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             if (a) {
#             f: integer;
#             f: float;
#             }
#             a: integer;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             a = c;
#             c = 1000;
#
#         }
#         """
#         expect = "Redeclared Variable: f"
#
#         self.assertTrue(TestChecker.test(input,expect, 404))
#
#     def testFuncCall5(self):
#         input = """
#         foo: function auto(b: integer, c: string) {
#         a: string = "abc";
#         }
#         main:function void() {
#             x, y: integer = 1, foo(1, "abc");
#             a: integer;
#             main: integer;
#             for(a=1, a<10, a+1) {
#             a: integer = 1;
#              a: string = "abc";
#             }
#         }
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect, 405))
#
#     def testExpression6(self):
#         input = """
#         foo: function auto(b: integer, c: string) {
#         a: string = "abc";
#         return 0;
#         }
#         main:function void() {
#             a: integer;
#             main: integer;
#             for(a=1, a<10, a+1) {
#              a = 1*2+true/3.3;
#             }
#         }
#         """
#         expect = "Type mismatch in expression: BinExpr(/, BooleanLit(True), FloatLit(3.3))"
#         self.assertTrue(TestChecker.test(input,expect, 406))
#
#     def testExpression7(self):
#         input = """
#         foo: function auto(b: integer, c: string) {
#         a: string = "abc";
#         return a;
#         }
#         main:function void(c: float) {
#             a: integer;
#             b: float;
#             e,e1: boolean;
#             d: string;
#             // integer
#             // a = foo(a, d);
#             a =  1+2-2*3/4%5;
#             // float
#             b = 1.1+2.2+3*9-2.2*3.3/4.4;
#             b=1*2.2+3/23+10+b+10;
#             // string
#             d = "abc"::("def"::d);
#
#             // boolean
#             e= true||false&&true;
#             e = !e;
#             e = e&&e1;
#
#             e = ((((((1==true)!=(e!=1000))<10.1)>20)<=30)>=2010.123121)+2;
#         }
#         """
#         expect = "Type mismatch in expression: BinExpr(<, BinExpr(!=, BinExpr(==, IntegerLit(1), BooleanLit(True)), BinExpr(!=, Id(e), IntegerLit(1000))), FloatLit(10.1))"
#         self.assertTrue(TestChecker.test(input,expect, 407))
#
#     def testExpression8(self):
#         input="""
#         foo: function auto(b: integer, c: string) {
#             a: string = "abc";
#         return a;
#         }
#         main:function void(c: float) {
#         a: integer;
#         b: float;
#         e,e1: boolean;
#         d: string;
#         // integer
#         a = foo(a, d);
#     }
#     """
#         expect = "Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo, [Id(a), Id(d)]))"
#         self.assertTrue(TestChecker.test(input,expect, 408))
#
#     def testExpression9(self):
#         input = """
#         foo: function auto(b: integer, c: string) {
#         a: string = "abc";
#          return a;
#         }
#         main:function void(c: float) {
#             a: integer;
#             b: float;
#             e,e1: boolean;
#             d: string;
#             // integer
#             a = foo(a, d);
#         }
#         """
#         expect = "Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo, [Id(a), Id(d)]))"
#         self.assertTrue(TestChecker.test(input,expect, 409))
#
#     def testExpression10(self):
#         input = """
#         foo: function void(b: integer, c: string) {
#         a: string = "abc";
#         }
#         main:function void(c: float) {
#             a: integer;
#             b: float;
#             e,e1: boolean;
#             d: string;
#             // integer
#             a = foo(a, d);
#         }
#         """
#         expect = "Type mismatch in expression: FuncCall(foo, [Id(a), Id(d)])"
#         self.assertTrue(TestChecker.test(input,expect, 410))
#
#     def test11(self):
#         input = """
#         foo: function auto(b: integer, c: auto) {
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#
# }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), IntegerLit(2))"
#         self.assertTrue(TestChecker.test(input,expect, 411))
#
#     def test12(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#             return 1;
#             if (b == 1) {
#                 for (c =1, c < 10, c + 1) {
#                     return "strForLoop";
#                 }
#                 return "str";
#             }
#             else {
#                 return "str2";
#             }
#             return 1 + "2";
#
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#
#         }
#         """
#         expect = "Type mismatch in statement: ReturnStmt(StringLit(strForLoop))"
#         self.assertTrue(TestChecker.test(input,expect, 412))
#
#     def test13(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#             return 1;
#             if (b == 1) {
#                 return 2;
#             }
#             else {
#                 return 3;
#             }
#
#             return 1 + "2";
#
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#
#         }
#         """
#         expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), StringLit(2))"
#         self.assertTrue(TestChecker.test(input,expect, 413))
#
#
#     def test14(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#             return 10;
#             if (b == 1) {
#                 return "str";
#             }
#             else {
#                 return "str2";
#             }
#             return 1;
#
#
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#
#         }
#         """
#         expect = "Type mismatch in statement: ReturnStmt(StringLit(str))"
#         self.assertTrue(TestChecker.test(input,expect, 414))
#
#     def test15(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#             if (b == 1) {
#                 return "str";
#             }
#             else {
#                 return "str2";
#             }
#             return 1;
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#
#         }
#         """
#         expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
#         self.assertTrue(TestChecker.test(input,expect, 415))
#
#
#     def test16(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#             return 1;
#             return "ddasd";
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input,expect, 416))
#
#
#     def test17(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input,expect, 417))
#
#     def test18(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#             x: integer = 1;
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#
#         }
#         """
#         expect = "Redeclared Variable: x"
#         self.assertTrue(TestChecker.test(input,expect, 418))
#
#     def test19(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#             x: integer= 1;
#
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input,expect, 419))
#
#     def testArray20(self):
#
#         input = """
#         main:function void() {
#
#         b: array[3,2,1] of integer = {{{1},{2}},{{3},{4}},{{5},{6}}};
#         // d: array[1,2,3] of integer = {{{1},{2}}, };
#
#         a: array[2] of integer = { {1,2},{21,21},{12,13,8} }; // type mismatch var decl
#
#         // x: integer = b[1];  // b[1] type: ArrayType([2,3] IntegerType)
#         }
#         """
#         expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(21), IntegerLit(21)]), ArrayLit([IntegerLit(12), IntegerLit(13)])]))"
#         self.assertTrue(TestChecker.test(input,expect, 420))
#
#     def testArray21(self):
#
#         input = """
#         main:function void() {
#         a: string;
#         b: array[3,2,1] of integer = {{{"fasdfs", a},{2}},{{3},{4}},{{5},{6}}}; // Type mismatch
#         // d: array[1,2,3] of integer = {{{1},{2}}};
#
#         a: array[2] of integer = { {1,2},{21,21},{12,13} }; // type mismatch var decl
#
#         // x: integer = b[1];  // b[1] type: ArrayType([2,3] IntegerType)
#         }
#         """
#         expect = "Illegal array literal: ArrayLit([ArrayLit([StringLit(fasdfs), Id(a)]), ArrayLit([IntegerLit(2)])])"
#         self.assertTrue(TestChecker.test(input,expect, 421))
# #
#     def test22(self):
#         input = """
#         foo: integer;
#         foo: float;
#         foo : function auto(inherit x : auto, inherit y : auto, z : auto) {
#             x = 1;
#             return x + y + z;
#         }
#
#
#         main : function void() inherit foo{
#                  super(1.0, 2.0, 3.0);
#                 z: integer = foo("str1",2,3) + 1;
#                 x = "abc";
#                 y = true;
#             }
#         main: integer = 1;
#         """
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input,expect, 422))
#
#
#     def test23(self):
#         input = """
#         foo: function auto(b: integer, c: auto) {
#             // super(1,2);
#              x: auto = x+x;
#
#             // x: auto = x+10;
#             x = 10;
#             x = "abc";
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#             x: integer= 1;
#
#         }
#         """
#         expect = "Type mismatch in statement: AssignStmt(Id(x), StringLit(abc))"
#         self.assertTrue(TestChecker.test(input,expect, 423))
#
#     def test24(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#             x: integer= 1;
#
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input,expect, 424))
#
#
#     def test25(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#             x: integer= 1;
#
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input,expect, 425))
#
#
#     def test26(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#             x: integer= 1;
#
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input,expect, 426))
#
#     def test27(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#             x: integer= 1;
#
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input,expect, 427))
#
#     def test28(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#             x: integer= 1;
#
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input,expect, 428))
#
#     def test29(self):
#         input = """
#         foo: function auto(b: integer, c: auto) inherit foo1 {
#             super(1,2);
#         }
#
#         main:function void() {
#             b: integer = 1;
#             a:auto = b<100;
#             d: auto = "abc" :: "def";
#             c:auto = foo(1, d);
#             foo1(1,2);
#             foo(1, "3123");
#             foo1(1, 1.2);
#             foo(1, 2);
#             a = c;
#             c = 1000;
#         }
#
#         foo1: function auto(inherit x: auto, y: auto) {
#             x: integer= 1;
#
#         }
#         """
#         expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
#         self.assertTrue(TestChecker.test(input,expect, 429))
#
#
#     def testScope30(self):
#
#         input = """
#         main:function void() {
#         a: integer;
#         if (a==1) {
#             a: integer = 1;
#             b: float = 2.3;
#             if (b>2) {
#                 a: float = 1.1;
#                 a: string ;
#             }
#         }
#         }
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input,expect, 430))
#
#     def testScope31(self):
#
#         input = """
#         main:function void() {
#         a: integer;
#         if (a==1) {
#             a: string = "dads";
#             b: float = 2.3;
#             if (b>2) {
#                 a = "fasfd";
#             }
#                 a= "ffdfssfsfdffs";
#         }
#         a = "3jiojiojoij";
#         }
#         """
#         expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(3jiojiojoij))"
#         self.assertTrue(TestChecker.test(input,expect, 431))
#
#     def testScope32(self):
#
#             input = """
#             main:function void() {
#             a: integer;
#             if (a==1) {
#                 a: string = "dads";
#                 b: float = 2.3;
#                 if (b>2) {
#                     a = "fasfd";
#                 }
#                     a= "ffdfssfsfdffs";
#             }
#             a = "3jiojiojoij";
#             }
#             """
#             expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(3jiojiojoij))"
#             self.assertTrue(TestChecker.test(input,expect, 432))
#
#     def test33(self):
#         input = """
#         foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
#             return a+b;
#         }
#
#         foo: function integer(x: string, y: integer) inherit foo1 {
#             preventDefault();
#             a: integer = 1;
#             b: integer = 2;
#             d: float = 3.4;
#
#             return 1;
#         }
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect, 433))
#
#     def test34(self):
#         input = """
#         foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
#             return a+b;
#         }
#
#         foo: function integer(x: string, y: integer) inherit foo1 {
#             preventDefault();
#             a: integer = 1;
#             b: integer = 2;
#             d: float = 3.4;
#
#             return 1;
#         }
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect, 434))
#
#     def test35(self):
#         input = """
#         foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
#             return a+b;
#         }
#
#         foo: function integer(x: string, y: integer) inherit foo1 {
#             preventDefault();
#             a: integer = 1;
#             b: integer = 2;
#             d: float = 3.4;
#
#             return 1;
#         }
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect, 435))
#
#     def test36(self):
#         input = """
#         foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
#             return a+b;
#         }
#
#         foo: function integer(x: string, y: integer) inherit foo1 {
#             preventDefault();
#             a: integer = 1;
#             b: integer = 2;
#             d: float = 3.4;
#
#             return 1;
#         }
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect, 436))
#
#     def test37(self):
#         input = """
#         foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
#             return a+b;
#         }
#
#         foo: function integer(x: string, x: integer) inherit foo1 {
#             preventDefault();
#             a: integer = 1;
#             b: integer = 2;
#             d: float = 3.4;
#
#             return 1;
#         }
#         """
#         expect = "Redeclared Parameter: x"
#         self.assertTrue(TestChecker.test(input,expect, 437))
#
#     def test38(self):
#         input = """
#         foo1: function integer(inherit a: integer, a: integer, inherit out c: string, d: float) {
#             return a+b;
#         }
#
#         foo: function integer(x: string, y: integer) inherit foo1 {
#             preventDefault();
#             a: integer = 1;
#             b: integer = 2;
#             d: float = 3.4;
#
#             return 1;
#         }
#         """
#         expect = "Redeclared Parameter: a"
#         self.assertTrue(TestChecker.test(input,expect, 438))
#
#     def test39(self):
#         input = """
#         foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
#             return a+b;
#         }
#
#         foo: function integer(x: string, y: integer) inherit foo1 {
#             preventDefault();
#             a: integer = 1;
#             b: integer = 2;
#             d: float = 3.4;
#
#             return 1;
#         }
#         """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input,expect, 439))
#
#     def testInherit40(self):
#         input = """
#         foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
#             return a+b;
#         }
#
#         foo: function integer(x: string, y: integer) inherit foo1 {
#             super(123123, "strText");
#             return 1;
#         }
#         """
#         expect = "Type mismatch in expression: StringLit(strText)"
#         self.assertTrue(TestChecker.test(input,expect, 440))
#
#
#     def testInherit41(self):
#         input = """
#         foo1: function integer(inherit a: integer, b: integer,inherit out c: string, d: float) {
#             return a+b;
#         }
#
#         foo: function integer(a: string, y: integer) inherit foo1 {
#             super(123123, "fadfsfdff");
#             return 1;
#         }
#         """
#         expect = "Type mismatch in expression: StringLit(fadfsfdff)"
#         self.assertTrue(TestChecker.test(input,expect, 441))
#
#     def testInherit42(self):
#         input = """
#            foo1: function integer(a: integer, inherit b: integer, out c: string, d: float) {
#                return a+b;
#            }
#
#            foo: function integer(a: string, y: integer) inherit foo1 {
#                super(10,20, "arwerwwer", 10.1);
#                 b: float; // redeclared b from foo1
#                return 1;
#            }
#            """
#         expect = "Redeclared Variable: b"
#         self.assertTrue(TestChecker.test(input, expect, 442))
#
#
#     def testInherit43(self):
#         input = """
#            foo1: function integer(a: integer, inherit b: integer, out c: string, d: float) {
#                return a+b;
#            }
#
#            foo: function integer(a: string, y: integer) inherit foo1 {
#                super(10,20, "arwerwwer");
#                 b: float; // redeclared b from foo1
#                return 1;
#            }
#            """
#         expect = "Type mismatch in expression: "
#         self.assertTrue(TestChecker.test(input, expect, 443))
#
#     def testInherit44(self):
#         input = """
#            foo1: function integer(a: integer, inherit b: integer, out c: string, d: float) {
#                return a+b;
#            }
#
#            foo: function integer(a: string, y: integer) inherit foo1 {
#                super(10,20, "arwerwwer", 13.312, true,a,y);
#                 b: float; // redeclared b from foo1
#                return 1;
#            }
#            """
#         expect = "Type mismatch in expression: BooleanLit(True)"
#         self.assertTrue(TestChecker.test(input, expect, 444))
#
#     def testInherit45(self):
#         input = """
#            foo1: function integer(a: integer, inherit b: integer, out c: string, d: float) {
#                return a+b;
#            }
#
#            foo: function integer(a: string, y: integer) inherit foo1 {
#                super(10,20, "arwerwwer", 10.1);
#                 b: float; // redeclared b from foo1
#                return 1;
#            }
#            """
#         expect = "Redeclared Variable: b"
#         self.assertTrue(TestChecker.test(input, expect, 445))
#
#     def testDecl446(self):
#         input = """
#     main: function void() {
#         x:auto = foo(1);
#        foo2();
#        arr:array[2,2] of integer = {{1,2}, {1,2}};
#        foo(1);
#         b[2] = 9;
#         a[1,2] = {1,2,3,4,5,6,7,8};
#       c: array [2,2] of integer = {{21,2},{12,212}};
#
#         // a: integer = bar(10);
#        // b: array [2] of integer = {1,2};
#       // d: array [2] of integer = { x({2}, 2), bar(10) };
#     // a: array [1] of integer = {1};
#      // bar(1);
#     // a: integer = x(b);
#
#     }
#
#             foo:function float(x:integer){
#                 return x + 1.2;
#             }
#             foo2: function void(){}
#         """
#         expect = "Undeclared Identifier: b"
#         self.assertTrue(TestChecker.test(input, expect, 446))
#
#     def test447(self):
#         input = """
#         foo1: function integer(inherit a: integer, b: integer) {
#         printString("hello");
#             a = printInteger("fadsf");
#             c: integer;
#             c = foo("fdadf",b);
#             a = 10;
#         }
#         foo: function array[4] of integer(a: string, y: integer) inherit foo1 {
# //             super(a, a);
#             preventDefault();
#             a: integer;
#             return {1,2,3,4};
#         }
#
#         main: function void() {
#         // a = b;
#         }
#         """
#
#         expect = "Type mismatch in expression: FuncCall(printInteger, [StringLit(fadsf)])"
#
#         self.assertTrue(TestChecker.test(input, expect, 447))
#
#     def test448(self): # TODO: fix raise index Op arr[1,2,3]
#         intput = """
#        main:function void() inherit foo{
#                 super(12);
#                 x:auto = foo(1);
#                 foo2();
#                 arr:array[2,2] of integer = {{1,2}, {1,2}};
#                 arr[1,2,3] = 1;
#             }
#             foo:function float(x:float){
#                 return x + 1.2;
#             }
#             foo2: function void(){}
#         """
#         expect = "Type mismatch in expression: IntegerLit(3)"
#         self.assertTrue(TestChecker.test(intput, expect, 448))
#
#     def test449(self):
#         input = """
#         foo: function auto() {}
#         inc : function void (out b : integer, d: float) inherit foo{
#               super();
#               foo();
#               a: integer = 1 % foo();
#               c: integer = 124;
#         }
#         foo : function void (inherit n: float, f: integer){}
#
#                foo: function void (b: auto, c: auto){
#             d: string;
#             a: string = b + d;
#
#         }
#         b: integer = foo();
#         main: function void() {
#
#         }
#         """
#         expect = "Redeclared Function: foo"
#
#         self.assertTrue(TestChecker.test(input, expect, 449))
#
#     def test50(self):
#         input = """
#         foo: function auto() {}
#
#         inc : function void (out b : integer, d: float){
#             i: integer;
#             for (i = 0, i < 10, 1) {
#                 if (b > 1) {
#                     b = b + 1;
#                     break;
#                 }
#                 continue;
#             }
#             continue;
#         }
#
#         """
#         expect = "Must in loop: ContinueStmt()"
#         self.assertTrue(TestChecker.test(input, expect, 450))
#
#     def test51(self):
#         input = """
#         foo: function auto() {}
#
#         inc : function void (out b : integer, d: float){
#             i,j: integer;
#             a: float;
#             for (i = 0, i < 10, 1) {
#                 if (b > 1) {
#                     b = b + 1;
#                     for (i = "fsdf", i < 10, a) {
#                     break;
#                         while(true) {
#                         break;
#                         }
#                     }
#                     break;
#                 }
#                 continue;
#             }
#             continue;
#         }
#         """
#         expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), StringLit(fsdf)), BinExpr(<, Id(i), IntegerLit(10)), Id(a), BlockStmt([BreakStmt(), WhileStmt(BooleanLit(True), BlockStmt([BreakStmt()]))]))"
#         self.assertTrue(TestChecker.test(input, expect, 451))
#
#     def test52(self):
#         input = """ a : string = "2" :: "33" ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 452))
#
#     def test53(self):
#         input = """ x : string = "223232" ; a : string = "2" :: x ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 453))
#
#     def test54(self):
#         input = """ x : float = -2.5554 ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 454))
#
#     def test55(self):
#         input = """ x : float = -2.5554 + 3 + -4.2 ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 455))
#
#     def test56(self):
#         input = """ x : boolean = !true ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 456))
#
#     def test57(self):
#         input = """ a : boolean = false ; x : boolean = !a ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 457))
#
#     def test58(self):
#         input = """ a : string = "false" ; x : boolean = !a ;"""
#         expect = "Type mismatch in expression: UnExpr(!, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 458))
#
#     def test59(self):
#         input = """ x : integer ; a : array [3,1] of integer = {{1}, {2}, {x}} ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 459))
#
#     def test60(self):
#         input = """ x : float ; a : array [1,2] of integer = {1, 2, x} ;"""
#         expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), Id(x)])"
#         self.assertTrue(TestChecker.test(input, expect, 460))
#
#     def test61(self):
#         input = """ a : array [1,2] of integer = {1, 2, x} ;"""
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 461))
#
#     def test62(self):
#         input = """ a : array [2,1] of integer = {{1 + 2}, {3 + 4}} ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 462))
#
#     def test63(self):
#         input = """ a : array [1,2] of integer = {true, 1} ;"""
#         expect = "Illegal array literal: ArrayLit([BooleanLit(True), IntegerLit(1)])"
#         self.assertTrue(TestChecker.test(input, expect, 463))
#
#     def test64(self):
#         input = """ x, y : integer ; a : array [2] of integer = {1 + x, 2 * y} ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 464))
#
#     def test65(self):
#         input = """ x, y : integer ; b : array [2, 3] of integer ; a : array [1,2] of integer = {1 + x, 2 * b} ;"""
#         expect = "Type mismatch in expression: BinExpr(*, IntegerLit(2), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 465))
#
#     def test66(self):
#         input = """ a : array [1,2] of integer = {true, true, false} ;"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2], IntegerType), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False)]))"
#         self.assertTrue(TestChecker.test(input, expect, 466))
#
#     def test67(self):
#         input = """ a : array [2, 2] of integer = {{1, 2}, {3, 4}} ; b : integer = a[0] ;"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(0)]))"
#         self.assertTrue(TestChecker.test(input, expect, 467))
#
#     def test68(self):
#         input = """ b : integer = a[2] ;"""
#         expect = "Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 468))
#
#     def test69(self):
#         input = """ a : integer ; b : integer = a[2] ;"""
#         expect = "Type mismatch in expression: Id(a)"
#         self.assertTrue(TestChecker.test(input, expect, 469))
#
#     def test70(self):
#         input = """ a : array [1,2] of integer ; b : integer = a[2, 3, 5] ;"""
#         expect = "Type mismatch in expression: IntegerLit(5)"
#         self.assertTrue(TestChecker.test(input, expect, 470))
#
#     def test71(self):
#         input = """ a : array [1,2] of integer ; b : integer = a[2.2] ;"""
#         expect = "Type mismatch in expression: FloatLit(2.2)"
#         self.assertTrue(TestChecker.test(input, expect, 471))
#
#     def test72(self):
#         input = """ a : array [1,2] of integer ; b : integer = a[1 + 2] ;"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2))]))"
#         self.assertTrue(TestChecker.test(input, expect, 472))
#
#     def test73(self):
#         input = """ a : auto = "false" ; b : auto = a :: "true" ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 473))
#
#     def test74(self):
#         input = """ x : auto = {1, 2, 3} ; b : auto = x :: {4, 5, 6} ;"""
#         expect = "Type mismatch in expression: BinExpr(::, Id(x), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]))"
#         self.assertTrue(TestChecker.test(input, expect, 474))
#
#     def test75(self):
#         input = """ x : auto = {{1.0, 2.2}, {3.9, 2.5}, {3.7, 9.0}} ; """
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 475))
#
#     def test76(self):
#         input = """ x : auto = 1 + {1, 2, 3}; """
#         expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
#         self.assertTrue(TestChecker.test(input, expect, 476))
#
#     def test77(self):
#         input = """ a : array [3,2] of float = {{2.0, 3.0}, {3.0, 4.0}, {5.0, 6.6}} ; b : integer = a[2, 1] ;"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(2), IntegerLit(1)]))"
#         self.assertTrue(TestChecker.test(input, expect, 467))
#
#     def test78(self):
#         input = """ a : array [3] of float = {1.0, 2.0, 6.6} ; b : float = a[2] ;"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 478))
#     def test79(self):
#         input = """ arr : array [3, 2] of integer = {{{1}, {2}}, {{2}, {3}}, {{3}, {3, 3}}} ; """
#         expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(3)])])"
#         self.assertTrue(TestChecker.test(input, expect, 479))
#
#     def test_80(self):
#         input = """
#         x: float = 3.0;
#         a : array [2] of integer;
#         foo: function auto(){}
#         fact : function integer (n : integer) {
#             b: float;
#             n = b + 1;
#         }
#         main: function void(){}
#     """
#
#         expect = "Type mismatch in statement: AssignStmt(Id(n), BinExpr(+, Id(b), IntegerLit(1)))"
#         self.assertTrue(TestChecker.test(input, expect, 480))
#
#     def test_81(self):
#         input = """
#         a : array [2] of integer;
#         foo: function auto(x: integer){}
#         foo1: function auto(x: integer) {}
#         fact : function integer (n : integer) {
#             foo: float = 3.0;
#             b: integer;
#             n1: boolean = -foo1(1) + 1;
#         }
#         main: function void(){}
#     """
#
#         expect = "Type mismatch in Variable Declaration: VarDecl(n1, BooleanType, BinExpr(+, UnExpr(-, FuncCall(foo1, [IntegerLit(1)])), IntegerLit(1)))"
#         self.assertTrue(TestChecker.test(input, expect, 481))
#
#     def test_82(self):
#         input = """
#         foo: function auto(x: integer){}
#         foo1: function auto(x: float){}
#         fact : function integer (n : integer) {
#             a : array [2] of integer;
#             a[1] = (foo1(foo(1900)) + 1);
#         }
#         main: function integer(){}
#     """
#
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 482))
#
#     def test_83(self):
#         input = """
#         // foo: function auto(){}
#         foo1: function auto(y: boolean){}
#         foo2: function boolean(){}
#         fact : function integer (n : integer) {
#             a : array [2] of integer;
#             i: float = 3;
#             for (i = 123, 9 > 8, i + 1){}
#         }
#         main: function void(){}
#     """
#
#         expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(123)), BinExpr(>, IntegerLit(9), IntegerLit(8)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"
#         self.assertTrue(TestChecker.test(input, expect, 483))
#
#     def test_84(self):
#         input = """
#         foo2: function boolean(i: integer){}
#         main: function void(){
#             for (i = 123, i > 8, foo2(1)){}
#         }
#     """
#
#         expect = "Undeclared Identifier: i"
#         self.assertTrue(TestChecker.test(input, expect, 484))
#
#     def test_85(self):
#         input = """
#         foo2: function auto(i: integer){
#             return 1;
#             if (i == 1) {
#             return 2;
#             }
#             else {
#             return "dada";
#             }
#         }
#         main: function void(){
#             foo1(213);
#         }
#     """
#
#         expect = "Type mismatch in statement: ReturnStmt(StringLit(dada))"
#         self.assertTrue(TestChecker.test(input, expect, 485))
#
#     def test_86(self):
#         input = """
#         foo1: function integer(){}
#         foo2: function float(inherit x: boolean){
#             return 1;
#         }
#         foo3: function float() inherit foo1{
#             printInteger(1);
#             // preventDefault();
#             return 1.123;
#         }
#         main: function void(){
#             x: integer = readInteger();
#         }
#     """
#
#         expect = "None"
#         self.assertTrue(TestChecker.test(input, expect, 486))
#
#     def test_87(self):
#         input = """
#         x: integer;
#         foo1: function integer(inherit x: float){}
#         foo2: function float(inherit y: float) inherit foo1{
#             super(10);
#             z: float = 10.1;
#             return 1;
#         }
#         foo3: function float(out z: float) inherit foo2{
#             preventDefault();
#             y: integer = 10;
#             printInteger(1);
#             return 1.123;
#         }
#         main: function void(){
#             x: integer = readInteger();
#             break;
#         }
#     """
#
#         expect = "Must in loop: BreakStmt()"
#         self.assertTrue(TestChecker.test(input, expect, 487))
#
#     def test_88(self):
#         input = """
#         x: integer;
#         foo1: function integer(inherit x: float){}
#         foo2: function float(inherit y: float){
#             super(10);
#             z: float = 10.1;
#             return 1;
#         }
#         main: function void(){
#             x: integer = readInteger();
#         }
#     """
#
#         expect = "Invalid statement in function: foo2"
#         self.assertTrue(TestChecker.test(input, expect, 488))
#
#     def test_89(self):
#         input = """
#         x: integer;
#         foo1: function integer(){}
#         foo2: function float(inherit y: float) inherit foo1{
#             super();
#             z: float = 10.1;
#             return 1;
#         }
#         main: function void(){
#             x: integer = readInteger();
#             return 1;
#         }
#     """
#
#         expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
#         self.assertTrue(TestChecker.test(input, expect, 489))
#
#     def test_90(self): # TODO: fix index op
#         input = """
#         isPalindrome: function boolean(strs: array[100] of string, strSize: integer) {
#             i: integer;
#           for (i = 0, i < strSize / 2, i+1) {
#             if (strs[i] != strs[strSize-i-1]) {
#           return 10;
#               return false;
#             }
#           }
#           return true;
#         }
#         main: function void() {
#             strs   : array [5] of string = {"hello", "world", "!!!", "", "test\\n"};
#             if(isPalindrome(strs, 5)) printString("Correct!!!");
#             else printString("Wrong!!!");
#         }
#     """
#
#         expect = "Type mismatch in expression: BinExpr(!=, ArrayCell(strs, [Id(i)]), ArrayCell(strs, [BinExpr(-, BinExpr(-, Id(strSize), Id(i)), IntegerLit(1))]))"
#         self.assertTrue(TestChecker.test(input, expect, 490))
#
#     def test_91(self):
#         input = """
#         inc: function auto(a: integer, b: float)
#         {
#             a = -1 + -2 + -3;
#             b = a + a / b + a;
#             while (a!=0)
#                 a = a - 1;
#             do
#             {
#                 return b;
#             }
#             while (a==true);
#             return a;
#         }
#         main: function void() {
#         return 1;
#         }
#     """
#         expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
#         self.assertTrue(TestChecker.test(input, expect, 491))
#
#     def test_492(self):
#         input = """
#         count: function boolean(n: integer)
#         {
#             i: integer;
#             c: integer = 0;
#             for (i=1,i<n,i+1)
#                 if (n%i==0)
#                     c = c + 1;
#             if (c == 2)
#                 return true;
#             else
#                 return false;
#         }
#         main: function void() {
#             n : integer;
#             printString("Input n:");
#             readInteger(n);
#             if (count(n) == true)
#                 print("n is prime number");
#             else
#                 print("n is not prime number");
#         }
#     """
#         expect = "Type mismatch in statement: CallStmt(readInteger, Id(n))"
#         self.assertTrue(TestChecker.test(input, expect, 492))
#
#     def test_93(self):
#         input = """
#         s : string;
#         random: function string(n: integer)
#         {
#             i: integer;
#             s = "";
#             for (i = 0,i < n,i+1)
#                 s = s + readString();
#             return s;
#         }
#         main: function void() {}
#     """
#         expect = "Type mismatch in expression: BinExpr(+, Id(s), FuncCall(readString, []))"
#         self.assertTrue(TestChecker.test(input, expect, 493))
#
#     def test_94(self):
#         input = """
#         foo3: function auto(inherit i: integer, a: float) {}
#         foo2: function auto(inherit b: float, a: float) inherit foo3 {
#             super(1, 1.0);
#             c: integer = 1;
#         }
#         foo1: function integer(inherit c: float) inherit foo2 {
#             super(1, 1.0);
#             i: integer = 2;
#
#             b: string;
#             return 1;
#         }
#         main: function void(){
#             foo2(foo1(1.0), 1);
#         }
#             """
#         expect = "Redeclared Variable: b"
#         self.assertTrue(TestChecker.test(input, expect, 494))
#
#     def test_95(self):
#         input = """
#         s : string;
#         random: function string(n: integer)
#         {
#             i: integer;
#             s = "";
#             for (i = 0,i < n,i+1)
#                 s = s + randomChar();
#             return s;
#         }
#         main: function void() {}
#     """
#         expect = "Undeclared Function: randomChar"
#         self.assertTrue(TestChecker.test(input, expect, 495))
#
#     def test_96(self):
#         input = """
#         s : string;
#         random: function string(n: integer)
#         {
#             i: integer;
#             s = "";
#             for (i = 0,i < n,i+1)
#                 s = s + readString();
#             return s;
#         }
#         main: function void() {}
#     """
#         expect = "Type mismatch in expression: BinExpr(+, Id(s), FuncCall(readString, []))"
#         self.assertTrue(TestChecker.test(input, expect, 496))
#
#     def test_97(self):
#         input = """
#         s : string;
#         random: function string(n: integer)
#         {
#             i: integer;
#             s = "";
#             for (i = 0,i < n,i+1)
#                 s = s::readString();
#             return s;
#         }
#         main: function void() {
#             n : integer;
#             printString("Input n:");
#             n = readInteger();
#             printString("The random string length n is "::random(n));
#             return 1;
#         }
#     """
#         expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
#         self.assertTrue(TestChecker.test(input, expect, 497))
#
#     def test_98(self): # TODO: fix index op
#         input = """
#         a,b: array[10] of integer;
#         swap: function void(out a: array[10] of integer, out b: array[10] of integer, n: integer)
#         {
#             if (n>10)
#                 return;
#             else
#             {
#                 temp,i : integer;
#                 for (i=0,i<n,i+1)
#                 {
#                     temp=a[i];
#                     a[i]=b[i];
#                     b[i]=temp;
#                 }
#             }
#         }
#         main: function void() {
#             return 1;
#         }
#     """
#         expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
#         self.assertTrue(TestChecker.test(input, expect, 498))
#
#     def test_99(self):
#         input = """
#             foo3: function auto(inherit i: integer, b: float) {}
#             foo2: function auto(inherit b: float, a: float) inherit foo3 {
#                 preventDefault(1+1);
#             }
#             main: function void(){
#                 foo2(foo1(1.0), 1);
#             }
#             """
#         expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), IntegerLit(1))"
#         self.assertTrue(TestChecker.test(input, expect, 499))


import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_400(self):
        input = """
        foo1: function void (c: integer) inherit foo
        {
            super(b, c);
        }
        foo: function void (a: integer, inherit b: auto) {

        }
        foo2: function void (x: integer) inherit foo1
        {
            super(b);
        }
        main: function void() {

        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_401(self):
        input = """
        a: integer = foo(1, 2) + 1;
        foo: function auto (a: auto, b: auto)
        {
            return a + b;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = input = """i, j, t: string = \"20\", \"30\", \"40\";
        main: function void()
        {
            k = j :: (i :: t);
            printString(k);
        }"""
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_403(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_404(self):
        input = """
        foo: function integer (inherit x: integer, y: integer)
        {

        }
        foo1: function integer(z: string) inherit foo
        {
            super(x, y);
        }
        main: function void() {

        }"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_405(self):
        input = """x, y: boolean = true, foo(1, 2);
        foo: function auto (x: auto, y: integer)
        {
            return x == y;
        }
        goo: function void(a: auto)
        {

        }
        main: function void() {
            goo(2018);
            goo(3.75);
        }"""
        expect = "Type mismatch in statement: CallStmt(goo, FloatLit(3.75))"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """
        foo: function auto (a: auto, b: integer)
        {
            a = a + b;
            return a;
        }
        main: function void() {
            x: integer = foo(1.7, 2);
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, [FloatLit(1.7), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_407(self):
        input = """
        foo: function auto (a: auto, b: integer)
        {
            a = a + b;
            return a;
        }
        goo: function void()
        {
            x: integer = foo(1.7, 2);
        }
        main: function void() {

        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, [FloatLit(1.7), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_408(self):
        input = """
        foo: function auto (a: auto, b: integer)
        {
            a = a + b;
            return a;
        }
        goo: function void() inherit foo
        {
            a: integer = 1;
            super(1, 2);
        }
        main: function void() {

        }"""
        expect = "Invalid statement in function: goo"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_409(self):
        input = """
        inc : function void (out n : integer, a: float) inherit foo {} 
        foo : function auto (inherit n: float, n: integer){} 
        main: function void()
        {

        }"""
        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_410(self):
        input = """
        foo: function void (inherit a: integer, a: float) inherit bar {}
        main: function void()
        {

        }"""
        expect = "Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_411(self):
        input = """
        foo: function void() inherit foo1{
            super("HCMUT", true);
            x = 7;
        }
        foo1: function void (inherit x: string, inherit x: boolean) {}
        main: function void() {}"""
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_412(self):
        input = """
        foo: function integer() {
            foo: integer = 2018;
        }
        main: function void() {
	        foo: integer = foo();
        }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [])"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_413(self):
        input = """
        foo: function auto (a: auto, b: integer)
        {
            return a + b;
        }
        a: integer = foo(1, 2) + 1;
        main: function void() {
            a = foo(1.1, 2);
        }"""
        expect = "Type mismatch in expression: FuncCall(foo, [FloatLit(1.1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """
        x: auto = x + 4.7;
        foo: function void(a: integer) {}
        main: function void() {
            foo(x);
        }"""
        expect = "Type mismatch in statement: CallStmt(foo, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
        foo: function void(a: integer) {}
        foo: integer = 2;
        main: function void() {

        }"""
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
        foo: function void (b: integer) inherit a {
            preventDefault();
        }
        a: function string (inherit c: string) {}
        a: integer = 1;
        main: function void() {}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """
        foo: function auto (a: integer) {
            if (a < 10)
            {
                return a;
            }
            else
            {
                return 3.25;
            }
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(3.25))"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
        main: function void(){
            a: integer = func1() + 2.2;
        }
        func1: function auto(){
            return "string";
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
        main: function void(){
            a: integer = func1() + 2;
        }
        func1: function auto() inherit foo {
            return 0;
        }
        foo: function integer(){
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
        func1: function auto() inherit foo {
            super(20);
            x: integer = 20;
        }
        foo: function integer(inherit x: integer) {

        }
        main: function void(){
            a: integer = func1() + 2;
        }"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
        func1: function auto(a: integer) inherit foo {
            super(20);
            return a;
        }
        foo: function integer(inherit x: integer) {

        }
        main: function void(){
            a: integer = func1() + 2;
        }"""
        expect = "Type mismatch in expression: FuncCall(func1, [])"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
        fact: function integer (n: integer) {
            fact(2018);
        }
        main: function void() {
            delta: integer = fact(3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = """
        fact: function integer (n: integer) {
            if (n <= 1)
            {
                return 1;
            }
            return fact(n - 1) + fact(n - 2);
        }
        main: function void() {
            delta: integer = fact(3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = """
        foo: function auto () {
            return 2018;
        }
        main: function void() {
            delta: integer = foo();
            printInteger(delta);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
        x: boolean = true;
        foo: function auto () {
            return x;
        }
        main: function void() {
            delta: integer = foo();
            printInteger(delta);
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(delta, IntegerType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        input = """
        x: boolean = true;
        foo: function auto () {
            return x;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        input = """
        x: integer = 3;
        a: integer = readInteger();
        fact: function integer() 
        {

        }
        foo: function auto () {
            return a;
        }
        main: function void() {
            x = foo();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        input = """
        foo : function void (a : auto){}                  // Line 1
        main : function void () {
            foo(true);                                    // Line 3
            goo();                                        // Line 4
        }
        goo : function void (){                           // Line 6                    
            foo(3);                                       // Line 7
        } """
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        input = """
        foo: function void (a : auto) {}
        main: function void () {
            foo(2018);
            goo();
        }
        goo: function void (){                    
            foo(3);
        } """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        input = """
        foo: function void (a: auto) inherit goo {
            preventDefault();
        }
        main: function void () {
            foo(2018);
            goo(20);
        }
        goo: function void (inherit a: integer){                 
            foo(3);
        } """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        input = """
        foo: function void (a: auto) inherit goo {
            preventDefault();
            b = b + 1;
        }
        main: function void () {
            foo(2018);
            goo(20, 1998);
        }
        goo: function void (inherit a: integer, inherit b: integer){                 
            foo(3);
        } """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
        input = """
        a: array [3, 2] of integer = {{1, "2"}, {1, 2}, {1, 2}};
        main: function void () {

        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), StringLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_433(self):
        input = """
        foo: function integer(a: auto)
        {
            if (a < 20)
            {
                return 1;
            }
            return 2.7;
        }
        main: function void () {

        }"""
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(2.7))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = """
        foo: function integer(a: auto) inherit foo1
        {
            preventDefault();
            if (a < 20)
            {
                x: integer = 5;
                return x;
            }
            return 3;
        }
        foo1: function integer(inherit x: integer)
        {
            preventDefault();
        }
        main: function void () {

        }"""
        expect = "Invalid statement in function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
        foo: function integer(a: auto) inherit foo1
        {
            preventDefault();
            x: integer = 20;
            if (a < 20)
            {
                x: integer = 5;
                return x;
            }
            return x;
        }
        foo1: function integer(inherit x: integer)
        {

        }
        main: function void () {

        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = """
        main : function void() inherit foo {
            super(1.0, 2.0, 3.0);
            z: integer = foo(1, 2, 3) + 1;
            x = "abc";
            y = true;
        }
        foo : function auto(inherit x: auto, inherit y: auto, z: auto){
            return x + y + z;
        }"""
        expect = "Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = """
        main:function void() inherit foo {
            super(12);
            x:auto = foo(1);
            foo2();
            arr: array[2,2] of integer = {{1, 2.7}, {1,2}};
            arr[1,2] = 1;
        }
        foo:function float (x: integer){
            return x + 1.2;
        }
        foo2: function void(){}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), FloatLit(2.7)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = """
        foo : function void() {}
        foo : function auto ( a : integer , b : integer ) inherit bar {}
        main: function void() {}"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        input = """
        a: auto = foo(1, 2);
        foo: function auto() { }
        main: function void() {}"""
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        input = """
        x: auto = {4,5,6};
        y: auto = x[1,2];
        main: function void() {}"""
        expect = "Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        input = """
        foo: function float (out z: auto, t: auto)
        {
            z = 5;
            return z + t;
        }
        main: function void() {
            a: auto = foo(2.0, 2);
            b: auto = foo(3.0, 1);
            c: float = a + b;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        input = """
        foo: function boolean (n: integer)
        {
            if (n < 2)
            {
                return false;
            }
            if (n % 2 == 0)
            {
                return n == 2;
            }
            i: integer;
            for (i = 2, i * i <= n, 1)
            {
                if (n % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
        main: function void() {
            n: integer = readInteger();
            printBoolean(foo(n));
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        input = """
        main: function void() {
            n: integer = readInteger();
            printBoolean(foo(n));
        }
        foo: function void(n: integer) {}"""
        expect = "Type mismatch in expression: FuncCall(foo, [Id(n)])"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        input = """
        main: function void() {
            n: integer = readInteger();
            if (foo(n))
            {
                printInteger(n);
            }
            else
            {
                printInteger(1 + n);
            }
        }
        foo: function boolean(n: integer) {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = """
        main: function void() {
            n: float = readInteger();
            if (foo(n) && foo(n + 1))
            {
                printInteger(n);
            }
            else
            {
                printInteger(1 + n);
            }
        }
        foo: function boolean(n: float) {}"""
        expect = "Type mismatch in statement: CallStmt(printInteger, Id(n))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        input = """
        foo: function auto(a: auto, b: string) inherit bar {
            super(1, a, bar()); // 1
        }
        bar: function auto (x: auto, y: boolean, z: float) {}
        main: function void() {}"""
        expect = "Type mismatch in expression: FuncCall(bar, [])"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = """
        foo: integer = 2018;
        foo1: function auto()
        {
            return foo;
        }
        main: function void()
        {
            foo: auto = foo1();
            printBoolean(foo);
        }"""
        expect = "Type mismatch in statement: CallStmt(printBoolean, Id(foo))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = """i, j, k: integer = 20, 30, 40;
        main: function void()
        {
            i = j + k;
            printInteger(i);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """i, j, k: float = 2.75, 1.98, 3.17;
        main: function void()
        {
            t = i + j + k;
            printFloat(t);
        }"""
        expect = """Undeclared Identifier: t"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """i, j: string = \"Baba\", \"Mama\";
        main: function void()
        {
            k = j :: i;
            t = (k :: j) :: i;
            l = k :: (j :: i);
            printString(t);
            printString(l);
        }"""
        expect = """Undeclared Identifier: k"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """main: function void(){
            a[3 + 5, 2 * x] = y[4] - 7;
            return;
        }"""
        expect = """Undeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = """
        a: integer = 20;
        a: function void() {
            x: integer = 3;
        }"""
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """main: function void(){
            i: integer = 3;
            do
            {
                i = i + 1;
            }   
            while (i < 200);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        input = """main: function void(){
            i: integer = 3;
            do {
                i = i + 1;
            } while (i < 20);
            printInteger(i);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = """a: array[3] of float = {1, 2, 3};
        main: function void() {

        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        input = """foo: function void () inherit bar {
            if (a < b)
                if (c < d)
                    printString("True");
                else
                    printString("False");
        }
        main: function void() {}
        bar: integer = 2;"""
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = """main: function auto () { return; }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        input = """x: integer = 2018;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        decr: function void(out n: integer, delta: integer) {
            n = n - delta;
        }
        main: function void() {
            delta: integer = fact(3_2);
            decr(x, delta);
            printInteger(x);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = """main: function void () {
            a: array [2, 2] of float;
            i, j: integer;
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 2, j + 1) {
                    a[i, j] = readFloat();
                }
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        input = """main: function void () {
            a: array [2, 2] of float;
            i, j: integer;
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 2, j + 1) {
                    a[i, j] = readFloat();
                }
            }
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 2, j + 1) {
                    printFloat(a[i, j]);
                }
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        input = """x: integer = 2018;
        fibo: function integer (n: integer) {
            if (n <= 1) return 1;
            else return fibo(n - 1) + fibo(n - 2);
        }
        decr: function void(out n: integer, delta: integer) {
            n = n - delta;
        }
        main: function void() {
            delta: integer = fibo(100);
            decr(x, delta);
            printInteger(x);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        input = """main: function void() {
            a[0] = b[2, 3] + foo(2) + (b[0, 1] + goo(1));
            return;
        }"""
        expect = """Undeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = """a: integer = foo();
        foo: function string() { }
        main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = """a : integer = foo(1, 2);
        foo : function float (a : auto, b: auto) {
            a = "abc";
            b = "bcd";
            return a + b;
        }
        main: function void() {}"""
        expect = """Type mismatch in statement: AssignStmt(Id(a), StringLit(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        input = """a : integer = foo(1, 2);
        foo : function integer (a : auto, b: auto) {
            x: auto = a + b;
            return x;
        }
        main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
        input = """a: auto;
        main: function void() {}"""
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        input = """x: integer;
        y: float;
        z: boolean;
        goo: function void(x: integer, y: float) {

        }
        t: array[10] of float;
        foo: function auto() {

        }
        a: string = \"Hello World\";"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = """
        x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
        y: auto = x[0, 1+1-0];
        main: function void() {

        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = """
        goo: function void(a: auto, b: auto)
        {
            x: string = a + b;
        }
        main: function void() {}
        foo1: function void(inherit out a: integer) inherit foo {
            super(x, y, z);
        }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, BinExpr(+, Id(a), Id(b)))"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = """foo: function integer () {return 1;}
        x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
        y: auto = x[1, foo()];"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = """x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
        y: auto = x[2 < 3];
        main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(<, IntegerLit(2), IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """
        a: function integer (a: integer)
        {
            if (a <= 1)
            {
                return a;
            }
            return a(a - 1) + a(a - 2);
        }
        main: function void()
        {
            printInteger(a(2018));
        }"""
        expect = """Type mismatch in expression: FuncCall(a, [BinExpr(-, Id(a), IntegerLit(1))])"""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = """
        a: float = foo(1, 2) + 1.5;
        foo: function auto(a: integer, b: integer) {
            return a + b; 
        }
        main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        input = """
        main: function void () {
            a: integer = foo();//1
            b: float = "Error";//2
        }
        foo: function auto() {
            c: float = "Error";//3
            if("Error")//4
                return 123;//5
            else
                return 456;//6
            return "123"; //7
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(c, FloatType, StringLit(Error))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = """
        func1: function auto (d: integer, c: integer, e: auto) {
            g: integer = -e;
            f: integer = e;
        }
        main: function void () {
            a: integer = func1(2, 3, 2.9);
        }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(g, IntegerType, UnExpr(-, Id(e)))"""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input = """foo: function void(b: auto, c: auto)
        {
            a: integer = b + c == c;
        }
        main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(==, BinExpr(+, Id(b), Id(c)), Id(c)))"""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = """foo: function void (a: integer, b: integer, c: integer) {
            printInteger(a + 2 * b + 3 * c);
        }
        main: function void() {
            foo(2, 3, 4);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        input = """foo: function void (a: integer, b: integer) {
            c: integer = 2018;
            printInteger(a + 2 * b + 3 * c);
        }
        main: function void() {
            foo(2, 3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
        foo: function auto (b: integer, b: float) { 
	        return 3;
	        return "hello";
	        a: string = 123;
        }
        main: function void() {}"""
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """foo: function void (a: integer, b: integer) {
            i: integer;
            for (i = a, i <= b, i + 1) {
                c: integer = a + i;
                printInteger(c);
            }
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = """foo: function void () {
            do
            {
                printInteger(1);
            }   
            while (true);
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        input = """foo: function void () {
            while (true)
                break;
            return;
        }
        main: function void() {

        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = """foo: function void () {
            if (true) {
                if (!true) {

                }
                else return;
            }
            return;
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = """foo: function void () {
            if (!true) {
                if (true) {
                    a: integer = 10;
                    a = a + 1;
                    return;
                }
                else
                    return;
            }
            else {
                a: integer = 1;
                while (a < 20)
                    a = a + 1;
                printInteger(a);
            }
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = """foo: function array [10] of integer(a: array [10] of integer) {
            i: integer;
            for (i = 0, i < 10, i + 1) {
                a[i] = a[i] * 2 + 1;
            }
            return a;
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """foo: function void (out N: integer, i: integer) {
            j: integer;
            for (j = 0, j < i, j + 1) {
                if (N % j == 0) {
                    N = N - j;
                }
            }
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """foo1: function void (out N: integer, i: integer) {
            N = N * i;
        }
        main: function void() {
            N: integer = 2018;
            foo1(N, 3);
            printInteger(N);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        input = """foo1: function void (out s: string, N: integer) {
            i: integer;
            for (i = 0, i < N, i + 1) {
                temp: string = s[N - i - 1];
                s[N - i - 1] = s[i];
                s[i] = temp;
            }
        }
        main: function void() {}"""
        expect = """Type mismatch in expression: ArrayCell(s, [BinExpr(-, BinExpr(-, Id(N), Id(i)), IntegerLit(1))])"""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """
        inc : function void (a : integer) inherit foo{
            super("aa",2);
            a = 1::2;
        }
        foo : function auto (inherit n: float, inherit n: integer){

        }
        main: function void() {

        }"""
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """
        test1 : function string(y : auto) {
            y = 2; // line 2
            return "";
        }
        main: function void () {
            x: string = test1(true); // line 6
        }"""
        expect = """Type mismatch in statement: AssignStmt(Id(y), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """foo: function boolean (inherit out a: integer, b: float) inherit goo {}
        main: function void() {}"""
        expect = """Undeclared Function: goo"""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = """foo: function boolean (a: integer, b: float) {
            i: integer;
            for (i = 0, i < 5, i + 1) {
                x, y, z: integer = 10, 20, 30;
                return (x + a + y + b) > (y + a + z + b);
            }
        }
        main: function void() {

        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """foo1: function void (a: integer, b: float) {
            c: float = a + b;
            printFloat(c);
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """foo2: function void (a: integer) {
            printString(\"Test\");
            a = a + 1;
            printInteger(a);
        }
        main: function void() {
            foo2(10);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """a,b,c: boolean = true, false, true;
        main: function void() {
            a = b && c;
            printBoolean(a);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """foo: function void() {
            if (true)
            {
                a, b, c: integer = 10, 20, 30;
                printInteger(a + b + c);
            }
            else
            {
                x, y: float = 2.3e2, -2.3e2;
                printFloat(x + y);
            }   
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """a_20: boolean = (2 < 3) < 4;
        main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(<, BinExpr(<, IntegerLit(2), IntegerLit(3)), IntegerLit(4))"""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """foo: function string (a: string, b: integer) {
            return (a :: a[b]);
        }
        main: function void() {}"""
        expect = """Type mismatch in expression: ArrayCell(a, [Id(b)])"""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """x: integer = 65;
        y: function integer(x: integer) {
            return x + 1;
        }
        z: float = 65.20;
        t: function float(z: float) {
            return z * 2.0;
        }
        main: function void() {
            y: integer = y(x);
            t: float = t(z);
            printInteger(y);
            printFloat(t);
        }"""
        expect = """Type mismatch in expression: FuncCall(y, [Id(x)])"""
        self.assertTrue(TestChecker.test(input, expect, 499))