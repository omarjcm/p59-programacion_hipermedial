function ingresarElemento() {
    var textoPagina = document.getElementById('texto')

    var container = document.getElementById('container')
    container.innerHTML = '<h1>' + textoPagina.value + '</h1>'
}