grammar TL;

//saltar tabs y spacaes
WS : [ \t\r\n]+ -> skip; 
COMMENTS : '#' [a-zA-Z0-9 ()]* -> skip;

programa : funcion_seccion module;


funcion_seccion: funcion funcion_seccion
			   | funcion
			   | 
			   |
			   ;
funcion : 'funcion' name '(' arg_declaracion ')'  block  retorno 'end' 'funcion' 
        | 'funcion' name '(' arg_declaracion ')'  retorno 'end' 'funcion'  ;
name : ID;
arg_declaracion: ID
			   | ID ',' arg_declaracion
			   ;
retorno: 'retorno' '(' sentence ')' 
	  | 
	  ;
			   
block: assignment
     | escribir
	 | leer
	 | bucle
	 | si_bloque
	 | mientras
	 | sentence
	 ;			
sentence : expresion_condicional
		| callfunc
		| array
		| dicc
		| call_array;
		
module : block module
	   | importar module
	   |
	   ;
	  
importar: 'import' id_import
	    | 'desde' ID 'import' ID;
id_import : '.' id_import
		  | ID;

assignment : assign ; 

assign : ID '=' sentence
	   | call_array '=' sentence
	   //| call_dir '=' sentence
	   | ID '=' assign
	   | call_array '=' assign;
	   //| call_dir '=' assign ;

escribir : 'log' '(' sentence ')';
leer : 'leer' '(' sentence ')';


expresion_condicional : expresion_logica_or;

expresion_logica_or : expresion_logica_and
                    | expresion_logica_or '||' expresion_logica_and ;
					
expresion_logica_and : expresion_igualdad
                     | expresion_logica_and '&&' expresion_igualdad ;
					 
expresion_igualdad : expresion_relacional
                   | expresion_igualdad '==' expresion_relacional
                   | expresion_igualdad '!=' expresion_relacional ;

expresion_relacional : expresion_aditiva
				     | expresion_relacional '<' expresion_aditiva
                     | expresion_relacional '>' expresion_aditiva
                     | expresion_relacional '<=' expresion_aditiva
                     | expresion_relacional '>=' expresion_aditiva ;

expresion_aditiva : expresion_multiplicativa
				  | '-' expresion_multiplicativa
                  | expresion_aditiva '+' expresion_multiplicativa
                  | expresion_aditiva '-' expresion_multiplicativa ;
				  
expresion_multiplicativa : expresion_primaria
                         | expresion_multiplicativa '*' expresion_primaria
                         | expresion_multiplicativa '/' expresion_primaria
                         | expresion_multiplicativa '%' expresion_primaria ;

expresion_primaria : INT
				   | DOUBLE
				   | ID
				   | STRING 
				   | call_dir
				   | call_array
				   | '(' expresion_condicional ')';
				  
call_dir : ID '.' call_dir_it;
call_dir_it : ID '.' call_dir_it
            | ID;
			
call_array: ID '[' call_array_it ']';
call_array_it: expresion_aditiva ',' call_array_it
			 | expresion_aditiva;
			 
array : '[' arrele ']'; 
arrele : sentence
	   | sentence ',' arrele;
	 
dicc : '{' diccele '}'; 
diccele : ID ':' sentence
	   | ID ':' sentence ',' diccele;
			
INT : [0-9]+ ;
DOUBLE : [0-9]+ '.' [0-9]+;
STRING : '"'  [a-zA-Z0-9=: ]* '"';
ID : [a-zA-Z][a-zA-Z0-9]*;
alfabeto: '=';


callfunc : ID '(' parametros ')';
parametros : sentence
		   | sentence ',' parametros;

bucle : 'for' ID 'in' iter '{' module '}'
      | 'for' ID 'in' iter  '{' module '}'
	  | 'for' ID 'in' iter  block ;
	  
si_bloque : si  sino_si  sino
		  | si sino_si  sino
		  | si  sino_si sino
		  | si sino_si sino;
si : 'if' '(' expresion_condicional ')' '{' module '}'
   | 'if' '(' expresion_condicional ')'  module ;   
sino_si : 'else' 'if' '(' expresion_condicional ')' '{'  module '}' sino_si
     | 'else' 'if' '(' expresion_condicional ')'  module sino_si
     | 'else' 'if' '(' expresion_condicional ')'  '{'  module '}' sino_si
     | 
	 ;
sino : 'else' '{' module '}'
	 | 'else'  '{' module '}'
     | 'else'  module
     |
	 ;

iter : array
     | ID;

mientras : 'while' '(' expresion_condicional ')' '{' module '}'
      | 'while' '(' expresion_condicional ')'  '{' module '}'
      | 'while' '(' expresion_condicional ')'  module;
	  

 



