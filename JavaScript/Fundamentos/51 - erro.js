function tratarerro(erro){
    //throw 'Contate o suporte'
    //throw 10
    throw{ // throw faz o lançamento do erro
        tipo: erro.tipo
    }

}

function grito(obj){
    try{
        console.log(obj.nome.toUpperCase() + '!!!')
    }catch(e){
        tratarerro(e)
    }finally{
        console.log('FINAL!!')
    }
}

const obj = {noe: 'Ayrton'}
grito(obj)