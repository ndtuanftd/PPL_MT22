import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):

        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 2010))

    def test_simple_program1(self):

        input = """ main: function void() {
                    a: integer = 1;
                } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program2(self):

        input = """main: function void() {
                    dividend, divisor, quotient, remainder: integer;
                    quotient = dividend / divisor;
                    remainder = dividend % divisor;
                printf("Quotient = %d\n", quotient);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program3(self):

        input = """main: function void() {
                printf("\n\n\t\tStudytonight - Best place to learn\n\n\n");
                    printf("\n\nNested loops are usually used to print a pattern in c. \n\n");
                    printf("\n\nThey are also used to print out the matrix using a 2 dimensional array. \n\n");

                    i,j,k: integer;
                    printf("\n\nOutput of the nested loop is :\n\n");
                    for(i = 0, i < 5, i+1)
                    {
                        printf("\t\t\t\t");
                        for(j = 0, j < 5, j+1)
                        printf("* ");

                        printf("\n");
                    }
                    printf("\n\n\t\t\tCoding is Fun !\n\n\n");
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_simple_program4(self):

        input = """main: function void() {
                    
                    i,j,k: integer;
                    i = 1;
                    while (i*5 < 100)
                    {
                        printf("\n");
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_simple_program5(self):

        input = """main: function void() {
            
                    c : string;
                    lowercase_vowel, uppercase_vowel: integer;
                    printf("Enter an alphabet: ");
                    scanf("%c", c);

                    // evaluates to 1 if variable c is a lowercase vowel
                    lowercase_vowel = c == "a";

                    // evaluates to 1 if variable c is a uppercase vowel
                    uppercase_vowel = c == "A";

                    // evaluates to 1 (true) if c is a vowel
                    if (lowercase_vowel || uppercase_vowel)
                        printf("%c is a vowel.", c);
                    else
                        printf("%c is a consonant.", c);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_simple_program6(self):

        input = """main: function void() {
                    i: integer = 10;     // declaration and initialization at the same time
                    do // do contains the actual code and the updation
                    {
                        printf("i = %d\n",i);
                        i = i-1;    // updation
                    }
                    // while loop doesn't contain any code but just the condition
                    while(i > 0);
                    printf("\n\The value of i after exiting the loop is %d\n\n", i);
                    printf("\n\n\t\t\tCoding is Fun !\n\n\n\'");
                    return 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_simple_program7(self):

        input = """main: function void() {
                sum , mean, SD: float;
                    i: integer;
                    for (i = 0, i < 10, i+1) {
                        sum = sum + data[i];
                    }
                    mean = sum / 10;
                    for (i = 0, i < 10, i+1) {
                        SD = SD + pow(data[i] - mean, 2);
                    }
                    return sqrt(SD / 10);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_simple_program8(self):

        input = """main: function void() {
                r, c: integer;
                // a[10,10], transpose[10,10] 
                
                a, transpose: array [10,10] of integer;

            printf("Enter rows and columns: ");
            scanf("%d %d", r, c);
                
            // asssigning elements to the matrix
            printf("\nEnter matrix elements:\n");
            for (i = 0, i < r, i+1)
            for (j = 0, j < c, j+1) {
                printf("Enter element a%d%d: ", i + 1, j + 1);
                scanf("%d", a[i,j]);
            }

            // printing the matrix a[][]
            printf("\nEntered matrix: \n");
            for (i= 0, i < r, i+1)
            for (j = 0, j < c, j+1) {
                printf("%d  ", a[i,j]);
                if (j == c - 1)
                printf("\n");
            }

            // computing the transpose
            for (i = 0, i < r, i+1)
            for (j = 0, j < c, j+1) {
                transpose[j,i] = a[i,j];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_simple_program9(self):

        input = """main: function void() {
            i,j,k: integer;
            for(i = 0, i < 5, i+1)
            {
                printf("\t\t\t\t");
                for(j = 0, j < 5, j+1)
                printf("* ");
        
                printf("\n");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_simple_program10(self):

        input = """main: function void() {
     number: integer;
     if(number < 100)
        printf("Number is less than 100!\n");
    else if(number == 100)
        printf("Number is 100!\n");
    else
        printf("Number is greater than 100!\n");

 
 }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_simple_program11(self):

        input = """printDivisors: function void(n: integer)
                {
                    i: integer;
                    for (i = 1, i <= n, i+1)
                        if (n % i == 0)
                            printf("%d ", i);
                }

                main: function void() {

                printDivisors(100);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_simple_program12(self):

        input = """primenumber: function void(number: integer)
                {
                    i: integer;
                    
                    // condition for checking the
                    // given number is prime or
                    // not
                    for (i = 2, i <= number / 2, i+1) {
                        if (number % i != 0)
                            continue;
                        else
                            return 1;
                    }
                    return 0;
                }

                main: function void() {
                    primenumber(100);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_simple_program13(self):

        input = """primenumber: function void(number: integer)
                {
                    i: integer;

                    a : boolean = false;
                    return a;
                }

                main: function void() {
                    primenumber(100);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_simple_program14(self):

        input = """main: function void() {
                    data: array [5] of integer;
                    for (i = 0, i < 5, i+1)
                        scanf("%d", data + i);
                    for (i = 0, i < 5, i+1)
                        printf("%d\n", (data + i));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_simple_program15(self):
        input = """main: function void() {
                r, s: integer;
                a, b: array [10] of integer;
                r = 4.0;
                s = r * myPI;
                a[0] = s;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_simple_program16(self):

        input = """main: function void() {
                    foo(123*321,"12323");
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_simple_program17(self):

        input = """main: function void() {
                    foo(123*321,"12323");
                    while (true) {
                    if (a < 1) break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_simple_program18(self):

        input = """main: function void() {
                    foo(123*321,"12323");
                    while (true) {
                    if (a < 1) break;
                    else continue;
                    }
                }"""       
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_simple_program19(self):

        input = """main: function void() {
                    foo(123*321,"12323");
                    while (true) 
                    if (a < 1) break;
                    else continue;
                    
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_simple_program20(self):

        input = """
                    main: function void() {
                    while (a < 100*3) {
                        writeInt(i);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_simple_program21(self):

        input = """foo: function integer(out a1: integer) { 
                    return 0;
                }
                main: function void() {
                    while (a < 100*3) {
                        writeInt(i);
                    }
                    foo(a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_simple_program22(self):

        input = """foo: function integer(out a1: auto) {
                    return 0;
                }
                main: function void() {
                    while (a < 100*3) {
                        writeInt(i);
                    }
                    foo(a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_simple_program23(self):

        input = """foo: function integer(out a1: auto, inherit a2: string) {
                    return 0;
                }
                main: function void() {
                    while (a < 100*3) {
                        writeInt(i);
                    }
                    foo(a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_simple_program24(self):

        input = """foo: function integer(out a1: auto, inherit out a2: float ) {
                    return 0;
                }
                main: function void() {
                    while (a < 100*3) {
                        writeInt(i);
                    }
                    foo(a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_simple_program25(self):

        input = """foo_parent: function integer() {
                    return 1;
                }
                foo: function integer(out a1: auto, inherit out a2: float ) inherit foo_parent {
                    return 0;
                }
                main: function void() {
                    while (a < 100*3) {
                        writeInt(i);
                    }
                    foo(a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_simple_program26(self):

        input = """foo_parent: function integer() {
                    return 1;
                }
                foo: function integer(out a1: auto, a2: boolean) inherit foo_parent {
                    return 0;
                }
                main: function void() {
                    while (a < 100*3) {
                        writeInt(i);
                    }
                    foo(a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_simple_program27(self):

        input = """foo_parent: function integer() {
                    return 1;
                }
                foo: function integer(out a1: auto, a2: array [10] of integer) inherit foo_parent {
                    return 0;
                }
                main: function void() {
                    while (a < 100*3) {
                        writeInt(i);
                    }
                    foo(a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_simple_program28(self):

        input = """main: function void() {
                    a: integer  = 1*2 + 3;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_simple_program29(self):

        input = """main: function void() {
                    a: integer  = 1*2+3;
                    str: string = "Number" :: "String";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_simple_program30(self):

        input = """main: function void() {
                    a: array [20] of integer;
                    a[10] = 1200*2;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_simple_program31(self):

        input = """main: function void() {
                    a: array [20] of integer;
                    a[10] = 1200*2;
                    
                    // if without else
                    if (a[10] < 100) a[10] = a[10]*100;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_simple_program32(self):

        input = """main: function void() {
                    a: array [20] of integer;
                    a[10] = 1200*2;
                    
                    // if with else
                    if (a[10] < 100) a[10] = a[10]*100;
                    else a[10] = 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_simple_program33(self):

        input = """main: function void() {
                    a: array [20] of integer;
                    a[10] = 1200*2;
                    // if out else
                    if (a[10] < 100) {
                        a[10] = a[10]*100;
                        a[1] = a[10];
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_simple_program34(self):

        input = """main: function void() {
            a,b,c,d: string= 2,2,3,4;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_simple_program35(self):

        input = """main: function void() {
                    a: array [20] of integer;
                    a[10] = 1200*2;
                    i: integer;
                    // if with else
                    if (a[10] < 100) {
                        a[10] = a[10]*100;
                        a[1] = a[10];
                        for (i = 0, i<10, i+1) {
                            printInteger(a[i]);
                        }
                    }
                    else a[10] = 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_simple_program36(self):

        input = """main: function void() {
                    a: array [20] of integer;
                    a[10] = 1200*2;
                    i: integer;
                    // if with else
                    if (a[10] < 100) {
                            a[10] = a[10]*100;
                            a[1] = a[10];
                            while( a < 20 ) {
                            printf("value of a: %d\n", a);
                            a=a+1;
                            if( a > 15) {
                                /* terminate the loop using break statement */
                                break;
                            }
                        }
                        }
                    else a[10] = 0;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_simple_program37(self):

        input = """a,b,c: integer = 3,4,6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_simple_program38(self):

        input = """main: function void() {
                    i,j,k: integer;
                    i = 0;   
                    while(i!=10)  
                    {  
                        printf("%d", i);   
                        continue;   
                        i=i+1;  
                    }  
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_simple_program39(self):

        input = """main: function void() {
                 foo(2 + x, 4.0 / y);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_simple_program40(self):

        input = """main: function void() {
            a,b,c,d,e: string= 2,2,3,4,6;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_simple_program41(self):

        input = """main: function void() {
                foo(2 + x, 4.0 / y);
                goo();
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_simple_program42(self):
        input = """main: function void() {
                foo(2 + x, 4.0 / y);
                goo();
                    if (a < 10) 
                        if (a>5)
                            print(a);
                    else print(a+1);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_simple_program43(self):

        input = """main: function void() {
                    foo(2 + x, 4.0 / y);
                    goo();
                      for (i[0] = 1, i[0] < 10, i[0]+1) {
                        print(":");
                      }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_simple_program44(self):

        input = """for (i[0] = 1, i[0] < 10, i[0]+1) 
        print(":");"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_simple_program45(self):

        input = """main: function void() {
                foo(2 + x, 4.0 / y);
                goo();
                      for (i = 1, i <= (n * (n + 1)) / 2, i+1) {
                        printf("%d ", i);
                        if (i == (j * (j + 1)) / 2) {
                            printf("\n");
                            j=j+1;
                        }
                    }
                      
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_simple_program46(self):

        input = """main: function void() {
                foo(2 + x, 4.0 / y);
                goo();
                    while (i <= (n * (n + 1)) / 2) {
                    printf("%d ", i);
                    // condition for what element has to print and
                        // how many times
                        if (i == (j * (j + 1)) / 2) {
                            printf("\n");
                            j=j+1;
                        }
                        i=i+1;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_simple_program47(self):

        input = """floyd: function void(n: integer)
                {
                    // base condition
                    if (n == 0)
                        return;
                    j: integer;
                    for (j = 1, j <= row, j+1)
                        printf("%d ", i+1);
                    row = row+1;
                    printf("\n");
                    floyd(n - 1);
                }
                main: function void() {
                foo(2 + x, 4.0 / y);
                goo();
                    floyd(6);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_simple_program48(self):

        input = """floyd: function void(inherit out n: integer)
                {
                    // base condition
                    if (n == 0)
                        return;
                    j: integer;
                    row = row+1;
                    printf("\n");
                    floyd(n - 1);
                }
                main: function void() {
                    foo(2 + x, 4.0 / y);
                    goo();
                     floyd(6);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_simple_program49(self):

        input = """checkYear: function boolean(year: integer)
                {
                    if (year % 400 == 0)
                        return true;
                    if (year % 100 == 0)
                        return false;
                    if (year % 4 == 0)
                        return true;
                    return false;
                }
                main: function void() {
                    print(checkYear(2023));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_simple_program50(self):

        input = """checkYear: function boolean(year: integer)
{
    return (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0));
}
main: function void() {
    print(checkYear(2023));
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_simple_program51(self):

        input = """fib: function integer(n: integer)
{
    if (n <= 1)
        return n;
    return fib(n - 1) + fib(n - 2);
}
main: function void() {
    print(fib(10));
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_simple_program52(self):

        input = """fib: function integer(n: integer)
                {
                    f: array [100] of integer;
                    i: integer;
                    f[0] = 0;
                    f[1] = 1;
                    for (i = 2, i <= n, i+1) {
                        f[i] = f[i - 1] + f[i - 2];
                    }
                    return f[n];
                }
                main: function void() {
                    print(fib(10));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_simple_program53(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_simple_program54(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           // if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           }
"""
        expect = "Error on line 5 col 11: else"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_simple_program55(self):

        input = """main: function void(){
     r, s: string;
     r = "hello";                        
     s = "world";
     a: array [2] of string;
     a = {"abc","xyz"};
     a[0] = 1::2*2;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_simple_program56(self):

        input = """main: function void(){
     r,e,t,y,d,s: integer = 1,2,3,4,5,6;
     r = r + e + t + y + d + s;                        
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_simple_program57(self):

        input = """foo: function void(a: integer, b: boolean){
    print("fadsf");     
}            
main: function void(){
x: integer = 0;
y: float = 1.2;
    foo(2 + x, 4.0 / y);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_simple_program58(self):

        input = """main: function void(){
   r, s, t, k: string = "heeloo", "woeirsdf", "asdtdg" , "asertd";
   r = r::(s::(t::k));  
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_simple_program59(self):

        input = """main: function void(){
    arr: array [5] of integer;
    arr = {1, 2, 3, 4, 5};
    i, sum: integer = 0, 0;
    avg: float;
    for (i = 0, i < 5, i+1) {
        sum = sum + arr[i] ;
    }
    avg = sum / 5;
    printString("Average = ");
    writeFloat(avg);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_simple_program60(self):

        input = """main: function void(){
    a: float = 9.34354;
    b: integer = 23445;
   for(i = 0 , i < 10, i+1){
        if((a > 1) && (b < 5))
        {
            while (1!=0){
                printString("acss");
                break;
            }
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_simple_program61(self):

        input = """main: function void() {
  printString("Enter an integer: ");
    num: integer = readInt();
    printInt(num);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_simple_program62(self):

        input = """ main: function void(){
    a, b, x: float;
    printString("Enter coefficients a and b: ");
    readFloat(a);
    readFloat(b);
    if (a == 0) {
        if (b == 0) {
            printString("The equation has infinite solutions.\\n");
        } else {
            printString("The equation has no solution.\\n");
        }
    } else {
        x = -b / a;
        writeFloat(x);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_simple_program63(self):

        input = """main: function void(){
    a, b, c, delta, x1, x2 : float = readFloat(), readFloat(), readFloat(), readFloat(), readFloat(), readFloat();  
    delta = b * b - 4 * a * c;
    if (delta < 0) {
        printString("The equation has no real roots.\\n");
    } else (delta == 0) {
        x1 = -b / (2 * a);
        printString("The only solution is: \\n");
    }
}"""
        expect = "Error on line 6 col 11: ("
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_simple_program64(self):

        input = """main: function void() {
            i, j, temp: integer;
            arr: array [5] of integer ;
            arr = {5, 4, 3, 2, 1};
            for (i = 0, i < 5 - 1, i+1) {
    for (j = i + 1, j < 5, j+1) {
        if (arr[i] > arr[j]) {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
}
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_simple_program65(self):

        input = """isPrime: function boolean(n: integer) {
  if(n <= 1) return false;
 
  for(i = 2, i <= n / 2, i+1) {
    if(n % i == 0) return false;
  }
 
  return true;
}          
                main: function void(){
                   
                }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_simple_program66(self):

        input = """main: function void(){      
                arr: array [4] of array;
                arr = {
                {1,2,3,4},{2,3,4,5},{3,4,5,6},{3,45,2,3}
                } ;    
                rows, cols : integer = 4,4;  
                i,j : integer;      
                    for(i = 0, i < rows, i+1) {
    for(j = 0, j < cols, j+1) {      
      arr[i][j] = 1;
    }
  }
                }
"""
        expect = "Error on line 2 col 34: array"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_simple_program67(self):

        input = """main: function void(){
     r,e,t,y,d,s: integer = 1,2,3,4,5,6;
    if((r+3 > t-3) && (e+y == d/s))
    {
    break;
    }                        
   
}

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_simple_program68(self):

        input = """xsadgf: float = 6.5;      
            asdf: function float (out t: float, x: float){
            x = readFloat();
            t = x* xsadgf;
            return t;
            }        
            printflo: function void(sdt: float){
            writeFloat(std);
            }
                main: function void(){                  
                    ddd, ff, et : float = 0.1, 2.2,3.2;
                    printflo(asdf(ddd-1+2*3, ff*et));
                   
                }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_simple_program69(self):

        input = """main: function void(){
                    printInt(12.3*(123e4 + 343 - 345/(3+5)))  ;
                }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_simple_program70(self):

        input = """main: function void(){
    x: array [3] of integer;
    x = {
    {1,2,3}, {3,4,5},{3,4,5}
    };
    x[0,0] = x [1,2] % x[2,2] ;
}

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_simple_program71(self):

        input = """main: function void(){
     r,e,t,y,d,s: integer = 1,2,3,4,5,6;
    if((r+3 > t-3) && (e+y == d/s))
    {
    break;
    }                        
   
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_simple_program72(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           /*else return n * fact(n - 1); */
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_simple_program73(self):

        input = """ main: function integer () {
         n: integer;
         n=readInteger();
           // if (n == 0) return 1;
           /*else return n * fact(n - 1); */
           }
           inc: function void(out n: integer, delta: integer) {
           n = n + delta;
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_simple_program74(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               break;
               }
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_simple_program75(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               break ; //add more space between "break" and ';'
               }
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_simple_program76(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               continue(); // add ()
               }
           }"""
        expect = "Error on line 11 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_simple_program77(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               if (i>3) {
               break;}
               else continue;
               }
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_simple_program78(self):

        input = """main: function integer () {
                 n: integer;
                 n=readInteger();
                   if (n == 0) return 1;
                   else
                       return n * fact(n - 1);
               }
               inc: function void( n: integer, delta: integer) {
                   n = n + delta;
                   while (n*delta>3||(n-delta<3)){
                       printInteger(n);
                       n = n *9 + 4 /3 % 7;
                       delta=delta+4;
                   }
               }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_simple_program79(self):

        input = """main: function integer () {
                 n: integer;
                 n=readInteger();
                   if (n == 0) return 1;
                   else
                       return n * fact(n - 1);
               }
               inc: function void( n: integer, delta: integer) {
                   n = n + delta;
                   check: boolean = false;
                   if (n>3&&(delta<3))
                       check=true;
                   while (n>3&&(delta<3)){
                       printInteger(n);
                       n--;
                       delta=delta+4;
                   }
               }
"""
        expect = "Error on line 15 col 24: -"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_simple_program80(self):

        input = """main: function integer () {
                 n: integer;
                 n=readInteger();
                   if (n == 0) return 1;
                   else
                       return n * fact(n - 1);
               }
               inc: function void( n: integer, delta: integer) {
                   n = n + delta;
                   check: boolean = false;
                   if ((n>3)&&(delta<3))
                       check=true;
                   else check = false;
                   while ((n>3)&&(delta<3)){
                       printInteger(n);
                       n = 8+9-3%8;
                       delta=delta+4;
                   }
               }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_simple_program81(self):

        input = """main: function integer () {
                 n: integer;
                 n=readInteger();
                   if (n == 0) return 1;
                   else
                       return n * fact(n - 1);
               }
               inc: function void( n: integer, delta: integer) {
                   n = n + delta;
                   check: boolean = false;
                   if (n>3 && (delta<3))
                       check=true;
                   else check = false;
                   while (n>3&&(delta<3)){
                       printInteger(n);
                       n = 8+9-3%8;
                       delta=delta+4;
                   }
               }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_simple_program82(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               if (i>3) break;
               }
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_simple_program83(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               continue;
               }
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_simple_program84(self):

        input = """main: function integer () {
         n: integer;
         // n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           }

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_simple_program85(self):

        input = """main: function void() {
           printValue(4);
       }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_simple_program86(self):

        input = """main: function void() {
           x: integer=123,456;
       }
"""
        expect = "Error on line 2 col 25: ,"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_simple_program87(self):

        input = """ main: function integer () {
         n: integer;
         // n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_simple_program88(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               }
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_simple_program89(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               break;
               }
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_simple_program90(self):

        input = """main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               break ; //add more space between "break" and ';'
               }
           }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_simple_program91(self):

        input = """main: function void(){
                    x: boolean = 1.4;
                    for (i = 1, i < 10, i + 1) {
                        if(i != 4)
                        x = x * i;
                        else
                        continue;
                    }
                    }

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_simple_program92(self):

        input = """main: function void(){
                    for (i = 1, i < 10, i + 1) {
                        if(i == 8) break;                    }
                }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_simple_program93(self):

        input = """main: function void() {
            a,b,c,d: string= 2,2,3,4;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_simple_program94(self):

        input = """ main: function void(){
                         r, s: integer;
                         r = 2.0;
                         a, b: array [5] of integer;
                         s = r * r * myPI;
                         a[0] = s;
                    }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_simple_program95(self):

        input = """x: string = "abcabc";
                add: function integer (n: string){
                    return n::"abc";                  
                }
               
                main: function void(){                    
                    printstring(add(x));
                }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_simple_program96(self):

        input = """main: function void() {
            a,b,c,d: string= 2,2,3,4;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_simple_program97(self):

        input = """x: integer;                
                main: function void(){
                    for (i = 1, i < 10, i + 1) {
                        if(i == 1)
                        { j: integer = i;
                        while(j < 10)
                        {
                        j = j+1;
                        }
                        }
                        else break;
                    }
                }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_simple_program98(self):

        input = """ main: function void(){
                    x: array [3] of string;
                    x = {"Kangxi", "Yongzheng", "Qianlong"};
                    for(i = 0 , i < 3, i + 1)
                    printString(x[i]);
                    }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_simple_program99(self):

        input = """printSring(){
                    x: array [3] of string;
                    x = {"Kangxi", "Yongzheng", "Qianlong"};
                }    
                main: function void(){
                    x: integer = 2;
                    if(x>=0) print(x);    
                    }
"""
        expect = "Error on line 1 col 12: {"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_simple_program100(self):

        input = """main: function void(){
                    x: integer = 2;
                    if(x>=0) print(x);
                printString("heello");    
                    }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
