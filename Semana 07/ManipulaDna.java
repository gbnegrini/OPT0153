package primeiroTDD;

public class ManipulaDna {

	public ManipulaDna() {
		// TODO Auto-generated constructor stub
	}
	
	public String converterDNAemRNA(String dna) {
		return dna.replace("T", "U");
	}
	
	public String gerarFitaComplementar(String dna) {
		dna = dna.replace("A", "t");
		dna = dna.replace("T", "a");
		dna = dna.replace("C", "g");
		dna = dna.replace("G", "c");
		return dna.toUpperCase();
	}
}
