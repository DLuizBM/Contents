// Em JS um módulo é um arquivo

// formas de exportar coisas de um módulo
this.ola = 'Fala pessoal'
exports.bemVindo = 'Até logo'
module.exports.atelogo = 'até a próxima'
// ola, bemVindo, atelogo -> atributos dinâmicos

// forma mais comum, ESSE TIPO DE EXPORTAR DEVE ESTAR EM UM ARQUIVO SEPERADO
// NÃO PODE ESTAR COM AS OUTRAS FORMAS DE EXPORTAR
/*
module.exports = {
    bomDia: 'Bom dia',
    boaNoite(){
        return 'Boa noite'
    }
}
*/
