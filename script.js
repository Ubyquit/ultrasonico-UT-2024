$(document).ready(function () {
    var ctx = document.getElementById("sensorUltrasonico").getContext("2d");
    var chart = new Chart(ctx, {
        type: "bar", // Tipo de gráfica
        data: {
            labels: [], // Las etiquetas de tiempo
            datasets: [
                {
                    label: "Sensor Data",
                    backgroundColor: "rgb(51, 141, 255)",
                    borderColor: "rgb(93, 164, 255)",
                    data: [], // Los datos del sensor
                },
            ],
        },
        options: {},
    });

    // Función para actualizar la gráfica
    function fetchData() {
        $.ajax({
            url: "conexion.php",
            type: "GET",
            success: function (data) {
                var parsedData = JSON.parse(data);
                var labels = [];
                var sensorData = [];

                parsedData.forEach(function (row) {
                    labels.push(row.led_color);
                    sensorData.push(row.mensaje);
                });

                chart.data.labels = labels;
                chart.data.datasets[0].data = sensorData;
                chart.update();

                // Cambiar el LED basado en el color recibido
                var led1 = document.getElementById("led1");
                var led2 = document.getElementById("led2");
                var led3 = document.getElementById("led3");

                // Recuperar el color del último registro
                var lastColor = parsedData[0].led_color;

                // Cambiar el estado de los LEDs según el color recibido
                if (lastColor === "rojo") {
                    led1.src = "img/VERDE-OFF.svg";
                    led2.src = "img/AMARILLO-OFF.svg";
                    led3.src = "img/ROJO-ON.svg";
                } else if (lastColor === "amarillo") {
                    led1.src = "img/VERDE-OFF.svg";
                    led2.src = "img/AMARILLO-ON.svg";
                    led3.src = "img/ROJO-OFF.svg";
                } else if (lastColor === "verde") {
                    led1.src = "img/VERDE-ON.svg";
                    led2.src = "img/AMARILLO-OFF.svg";
                    led3.src = "img/ROJO-OFF.svg";
                }
            },
        });
    }

    // Actualizar la gráfica cada cierto tiempo, por ejemplo, cada 5 segundos
    setInterval(function () {
        fetchData(); // Actualizar la gráfica de datos
    }, 500); // Ajustar el intervalo según sea necesario
});
