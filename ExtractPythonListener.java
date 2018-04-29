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