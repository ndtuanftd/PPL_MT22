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
decl: vardecl | fundecl ;
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
fundecl: fun_prototype block_stm
    ;
fun_prototype: ID COLON FUNCTION fnType paramdecl fun_inherit_subpart?
    ;
fun_inherit_subpart: INHERIT ID
    ;
paramdecl: LB paramlist RB
    ;
paramlist: params?
    ;
params: param COMMA params | param
    ;
param: INHERIT? OUT? ID COLON varType
    ;



/* 7. statement */
stm: agnStm | ifStm | forStm | block_stm | whileStm | doWhileStm | breakStm
    | continueStm | returnStm | callStm
    ;

agnStm: (ID|indexOp) ASSIGN expr SM
    ;
// 7.2 if statement
ifStm: IF LB expr RB stm false_stm?
    ;
false_stm: ELSE stm
    ;

funCall: ID LB exprList? RB
    ;

// 7.3 for statement
forStm: FOR LB scalar_variable ASSIGN expr0 COMMA condition_expr COMMA update_expr  RB stm
    ;
scalar_variable: ID |indexOp ;   // TODO: only for type int
condition_expr: expr;  // TODO: Should be boolean type
update_expr: expr;     // TODO: UNARY operator
block_stm: LCB (stm | vardecl)* RCB
    ;


// 7.4 While statement
whileStm: WHILE LB condition_expr RB stm?
    ;

doWhileStm: DO block_stm WHILE LB condition_expr RB SM
    ;

breakStm: BREAK SM;
continueStm: CONTINUE SM;
returnStm: RETURN expr? SM;
callStm: funCall SM;




/* expression */

// 6.7 Precedence and associativity
exprList: expr COMMA exprList | expr
    ;
expr: expr0 STRINGCONCAT expr0 | expr0
    ;
expr0: expr1 STRINGCONCAT expr1 | expr1
    ;
expr1: expr2 relational_op expr2 | expr2
    ;
expr2: expr2 (ANDOP | OROP) expr3 | expr3
    ;
expr3: expr3 (ADDOP | SUBOP) expr4 | expr4
    ;
expr4: expr4 (MULOP | DIVOP | MODOP) expr5 | expr5
    ;
expr5: NEGOP expr5 | expr6
    ;
expr6: SUBOP expr6 | expr7
    ;
expr7: operand LSB exprList RSB | operand // index expression
    ;

operand: INTLIT
    | FLOATLIT
    | BOOLLIT
    | STRINGLIT
    | ID
    | arrLit
    | funCall
    | LB expr RB
    ;

idList: ID COMMA idList
    | ID
    ;


// array literal
arrLit: LCB (exprList|arrLit)? RCB
    ;
arrEles: int_list
    | float_list
    | bool_list
    | string_list
    ;
int_list: INTLIT COMMA int_list | INTLIT
    ;
float_list: FLOATLIT COMMA float_list | FLOATLIT
    ;
bool_list: BOOLLIT COMMA bool_list | BOOLLIT
    ;
string_list: STRINGLIT COMMA string_list | STRINGLIT
    ;

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

arrTypeDecl: ARRAY LSB indexList RSB OF atomicType
    ;

//// 4.3 Void type
//voidType: VOID
//   ;
//// 4.4 Auto type
//autoType: AUTO
//   ;


intOp:
    | ADDOP
    | SUBOP
    | MULOP
    | DIVOP
    | MODOP
    | EQOP
    | NEQOP
    | LTOP
    | GTOP
    | LEOP
    | GEOP
    ;

floatOp:
    | ADDOP
    | SUBOP
    | MULOP
    | DIVOP
    | LTOP
    | GTOP
    | LEOP
    | GEOP
    ;

boolOp: NEGOP
    | ANDOP
    | OROP
    | EQOP
    | NEQOP
    ;

stringConcat: STRINGCONCAT
    ;

indexOp: ID LSB (indexList | exprList) RSB
    ;

indexList: INTLIT COMMA indexList | INTLIT
    ;



rUnaryOp: SUBOP  // right assosicative unary
    | NEGOP
    ;
binOp: MULOP
    | DIVOP
    | MODOP
    | ADDOP
    | SUBOP
    | ANDOP
    | OROP
    | EQOP
    | NEQOP
    | LTOP
    | GTOP
    | GEOP
    | LEOP
    | STRINGCONCAT
    ;

relational_op: EQOP
    | NEQOP
    | LEOP
    | GTOP
    | LTOP
    | GEOP
    ;

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



// 3.7 Literals
FLOATLIT:
    (INTLIT DOT DIGIT* EXPORNENT?
//    | DOT DIGIT+ EXPORNENT?
    | INTLIT EXPORNENT)
    {
        self.text = self.text.replace('_', '')
    }
    ;
fragment EXPORNENT: [eE][+-]?DIGIT+;
INTLIT: ZERO
    | [1-9]('_'?DIGIT)*
    {
        self.text = self.text.replace('_', '')
    }
    ;
BOOLLIT: 'true'
    | 'false'
    ;

STRINGLIT: '"' ( '\\' . | ~["\\] )* '"'
    {
        self.text = self.text[1:-1]
    }
    ;

//STRINGLIT: '"' SUB_STRING* '"' {self.text = self.text[1:-1]}
//    ;

fragment ESC_SEQ: '\\' [bfrnt'\\] | '\'"';
fragment SUB_STRING: ~[\b\f\r\n\t'"\\] | ESC_SEQ;

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





fragment DIGIT: [0-9];
fragment ZERO: '0';

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
fragment ESCAPE: [\r\n\b\f\t'"\\];
