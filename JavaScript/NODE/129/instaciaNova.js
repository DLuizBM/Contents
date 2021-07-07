// Node por padrão retorna cache
// para retornar uma nova instância deve retornar uma função factory
// uma factory retorna uma nova instância (novo objeto)

module.exports = () => {
    return {
        valor: 1,
        inc(){
            this.valor++
        }
    }
}