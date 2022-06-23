const formulario = document.getElementById('formulario');

function comprobarClave() {
    c1 = document.f1.clave1.value
    c2 = document.f1.clave2.value

    if (c1 !== c2) {
        alert("las contraseñas no son iguales")
        document.f1.clave1.value = "";
        document.f1.clave2.value = "";
        document.f1.clave1.value.focus();
    }
}