// 1953073
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
    language=Python3;
}

program: (decl)+  EOF ; // Start variable

/*
*********************************************
        PARSER RULES
*********************************************
*/


/* declaration */
decl: vardecl | fundecl  ;
// x: integer;
// x, y: integer;
// x, y, z: integer = 1,2,3;
//vardecl: idList COLON (atomicType|arrayDecl) (ASSIGN exprList)? SM
//    {
//        nID = $idList.text.split(',')
//        print("Number of ID is: ", len(nID))
//    }
//    ;
//vardecl: ID COLON atomicType vardecl ASSIGN expr0 SM
//    ;

vardecl: (vardecl_wo_asg|vardecl_w_asg) SM
    ;
vardecl_wo_asg: idList COLON varType
    ;
vardecl_w_asg: ID COMMA vardecl_w_asg COMMA expr
    | ID COLON varType ASSIGN expr
    ;

//vardecl: ID COMMA vardecl '=' expr0;


// <identifier>: function <return-type> (<paramter-list>) [inherit <function-name>]?
fundecl: ID COLON FUNCTION fnType paramdecl fun_inherit_subpart? block_stm
    ;
//fun_prototype: ID COLON FUNCTION fnType paramdecl fun_inherit_subpart?
//    ;

paramdecl: LB paramlist RB
    ;
paramlist: params?
    ;
params: param COMMA params | param
    ;
param: INHERIT? OUT? ID COLON varType
    ;

fun_inherit_subpart: INHERIT ID
    ;

/* 7. statement */
stm: ifStm | agnStm  | forStm | block_stm | whileStm | doWhileStm | breakStm
    | continueStm | returnStm | callStm
    ;

agnStm: (ID|indexOp) ASSIGN expr SM
    ;
// 7.2 if statement
ifStm: IF LB expr RB stm false_stm?
    ;
false_stm: ELSE stm
    ;
//
//ifStm: matchStm
//    | unMatchStm
//    ;

//matchStm: IF LB expr RB matchStm (ELSE matchStm)?
//    | otherStm
//    ;
//
//unMatchStm: IF LB expr RB stm
//    | IF LB expr RB matchStm (ELSE unMatchStm)?
//    ;
funCall: ID LB exprList? RB
    ;

// 7.3 for statement
forStm: FOR LB scalar_variable ASSIGN expr COMMA condition_expr COMMA update_expr  RB stm
    ;
scalar_variable: ID |indexOp ;   // TODO: only for type int
condition_expr: expr;  // TODO: Should be boolean type
update_expr: expr;     // TODO: UNARY operator
block_stm: LCB (block_body)* RCB
    ;
block_body: stm | vardecl
    ;

// 7.4 While statement
whileStm: WHILE LB condition_expr RB stm?
    ;

doWhileStm: DO block_stm WHILE LB condition_expr RB SM
    ;

breakStm: BREAK SM;
continueStm: CONTINUE SM;
returnStm: RETURN expr? SM;
callStm: ID LB exprList? RB SM;




/* expression */

// 6.7 Precedence and associativity
exprList: expr COMMA exprList | expr
    ;

// Binary
expr: expr1 STRINGCONCAT expr1 | expr1
    ;
expr1: expr2 relational_op expr2 | expr2
    ;
expr2: expr2 (ANDOP | OROP) expr3 | expr3
    ;
expr3: expr3 (ADDOP | SUBOP) expr4 | expr4
    ;
expr4: expr4 (MULOP | DIVOP | MODOP) expr5 | expr5
    ;

// Uniary
expr5: NEGOP expr5 | expr6
    ;
expr6: SUBOP expr6 | expr7
    ;
//expr7:  operandexpr7 COMMA | operand // index expression
//    ;

expr7:  indexOp | operand // index expression
    ;

operand: INTLIT
    | FLOATLIT
    | BOOLLIT
    | arrLit
    | STRINGLIT
    | ID
    | funCall
    | LB expr RB
    | indexOp
    ;

idList: ID COMMA idList
    | ID
    ;


// array literal
//arrLit: LCB (exprList|arrLit)? RCB
arrLit: LCB (exprList|arrLit)? RCB
    ;
//arrEles: int_list
//    | float_list
//    | bool_list
//    | string_list
//    ;
//int_list: INTLIT COMMA int_list | INTLIT
//    ;
//float_list: FLOATLIT COMMA float_list | FLOATLIT
//    ;
//bool_list: BOOLLIT COMMA bool_list | BOOLLIT
//    ;
//string_list: STRINGLIT COMMA string_list | STRINGLIT
//    ;

// 4. type
//// 4.1 atomic type
atomicType: INT | FLOAT | BOOLEAN | STRING
    ;


//boolType: 'boolType'
//    ;
//intType: 'intType'
//   ;
//floatType: 'floatType'
//   ;
//stringType: '::'
//   ;
varType: atomicType | AUTO | arrTypeDecl
   ;

fnType: atomicType | VOID | AUTO | arrTypeDecl
    ;

arrTypeDecl: ARRAY LSB exprList RSB OF atomicType
    ;

//// 4.3 Void type
//voidType: VOID
//   ;
//// 4.4 Auto type
//autoType: AUTO
//   ;

//
//intOp:
//    | ADDOP
//    | SUBOP
//    | MULOP
//    | DIVOP
//    | MODOP
//    | EQOP
//    | NEQOP
//    | LTOP
//    | GTOP
//    | LEOP
//    | GEOP
//    ;
//
//floatOp:
//    | ADDOP
//    | SUBOP
//    | MULOP
//    | DIVOP
//    | LTOP
//    | GTOP
//    | LEOP
//    | GEOP
//    ;
//
//boolOp: NEGOP
//    | ANDOP
//    | OROP
//    | EQOP
//    | NEQOP
//    ;
//
//stringConcat: STRINGCONCAT
//    ;

indexOp: ID LSB exprList RSB
    ;

indexList: INTLIT COMMA indexList | INTLIT
    ;


//
//rUnaryOp: SUBOP  // right assosicative unary
//    | NEGOP
//    ;
//binOp: MULOP
//    | DIVOP
//    | MODOP
//    | ADDOP
//    | SUBOP
//    | ANDOP
//    | OROP
//    | EQOP
//    | NEQOP
//    | LTOP
//    | GTOP
//    | GEOP
//    | LEOP
//    | STRINGCONCAT
//    ;
//
relational_op: EQOP
    | NEQOP
    | LEOP
    | GTOP
    | LTOP
    | GEOP
    ;
//
//fragment REL_OP: EQOP
//    | NEQOP
//    | LEOP
//    | GTOP
//    | LTOP
//    | GEOP
//    ;

/*
*********************************************
        LEXER RULES FOR TOKENS
***********************************************
*/

/* 3.4 Keyword*/
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
FLOAT: 'float';
ELSE: 'else';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INT: 'integer';
RETURN: 'return';
STRING: 'string';
WHILE:'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';
//READINT: 'readInteger';
//PRINTINT:'printInteger';
//READFLOAT:'readFloat';
//PRINTFLOAT:'printFloat';
//READBOOL:'readBoolean';
//PRINTBOOL:'printBoolean';
//READSTRING:'readString';
//PRINTSTRING:'printString';



//TEXT: ~[\\"]+;
//INSTRING: CHARACTER*
//    ;
//
//CHARACTER: TEXT
//    | '\b'
//    | '\f'
//    | '\r'
//    | '\n'
//    | '\t'
//    | '\''
//    | '\\'
//    | INNERSTRING
//    ;
//
//INNERSTRING: 'innerString'
//    ;

/* 3.5 Operator*/
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
NEGOP: '!';
ANDOP: '&&';
OROP: '||';
EQOP: '==';
NEQOP: '!=';
LTOP: '<';
LEOP: '<=';
GTOP: '>';
GEOP: '>=';
STRINGCONCAT: '::';

/* 3.6 Seperator */
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
DOT: '.';
COMMA: ',';
SM: ';';
COLON: ':';
ASSIGN: '=';
DOUBLEQUOTE: '"';


BOOLLIT: 'true'
    | 'false'
    ;

fragment DIGIT: [0-9];
fragment ZERO: '0';



// 3.7 Literals
INTLIT: ZERO
    | [1-9]('_'?DIGIT)*
    {
        self.text = self.text.replace('_', '')
    }
    ;

//INTLIT: DIGIT | [1-9] DIGIT | ([1-9] | [1-9] [0-9_] DIGIT) ([1-9] [0-9_] DIGIT | DIGIT)* {self.text = self.text.replace('_' , '')};




//    FLOATLIT:
//        (INTLIT DECIMAL EXPORNENT?
//        | INTLIT DECIMAL? EXPORNENT
//        | INTLIT? DECIMAL EXPORNENT)
//        {
//            self.text = self.text.replace('_', '')
//        }
//        ;
fragment DECIMAL: DOT DIGIT*
    ;
fragment EXPORNENT: [eE][+-]?INTLIT;

FLOATLIT:
(INTLIT DOT DIGIT* EXPORNENT?
| DOT DIGIT* EXPORNENT?
| INTLIT EXPORNENT)
{
    self.text = self.text.replace('_', '')
}
;


//STRINGLIT: '"' SUB_STRING* '"' {self.text = self.text[1:-1]}
//    ;

fragment ESC_SEQ: '\\' [bfrnt"'\\];
//fragment SUB_STRING: ( '\\' [btnfr"'\\] | ~["\\\b\t\f\r\n] )*   ;
fragment SUB_STRING: ( '\\' [btnfr"'\\] | ~["\\] )*   ;

STRINGLIT: DOUBLEQUOTE SUB_STRING DOUBLEQUOTE
    {
        self.text = self.text[1:-1]
    }
    ;
// 3.3 Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*; // define identifier

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
BLOCKCOMMENT:'/*' .*? '*/' -> skip;
LINECOMMENT: '//' ~[\r\n]* -> skip;


ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' ( '\\' [btnfr"'\\] | ~[\b\t\f\r\n\\'"] )*
    {
        self.text = self.text[1:]
        raise UncloseString(self.text)
    };

ILLEGAL_ESCAPE: '"' .*? ESCAPE .*?
    {
        self.text = self.text[1:]
        raise IllegalEscape(self.text)
    };
//
//UNCLOSE_STRING: DOUBLEQUOTE SUB_STRING {raise UncloseString(self.text[1:])};
//ILLEGAL_ESCAPE: DOUBLEQUOTE SUB_STRING ('\\' ~[btnfr"'\\])* {raise IllegalEscape(self.text[1:])};

fragment ESCAPE: [\r\n\b\f\t'"\\];
