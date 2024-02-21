$(document).ready(function() {
    // Hacer una solicitud AJAX para obtener el estado actual del LED
    $.ajax({
        type: "POST",
        url: "toggle_led.php",
        success: function(response) {
            var isChecked = (response === "1");
            $("#toggleBtn").prop("checked", isChecked);
            // Cambiar la imagen según el estado del LED
            if(isChecked) {
                $("#led1").attr("src", "img/VERDE-ON.svg");
            } else {
                $("#led1").attr("src", "img/VERDE-OFF.svg");
            }
        },
        error: function(xhr, status, error) {
            console.error("Error al obtener el estado del LED:", error);
        }
    });

    // Manejar el evento de cambio del botón de alternancia
    $("#toggleBtn").on("change", function() {
        var isChecked = $(this).is(":checked");
        $.ajax({
            type: "POST",
            url: "toggle_led.php",
            data: { status: isChecked ? 1 : 0 },
            success: function(response) {
                console.log(response);
                // Cambiar la imagen según el estado del LED
                if(isChecked) {
                    $("#led1").attr("src", "img/VERDE-ON.svg");
                } else {
                    $("#led1").attr("src", "img/VERDE-OFF.svg");
                }
            },
            error: function(xhr, status, error) {
                console.error("Error al cambiar el estado del LED:", error);
            }
        });
    });
});
