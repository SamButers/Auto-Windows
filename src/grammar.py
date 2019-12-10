from lark import Lark, Tree, Token

# Truque para fazer as árvores mostrarem no modo "pretty" por padrão
Tree._repr_html_ = lambda t: '<pre>%s</pre>' % t.pretty()

grammar = Lark(r"""
start: function+

?function: VAR_NAME VAR_NAME "(" (declaration ("," declaration)*)? ")" scope

// Separation into argument for better organization in parsing
// No default initialization added yet
?argument: VAR_NAME VAR_NAME -> argument

scope: "{" statements statements* "}"

?statements: s_statement ";"
           | ns_statement

// Semi-colon Statement
?s_statement: declaration
            | assignment
            | return
            | expression

// No Semi-colon Statement
?ns_statement: loop
             | conditional

// The only allowed ASSIGN_OP in the declaration should be "=" (treated here)
?declaration: VAR_NAME VAR_NAME (/=/ expression)?

?assignment: VAR_NAME ASSIGN_OP expression
           | VAR_NAME INCREMENT_OP  -> post_increment
           | INCREMENT_OP VAR_NAME  -> pre_increment

?expression: expression PLUS_OP term -> binary_operation
           | term
      
?term : expression MUL_OP term -> binary_operation
      | pow
      
?pow  : atom POW_OP pow -> binary_operation
      | atom

return: "return" expression? -> return_expression

?loop: count
     | while
     | for

// Declaration cannot have assignment (not treated here)
// VALUES need to be FLOAT or INTEGER or result in one of those (not treated here)
?count: "count" (VAR_NAME|declaration)? "from" expression "to" expression scope

?while: "while" ((conditions)|("(" conditions ")")) scope -> while_loop

// Not all statements are allowed, such as return, loops or conditionals (treated here)
// ?for: "for" (declaration|assignment|expression)? ";" conditions ";" (declaration|assignment|expression)? scope -> for_loop
//    | "for" "(" (declaration|assignment|expression)? ";" conditions ";" (declaration|assignment|expression)? ")" scope -> for_loop

?for: "for" ";" conditions ";" scope -> minimal_for
    | "for" "(" ";" conditions ";" ")" scope -> minimal_for
    | "for" (declaration|assignment|expression) ";" conditions ";" scope -> left_for
    | "for" "(" (declaration|assignment|expression) ";" conditions ";" ")" scope -> left_for
    | "for" ";" conditions ";" (declaration|assignment|expression) scope -> right_for
    | "for" "(" ";" conditions ";" (declaration|assignment|expression) ")" scope -> right_for
    | "for" (declaration|assignment|expression) ";" conditions ";" (declaration|assignment|expression) scope -> for_loop
    | "for" "(" (declaration|assignment|expression) ";" conditions ";" (declaration|assignment|expression) ")" scope -> for_loop

// Switch pending
?conditional: if

?if: "if" ((conditions)|("(" conditions ")")) scope else? -> if_conditional

?else: "else" (if|scope) -> else_conditional

?conditions: condition (LOGICAL_OP conditions)*
           | "(" condition (LOGICAL_OP conditions)* ")"

?condition: expression (COMP_OP expression)?
          | expression COMP_OP expression COMP_OP expression

// (2 + 3) * x not working
atom: INTEGER
     | FLOAT
     | STRING
     | CHARACTER
     | BOOLEAN
     | VAR_NAME
     | call
     | "(" expression ")"

?call: VAR_NAME "(" (expression ("," expression)*)? ")"

// VAR_NAME refers to variables, function (which are variables as well) names and types.
// Terminals
INTEGER : /-?\d+/
FLOAT   : /-?\d+\.\d+/
STRING  : /"[^"]*"/
CHARACTER : /'[^']([^'])?'/
BOOLEAN : /(TRUE)|(FALSE)/
VAR_NAME: /[A-Za-z]\w*/

// ARITH_OP: /[\+-\*\/%\^]/

PLUS_OP: /[\+-]/
MUL_OP : /[\/*]/
POW_OP : /\^/
COMP_OP : /(==)|(!=)|(>=)|(<=)|(>)|(<)/
ASSIGN_OP : /=|(\+=)|(-=)|(\*=)|(\/=)|(&=)/
INCREMENT_OP: /(\+\+)|(--)/
LOGICAL_OP: /AND|OR|!/


%ignore /\s+/
""")