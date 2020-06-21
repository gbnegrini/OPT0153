package primeiroTDD;

import static org.junit.jupiter.api.Assertions.*;
import primeiroTDD.ManipulaDna;

import org.junit.jupiter.api.Test;

class ManipulaDnaTeste {
	@Test
	public void deveriaConverterDNAemRNA() throws Exception{
		String dna = "ATCGAT";
		String rna = "";
	
		ManipulaDna manipulador = new ManipulaDna();
		rna = manipulador.converterDNAemRNA(dna);
		assertEquals("AUCGAU", rna);
	}
	
	@Test
	public void deveriaGerarFitaComplementar() throws Exception{
		String dna = "ATCAATGCA";
		String dnaComplementar = "";
		
		ManipulaDna manipulador = new ManipulaDna();
		dnaComplementar = manipulador.gerarFitaComplementar(dna);
		assertEquals("TAGTTACGT", dnaComplementar);
	}
	

}
