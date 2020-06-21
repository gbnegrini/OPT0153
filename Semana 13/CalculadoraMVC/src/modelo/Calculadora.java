package modelo;

public class Calculadora {
	
	private int num1;
	private int num2;
	private int resultado;
	
	public void somar(){
		this.resultado = this.num1+this.num2;
	}
	
	public Calculadora() {
		super();
	}
	public int getNum1() {
		return num1;
	}
	public void setNum1(int num1) {
		this.num1 = num1;
	}
	public int getNum2() {
		return num2;
	}
	public void setNum2(int num2) {
		this.num2 = num2;
	}

	public int getResultado() {
		return resultado;
	}

	public void setResultado(int resultado) {
		this.resultado = resultado;
	}

	@Override
	public String toString() {
		return "Calculadora [num1=" + num1 + ", num2=" + num2 + ", resultado=" + resultado + "]";
	}
	
	
	

}
