// IIFE -> Immediately Invoked Function Expression
// Função imediatamente invocada
// Ideal para ser usada quando se deseja fugir do escopo global (quando se está usando o browser, por exemplo)
// lembrando que window é o escopo global no browser
// Tudo criado dentro desta função será executada apenas no escopo dessa função

(function () {
    console.log('Será executada na hora')
    console.log('Foge do escopo global')
    
})()