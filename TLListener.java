// Generated from TL.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TLParser}.
 */
public interface TLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TLParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(TLParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(TLParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#funcion_seccion}.
	 * @param ctx the parse tree
	 */
	void enterFuncion_seccion(TLParser.Funcion_seccionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#funcion_seccion}.
	 * @param ctx the parse tree
	 */
	void exitFuncion_seccion(TLParser.Funcion_seccionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#funcion}.
	 * @param ctx the parse tree
	 */
	void enterFuncion(TLParser.FuncionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#funcion}.
	 * @param ctx the parse tree
	 */
	void exitFuncion(TLParser.FuncionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#name}.
	 * @param ctx the parse tree
	 */
	void enterName(TLParser.NameContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#name}.
	 * @param ctx the parse tree
	 */
	void exitName(TLParser.NameContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#arg_declaracion}.
	 * @param ctx the parse tree
	 */
	void enterArg_declaracion(TLParser.Arg_declaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#arg_declaracion}.
	 * @param ctx the parse tree
	 */
	void exitArg_declaracion(TLParser.Arg_declaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#retorno}.
	 * @param ctx the parse tree
	 */
	void enterRetorno(TLParser.RetornoContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#retorno}.
	 * @param ctx the parse tree
	 */
	void exitRetorno(TLParser.RetornoContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(TLParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(TLParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#sentence}.
	 * @param ctx the parse tree
	 */
	void enterSentence(TLParser.SentenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#sentence}.
	 * @param ctx the parse tree
	 */
	void exitSentence(TLParser.SentenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#module}.
	 * @param ctx the parse tree
	 */
	void enterModule(TLParser.ModuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#module}.
	 * @param ctx the parse tree
	 */
	void exitModule(TLParser.ModuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#importar}.
	 * @param ctx the parse tree
	 */
	void enterImportar(TLParser.ImportarContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#importar}.
	 * @param ctx the parse tree
	 */
	void exitImportar(TLParser.ImportarContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#id_import}.
	 * @param ctx the parse tree
	 */
	void enterId_import(TLParser.Id_importContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#id_import}.
	 * @param ctx the parse tree
	 */
	void exitId_import(TLParser.Id_importContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(TLParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(TLParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#escribir}.
	 * @param ctx the parse tree
	 */
	void enterEscribir(TLParser.EscribirContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#escribir}.
	 * @param ctx the parse tree
	 */
	void exitEscribir(TLParser.EscribirContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#leer}.
	 * @param ctx the parse tree
	 */
	void enterLeer(TLParser.LeerContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#leer}.
	 * @param ctx the parse tree
	 */
	void exitLeer(TLParser.LeerContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#expresion_condicional}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_condicional(TLParser.Expresion_condicionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#expresion_condicional}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_condicional(TLParser.Expresion_condicionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#expresion_logica_or}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_logica_or(TLParser.Expresion_logica_orContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#expresion_logica_or}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_logica_or(TLParser.Expresion_logica_orContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#expresion_logica_and}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_logica_and(TLParser.Expresion_logica_andContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#expresion_logica_and}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_logica_and(TLParser.Expresion_logica_andContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#expresion_igualdad}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_igualdad(TLParser.Expresion_igualdadContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#expresion_igualdad}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_igualdad(TLParser.Expresion_igualdadContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#expresion_relacional}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_relacional(TLParser.Expresion_relacionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#expresion_relacional}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_relacional(TLParser.Expresion_relacionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#expresion_aditiva}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_aditiva(TLParser.Expresion_aditivaContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#expresion_aditiva}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_aditiva(TLParser.Expresion_aditivaContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#expresion_multiplicativa}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_multiplicativa(TLParser.Expresion_multiplicativaContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#expresion_multiplicativa}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_multiplicativa(TLParser.Expresion_multiplicativaContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#expresion_primaria}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_primaria(TLParser.Expresion_primariaContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#expresion_primaria}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_primaria(TLParser.Expresion_primariaContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#call_dir}.
	 * @param ctx the parse tree
	 */
	void enterCall_dir(TLParser.Call_dirContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#call_dir}.
	 * @param ctx the parse tree
	 */
	void exitCall_dir(TLParser.Call_dirContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#call_dir_it}.
	 * @param ctx the parse tree
	 */
	void enterCall_dir_it(TLParser.Call_dir_itContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#call_dir_it}.
	 * @param ctx the parse tree
	 */
	void exitCall_dir_it(TLParser.Call_dir_itContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#call_array}.
	 * @param ctx the parse tree
	 */
	void enterCall_array(TLParser.Call_arrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#call_array}.
	 * @param ctx the parse tree
	 */
	void exitCall_array(TLParser.Call_arrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#call_array_it}.
	 * @param ctx the parse tree
	 */
	void enterCall_array_it(TLParser.Call_array_itContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#call_array_it}.
	 * @param ctx the parse tree
	 */
	void exitCall_array_it(TLParser.Call_array_itContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(TLParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(TLParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#arrele}.
	 * @param ctx the parse tree
	 */
	void enterArrele(TLParser.ArreleContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#arrele}.
	 * @param ctx the parse tree
	 */
	void exitArrele(TLParser.ArreleContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#dicc}.
	 * @param ctx the parse tree
	 */
	void enterDicc(TLParser.DiccContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#dicc}.
	 * @param ctx the parse tree
	 */
	void exitDicc(TLParser.DiccContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#diccele}.
	 * @param ctx the parse tree
	 */
	void enterDiccele(TLParser.DicceleContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#diccele}.
	 * @param ctx the parse tree
	 */
	void exitDiccele(TLParser.DicceleContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#alfabeto}.
	 * @param ctx the parse tree
	 */
	void enterAlfabeto(TLParser.AlfabetoContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#alfabeto}.
	 * @param ctx the parse tree
	 */
	void exitAlfabeto(TLParser.AlfabetoContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#callfunc}.
	 * @param ctx the parse tree
	 */
	void enterCallfunc(TLParser.CallfuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#callfunc}.
	 * @param ctx the parse tree
	 */
	void exitCallfunc(TLParser.CallfuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#parametros}.
	 * @param ctx the parse tree
	 */
	void enterParametros(TLParser.ParametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#parametros}.
	 * @param ctx the parse tree
	 */
	void exitParametros(TLParser.ParametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#bucle}.
	 * @param ctx the parse tree
	 */
	void enterBucle(TLParser.BucleContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#bucle}.
	 * @param ctx the parse tree
	 */
	void exitBucle(TLParser.BucleContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#si_bloque}.
	 * @param ctx the parse tree
	 */
	void enterSi_bloque(TLParser.Si_bloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#si_bloque}.
	 * @param ctx the parse tree
	 */
	void exitSi_bloque(TLParser.Si_bloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#si}.
	 * @param ctx the parse tree
	 */
	void enterSi(TLParser.SiContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#si}.
	 * @param ctx the parse tree
	 */
	void exitSi(TLParser.SiContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#sino_si}.
	 * @param ctx the parse tree
	 */
	void enterSino_si(TLParser.Sino_siContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#sino_si}.
	 * @param ctx the parse tree
	 */
	void exitSino_si(TLParser.Sino_siContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#sino}.
	 * @param ctx the parse tree
	 */
	void enterSino(TLParser.SinoContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#sino}.
	 * @param ctx the parse tree
	 */
	void exitSino(TLParser.SinoContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#iter}.
	 * @param ctx the parse tree
	 */
	void enterIter(TLParser.IterContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#iter}.
	 * @param ctx the parse tree
	 */
	void exitIter(TLParser.IterContext ctx);
	/**
	 * Enter a parse tree produced by {@link TLParser#mientras}.
	 * @param ctx the parse tree
	 */
	void enterMientras(TLParser.MientrasContext ctx);
	/**
	 * Exit a parse tree produced by {@link TLParser#mientras}.
	 * @param ctx the parse tree
	 */
	void exitMientras(TLParser.MientrasContext ctx);
}