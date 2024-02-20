<?php
// Configuración de la conexión a la base de datos
$host = 'localhost';
$dbname = 'sm52_arduino';
$username = 'root';
$password = 'root';

try {
    // Conexión a la base de datos
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);

    // Verificar si se ha enviado un estado nuevo del LED
    if (isset($_POST['status'])) {
        // Obtener el nuevo estado del LED
        $newStatus = intval($_POST['status']);

        // Actualizar el estado del LED en la base de datos
        $stmt = $pdo->prepare("UPDATE estado_led SET led_status = :status WHERE id_estado_led = 1");
        $stmt->bindParam(':status', $newStatus, PDO::PARAM_INT);
        $stmt->execute();

        echo "Estado del LED actualizado correctamente a: $newStatus";
    } else {
        // Obtener el estado actual del LED desde la base de datos
        $stmt = $pdo->query("SELECT led_status FROM estado_led WHERE id_estado_led = 1");
        $row = $stmt->fetch(PDO::FETCH_ASSOC);
        $currentStatus = $row['led_status'];
        echo $currentStatus;
    }
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
