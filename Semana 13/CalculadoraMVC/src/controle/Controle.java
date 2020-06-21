package controle;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import dao.Dao;
import modelo.Calculadora;
import visao.JanelaCalculadora;

public class Controle implements ActionListener {
	
	private JanelaCalculadora janela;
	private Calculadora calculadora;
	private Dao dao;
	
	

	public Controle(JanelaCalculadora janela, Calculadora calculadora) {
		super();
		this.janela = janela;
		this.calculadora = calculadora;
		this.janela.getBtnLimpar().addActionListener(this);
		this.janela.getBtnSoma().addActionListener(this);
		dao = new Dao();
		
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getActionCommand().equals("Somar")){
			calculadora.setNum1(Integer.parseInt(janela.getTextFieldNum1().getText()));
			calculadora.setNum2(Integer.parseInt(janela.getTextFieldNum2().getText()));
			calculadora.somar();
			janela.getTextField().setText(String.valueOf(calculadora.getResultado()));
			
			System.out.println(calculadora.toString());
			
			try {
				dao.gravarArquivo(calculadora);
			} catch (Exception e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		}
		if(e.getActionCommand().equals("Limpar")){
			janela.getTextField().setText("");
			janela.getTextFieldNum1().setText("");
			janela.getTextFieldNum2().setText("");
		}
		
		
	}
	
	
	

}
