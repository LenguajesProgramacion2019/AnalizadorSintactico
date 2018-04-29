import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.misc.Interval;

public class ExtractPythonListener extends TLBaseListener {
	TLParser parser;
	
	public ExtractPythonListener(TLParser parser) {this.parser = parser;}
	
	/** Listen to matches of classDeclaration */
	
	//public void enterExpresion_aditiva(TLParser.Expresion_aditivaContext ctx){
	//	System.out.println(ctx.expresion_multiplicativa());
	//}
	
	@Override
	public void exitFuncion(TLParser.FuncionContext ctx){
		TokenStream tokens = parser.getTokenStream();
		
		String nombre = tokens.getText(ctx.name());
		String argumentos = tokens.getText(ctx.arg_declaracion());
		System.out.println("def " + nombre + "( " + argumentos + " ):" );
		
		String bloque = "";
		if (ctx.block() != null){
			bloque = tokens.getText(ctx.block());
			System.out.println("   " + bloque);
		}
		
		String retorno = "";
		if (ctx.retorno().sentence() != null){
			retorno = tokens.getText(ctx.retorno().sentence());
			System.out.println("   return " + retorno);
		}		
	}
	
	@Override
	public void exitExpresion_aditiva(TLParser.Expresion_aditivaContext ctx){
		TokenStream tokens = parser.getTokenStream();
		String expresion = tokens.getText(ctx.expresion_multiplicativa());
		//System.out.println(expresion);
	}

	
	@Override
	public void enterPrograma(TLParser.ProgramaContext ctx){
		System.out.println("Comienzo");
	}
	
	@Override
	public void exitPrograma(TLParser.ProgramaContext ctx) {
		System.out.println("Fin");
	}

	/** Listen to matches of methodDeclaration */
	/*@Override
	public void enterMethodDeclaration(JavaParser.MethodDeclarationContext ctx) {
	// need parser to get tokens
		TokenStream tokens = parser.getTokenStream();
		String type = "void";	
		if ( ctx.type()!=null ) {
			type = tokens.getText(ctx.type());
		}
		String args = tokens.getText(ctx.formalParameters());
		System.out.println("\t"+type+" "+ctx.Identifier()+args+";");
	}*/
}