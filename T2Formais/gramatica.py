program -> block
block -> lc decls stmts rc
decls -> decl decls | &
decl -> type id endl
type -> basic types
types -> lb num rb types | &
stmts -> stmt stmts | &
stmt -> loc attr bool endl | open_if | while lp bool rp stmt | do stmt while lp bool rp | break endl | block
open_if -> if lp bool rp then block else_if
else_if -> else block | &
loc -> id locs
locs -> lb bool rb locs | &
bool -> join bool*
bool* -> or bool | &
join -> equality join*
join* -> and join | &
equality -> rel equality*
equality* -> eq equality | dif equality | &
rel -> expr rel*
rel* -> lt expr | let expr | get expr | gt expr | &
expr -> term exprs
exprs -> plus expr | minus expr | &
term -> unary terms
terms -> mult term | div term | &
unary -> not unary | minus unary | factor
factor -> lp bool rp | loc | num | real | true | false