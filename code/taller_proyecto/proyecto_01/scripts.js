function guardar() {
    var nombre = document.getElementById('nombre').value
    var apellido = document.getElementById('apellido').value

    var palabras = document.getElementById('palabras')
    palabras.innerHTML = '<h1>'+nombre+' '+apellido+'</h1>'
}