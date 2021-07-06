package Generics;

public class CaixaNumero<N extends Number> extends Caixa<N>{

    // Restringindo o tipo no generics
    // caixa foi resolvida para o tipo N
    // CaixaNumero foi resolvida para o mesmo tipo de Caixa, porém só herda um tipo Número
    
}
