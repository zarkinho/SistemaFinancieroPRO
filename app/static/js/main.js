// ============================================================
// PROYECTO : Sistema Financiero PRO
// ARCHIVO  : main.js
// VERSIÓN  : 3.0
// ============================================================


// ============================================================
// RELOJ
// ============================================================

function actualizarReloj() {

    const fechaElemento = document.getElementById("fecha");

    if (!fechaElemento) return;

    const ahora = new Date();

    fechaElemento.innerHTML =
        "📅 " +
        ahora.toLocaleDateString("es-CO") +
        " | 🕒 " +
        ahora.toLocaleTimeString(
            "es-CO",
            {
                hour: "2-digit",
                minute: "2-digit",
                hour12: false
            }
        );

}

actualizarReloj();

setInterval(actualizarReloj, 1000);


// ============================================================
// CONFIRMAR ELIMINAR
// ============================================================

document.querySelectorAll(".btn-eliminar").forEach(function (boton) {

    boton.addEventListener("click", function (e) {

        if (!confirm("¿Desea eliminar este movimiento?")) {

            e.preventDefault();

        }

    });

});


// ============================================================
// BUSCADOR
// ============================================================

const buscador = document.getElementById("buscar");

if (buscador) {

    buscador.addEventListener("keyup", function () {

        const texto = this.value.toLowerCase();

        document.querySelectorAll("tbody tr").forEach(function (fila) {

            fila.style.display =

                fila.innerText
                    .toLowerCase()
                    .includes(texto)

                    ? ""

                    : "none";

        });

    });

}


// ============================================================
// CARGAR CATEGORÍAS AUTOMÁTICAMENTE
// ============================================================

document.addEventListener("DOMContentLoaded", function () {

    const tipo = document.getElementById("tipo");

    const categoria = document.getElementById("categoria");

    if (!tipo || !categoria) {

        return;

    }

    async function cargarCategorias() {

        const respuesta = await fetch(

            "/categorias/" + tipo.value

        );

        const datos = await respuesta.json();

        categoria.innerHTML = "";

        datos.forEach(function (item) {

            const opcion = document.createElement("option");

            opcion.value = item.id;

            opcion.textContent = item.nombre;

            categoria.appendChild(opcion);

        });

    }

    tipo.addEventListener(

        "change",

        cargarCategorias

    );

    cargarCategorias();

});


// ============================================================
// FIN
// ============================================================