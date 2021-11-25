function agregarElemento() {
    var textoPagina = document.getElementById('texto')

    var h1 = document.createElement('h1')
    var texto = document.createTextNode( textoPagina.value )
    h1.appendChild( texto )

    var container = document.getElementById('container')
    container.appendChild( h1 )
}

function eliminarElemento() {
    var container = document.getElementById('container')
    container.removeChild( container.lastElementChild )
}