// O objeto global é um objeto JS que possui várias funções e métodos
// é possível adionar funções e métodos no objeto global
// Mas essa prática não é recomendável
// para fazer adição de funções e métodos, deves-se criar módulos

global.Minhaapp = {
    saudacao(){
        return 'Olá programador'
    },
    nome: 'Sistema legal!!'
}