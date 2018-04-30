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
	public void enterModule (TLParser.ModuleContext ctx){
		TokenStream tokens = parser.getTokenStream();

		String expresion;
		String name;
		char[] expresion_char;
		if(ctx.block() != null){
			if(ctx.block().assignment() != null){
				expresion = tokens.getText(ctx.block().assignment());
				System.out.println(expresion);
			}
			else if(ctx.block().escribir() != null){
				expresion = tokens.getText(ctx.block().escribir().sentence());
				System.out.println("print " + expresion);
			}
			else if(ctx.block().leer() != null){
				System.out.println("input()");
			}
			
			else if(ctx.block().sentence() != null){
				if(ctx.block().sentence().call_array() != null){
					name = tokens.getText(ctx.block().sentence().call_array().name());
					expresion = tokens.getText(ctx.block().sentence().call_array().call_array_it());
					System.out.print(name);
					expresion_char = expresion.toCharArray();
					System.out.print("[");
					for (char c : expresion_char){
						if (c == ',')
							System.out.print("][");
						else
							System.out.print( c );
					}
					System.out.println("]");
				}
				else if(ctx.block().sentence().call_dir() != null){
					name = tokens.getText(ctx.block().sentence().call_dir().name());
					expresion = tokens.getText(ctx.block().sentence().call_dir().call_dir_it());
					System.out.print(name);
					expresion_char = expresion.toCharArray();
					System.out.print("['");
					for (char c : expresion_char){
						if (c == '.')
							System.out.print("']['");
						else
							System.out.print( c );
					}
					System.out.println("']");
				}
				else if(ctx.block().sentence().dicc() != null){
					expresion = tokens.getText(ctx.block().sentence().dicc().diccele());
					expresion_char = expresion.toCharArray();
					System.out.print("{'");
					for (char c : expresion_char){
						if (c == ':')
							System.out.print("':");
						else if (c == ',')
							System.out.print(", '");
						else
							System.out.print( c );
					}
					System.out.println("'}");
				}
				else{
					expresion = tokens.getText(ctx.block().sentence());
					System.out.println(expresion);
				}
			}
		}
	}
	
	@Override
	public void enterSi_bloque (TLParser.Si_bloqueContext ctx){
		TokenStream tokens = parser.getTokenStream();
		
		String condicional = tokens.getText(ctx.si().expresion_condicional());
		System.out.println("if " + condicional + ":");
		String modulo;
		if(ctx.si().module_si() != null){
			printModuleSi(ctx.si().module_si());
			//modulo = tokens.getText(ctx.si().module_si());
			//System.out.println("   " + modulo);
		}
		
		if (ctx.sino_si().expresion_condicional() != null){
			condicional = tokens.getText(ctx.sino_si().expresion_condicional());
			System.out.println("elif " + condicional + ":");
			
			if(ctx.sino_si().module_si().block() != null || ctx.sino_si().module_si().importar() != null){
				printModuleSi(ctx.sino_si().module_si());
				//modulo = tokens.getText(ctx.sino_si().module_si());
				//System.out.println("   " + modulo);
			}
		}
		
		if (ctx.sino().module_si() != null){
			System.out.println("else:");
			if(ctx.sino().module_si().block() != null || ctx.sino().module_si().importar() != null){
				printModuleSi(ctx.sino().module_si());
				//modulo = tokens.getText(ctx.sino().module_si());
				//System.out.println("   " + modulo);
			}
		}
	}

	public void printModuleSi (TLParser.Module_siContext ctx){
		TokenStream tokens = parser.getTokenStream();

		String expresion;
		String name;
		char[] expresion_char;
		if(ctx.block() != null){
			if(ctx.block().assignment() != null){
				expresion = tokens.getText(ctx.block().assignment());
				System.out.println("   " + expresion);
			}
			else if(ctx.block().escribir() != null){
				expresion = tokens.getText(ctx.block().escribir().sentence());
				System.out.println("   " + "print " + expresion);
			}
			else if(ctx.block().leer() != null){
				System.out.println("   " + "input()");
			}
			
			else if(ctx.block().sentence() != null){
				if(ctx.block().sentence().call_array() != null){
					name = tokens.getText(ctx.block().sentence().call_array().name());
					expresion = tokens.getText(ctx.block().sentence().call_array().call_array_it());
					System.out.print("   " + name);
					expresion_char = expresion.toCharArray();
					System.out.print("[");
					for (char c : expresion_char){
						if (c == ',')
							System.out.print("][");
						else
							System.out.print( c );
					}
					System.out.println("]");
				}
				else if(ctx.block().sentence().call_dir() != null){
					name = tokens.getText(ctx.block().sentence().call_dir().name());
					expresion = tokens.getText(ctx.block().sentence().call_dir().call_dir_it());
					System.out.print("   " + name);
					expresion_char = expresion.toCharArray();
					System.out.print("['");
					for (char c : expresion_char){
						if (c == '.')
							System.out.print("']['");
						else
							System.out.print( c );
					}
					System.out.println("']");
				}
				else if(ctx.block().sentence().dicc() != null){
					expresion = tokens.getText(ctx.block().sentence().dicc().diccele());
					expresion_char = expresion.toCharArray();
					System.out.print("   " + "{'");
					for (char c : expresion_char){
						if (c == ':')
							System.out.print("':");
						else if (c == ',')
							System.out.print(", '");
						else
							System.out.print( c );
					}
				}
				else{
					expresion = tokens.getText(ctx.block().sentence());
					System.out.println(expresion);
				}
			}
		}

	}
	
	@Override
	public void enterImportar(TLParser.ImportarContext ctx){
		TokenStream tokens = parser.getTokenStream();
		if(ctx.id_import() != null){
			String id_import = tokens.getText(ctx.id_import());
			System.out.println("import "+ id_import);
		}
		else {
			System.out.println("from "+ctx.ID().get(0)+" import "+ctx.ID().get(1));
		} 
	}


	public void enterBucle(TLParser.BucleContext ctx){
		TokenStream tokens = parser.getTokenStream();
		
		String iter = tokens.getText(ctx.iter());
		System.out.println("for "+ctx.ID()+" in "+iter+":");

		printModuleFor(ctx.module_for());
		
		/*String modulo = tokens.getText(ctx.module_for());
		char[] modulo_char = modulo.toCharArray();
		System.out.print("   ");
		for (char c : modulo_char){
			if (c == '\n')
				System.out.print("\n   ");
			else
				System.out.print( c );
		}*/
	}	

	public void printModuleFor (TLParser.Module_forContext ctx){
		TokenStream tokens = parser.getTokenStream();

		String expresion;
		String name;
		char[] expresion_char;
		if(ctx.block() != null){
			if(ctx.block().assignment() != null){
				expresion = tokens.getText(ctx.block().assignment());
				System.out.println("   " + expresion);
			}
			else if(ctx.block().escribir() != null){
				expresion = tokens.getText(ctx.block().escribir().sentence());
				System.out.println("   " + "print " + expresion);
			}
			else if(ctx.block().leer() != null){
				System.out.println("   " + "input()");
			}
			
			else if(ctx.block().sentence() != null){
				if(ctx.block().sentence().call_array() != null){
					name = tokens.getText(ctx.block().sentence().call_array().name());
					expresion = tokens.getText(ctx.block().sentence().call_array().call_array_it());
					System.out.print("   " + name);
					expresion_char = expresion.toCharArray();
					System.out.print("[");
					for (char c : expresion_char){
						if (c == ',')
							System.out.print("][");
						else
							System.out.print( c );
					}
					System.out.println("]");
				}
				else if(ctx.block().sentence().call_dir() != null){
					name = tokens.getText(ctx.block().sentence().call_dir().name());
					expresion = tokens.getText(ctx.block().sentence().call_dir().call_dir_it());
					System.out.print("   " + name);
					expresion_char = expresion.toCharArray();
					System.out.print("['");
					for (char c : expresion_char){
						if (c == '.')
							System.out.print("']['");
						else
							System.out.print( c );
					}
					System.out.println("']");
				}
				else if(ctx.block().sentence().dicc() != null){
					expresion = tokens.getText(ctx.block().sentence().dicc().diccele());
					expresion_char = expresion.toCharArray();
					System.out.print("   " + "{'");
					for (char c : expresion_char){
						if (c == ':')
							System.out.print("':");
						else if (c == ',')
							System.out.print(", '");
						else
							System.out.print( c );
					}
				}
				else{
					expresion = tokens.getText(ctx.block().sentence());
					System.out.println(expresion);
				}
			}
		}

	}
	
	@Override
	public void exitMientras (TLParser.MientrasContext ctx){
		TokenStream tokens = parser.getTokenStream();
		
		String condicional = tokens.getText(ctx.expresion_condicional());
		System.out.println("while " + "(" + condicional + "):");

		printModuleWhile(ctx.module_while());
		//String modulo = tokens.getText(ctx.module_while());
		//char[] modulo_char = modulo.toCharArray();

	}

	public void printModuleWhile (TLParser.Module_whileContext ctx){
		TokenStream tokens = parser.getTokenStream();

		String expresion;
		String name;
		char[] expresion_char;
		if(ctx.block() != null){
			if(ctx.block().assignment() != null){
				expresion = tokens.getText(ctx.block().assignment());
				System.out.println("   " + expresion);
			}
			else if(ctx.block().escribir() != null){
				expresion = tokens.getText(ctx.block().escribir().sentence());
				System.out.println("   " + "print " + expresion);
			}
			else if(ctx.block().leer() != null){
				System.out.println("   " + "input()");
			}
			
			else if(ctx.block().sentence() != null){
				if(ctx.block().sentence().call_array() != null){
					name = tokens.getText(ctx.block().sentence().call_array().name());
					expresion = tokens.getText(ctx.block().sentence().call_array().call_array_it());
					System.out.print("   " + name);
					expresion_char = expresion.toCharArray();
					System.out.print("[");
					for (char c : expresion_char){
						if (c == ',')
							System.out.print("][");
						else
							System.out.print( c );
					}
					System.out.println("]");
				}
				else if(ctx.block().sentence().call_dir() != null){
					name = tokens.getText(ctx.block().sentence().call_dir().name());
					expresion = tokens.getText(ctx.block().sentence().call_dir().call_dir_it());
					System.out.print("   " + name);
					expresion_char = expresion.toCharArray();
					System.out.print("['");
					for (char c : expresion_char){
						if (c == '.')
							System.out.print("']['");
						else
							System.out.print( c );
					}
					System.out.println("']");
				}
				else if(ctx.block().sentence().dicc() != null){
					expresion = tokens.getText(ctx.block().sentence().dicc().diccele());
					expresion_char = expresion.toCharArray();
					System.out.print("   " + "{'");
					for (char c : expresion_char){
						if (c == ':')
							System.out.print("':");
						else if (c == ',')
							System.out.print(", '");
						else
							System.out.print( c );
					}
				}
				else{
					expresion = tokens.getText(ctx.block().sentence());
					System.out.println(expresion);
				}
			}
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