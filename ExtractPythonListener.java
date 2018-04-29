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
	public void exitAssignment(TLParser.AssignmentContext ctx){
		TokenStream tokens = parser.getTokenStream();
		String expresion = tokens.getText(ctx.assign());
		System.out.println(expresion);

	}

	public void exitEscribir(TLParser.EscribirContext ctx){
		TokenStream tokens = parser.getTokenStream();
		String expresion = tokens.getText(ctx.sentence());
		System.out.println("print " + expresion);
	}

	public void exitLeer(TLParser.LeerContext ctx){
		System.out.println("input()");
	}

	public void enterBucle(TLParser.BucleContext ctx){
		TokenStream tokens = parser.getTokenStream();
		String iter = tokens.getText(ctx.iter());
		String module = tokens.getText(ctx.module());
		System.out.println("for "+ctx.ID()+" in "+iter+":");
	}	
	
	@Override
	public void exitMientras (TLParser.MientrasContext ctx){
		TokenStream tokens = parser.getTokenStream();
		
		String condicional = tokens.getText(ctx.expresion_condicional());
		System.out.println("while " + "(" + condicional + ")");
		
		String modulo = tokens.getText(ctx.module().block());
		char[] modulo_char = modulo.toCharArray();
		System.out.print("   ");
		for (char c : modulo_char){
			if (c == '\n')
				System.out.print("\n   ");
			else
				System.out.print( c );
		}
	}


	/*
	@Override
	public void enterPrograma(TLParser.ProgramaContext ctx){
		System.out.println("Comienzo");
	}
	
	@Override
	public void exitPrograma(TLParser.ProgramaContext ctx) {
		System.out.println("Fin");
	}*/

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