function ingresarElemento() {
    var textoPagina = document.getElementById('texto')

    var container = document.getElementById('container')
    container.outerHTML = '<div id="container"><h1>' + textoPagina.value + '</h1></div>'
}