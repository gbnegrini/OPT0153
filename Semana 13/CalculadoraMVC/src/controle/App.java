package controle;

import modelo.Calculadora;
import visao.JanelaCalculadora;

public class App {

	public static void main(String[] args) {
		
		JanelaCalculadora janela = new JanelaCalculadora();
		janela.setVisible(true);
		Calculadora calculadora = new Calculadora();
		
		Controle controle = new Controle(janela, calculadora);

	}

}
