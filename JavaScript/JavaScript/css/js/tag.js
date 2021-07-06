
colors = {
    P: 'rgg(111, 122, 133)',
    padrao: '#616161',
    get (tagNAME){
        return this[tagNAME] ? this[tagNAME] : this.padrao
        // this referencia a cor que está dentro do objeto
    }
}

document.querySelectorAll('.TAG').forEach(element => {
    const tag = element.tagName

    element.style.borderBottom = "2px solid red"
    element.style.borderColor = colors.get(tag)

    const Label = document.createElement('tag_name')
    // cria um  novo nó com nome 'tag_name', esse novo nó vai ser inserido na posição 0
    // span dentro do parágrafo <p class="TAG"></p> é um nó.
    Label.innerHTML = tag
    element.insertBefore(Label, element.childNodes[0])
    // insertBefore é necessário para inserir o novo elemento 'Label'
    // sem isso ele não aparece na página, já que esse elemento não existe originalmente
    
    // childNodes dá os nós filhos a partir da class tag
    // ao usar insertBefore, será criado o nó Label na posição especificada 0
    // no elemento de classe tag
    console.log('childNodes',element.childNodes)

});