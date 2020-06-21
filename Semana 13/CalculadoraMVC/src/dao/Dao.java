package dao;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import modelo.Calculadora;

public class Dao {
	
	public Dao(){}
	
	public void gravarArquivo(Calculadora calculadora){
		
		File arq = new File("testeCalculadora.txt");
		FileOutputStream fout = null;
		String resultado = String.valueOf(calculadora.getResultado());
		System.out.println(resultado);
		
		for(int i = 0; i < resultado.length(); i++){
			try {
				fout.write(resultado.charAt(i));
				fout.flush();
			} catch (IOException e) {
				e.printStackTrace();
			}
			
		}
		System.out.println("Grava��o conclu�da com sucesso!");
		try {
			fout.close();
		} catch (IOException e) {
			e.printStackTrace();
		}		
		
	}

}
