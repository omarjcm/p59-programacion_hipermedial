function agregarElemento() {
    var h1 = document.createElement('h1')
    var texto = document.createTextNode('DOM - Document Object Model')
    h1.appendChild( texto )

    var container = document.getElementById('container')
    container.appendChild( h1 )
}