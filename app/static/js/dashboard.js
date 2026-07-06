// ============================================================
// PROYECTO : Sistema Financiero PRO
// ARCHIVO  : dashboard.js
// VERSIÓN  : 1.0
// ============================================================

// ============================================================
// RELOJ
// ============================================================

function actualizarReloj() {

    const ahora = new Date();

    const fecha = ahora.toLocaleDateString(
        "es-CO"
    );

    const hora = ahora.toLocaleTimeString(
        "es-CO",
        {
            hour: "2-digit",
            minute: "2-digit",
            hour12: false
        }
    );

    const reloj = document.getElementById("fecha");

    if (reloj) {

        reloj.innerHTML =
            "📅 " +
            fecha +
            " &nbsp; | &nbsp; 🕒 " +
            hora;

    }

}

actualizarReloj();

setInterval(

    actualizarReloj,

    1000

);

// ============================================================
// CHART.JS
// ============================================================

const canvas = document.getElementById("graficoFinanzas");

if (canvas && typeof datosGrafico !== "undefined") {

    new Chart(canvas, {

        type: "bar",

        data: {

            labels: [

                "Ingresos",

                "Gastos",

                "Inversiones"

            ],

            datasets: [

                {

                    label: "Valores",

                    data: datosGrafico,

                    borderWidth: 2,

                    borderRadius: 10

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

}