document.addEventListener("DOMContentLoaded", () => {
  const websocket = new WebSocket("ws://localhost:8765");
  
  websocket.onopen = () => console.log("Conectado al servidor WebSocket");
  
  // Manejar mensajes recibidos del servidor
  websocket.onmessage = (event) => {
    const message = event.data;
    console.log("Mensaje recibido:", message);
    
    // Actualiza la interfaz de usuario según el estado del LED
    const toggleBtn = document.getElementById("toggleBtn");

    if(message === "1") {
      toggleBtn.checked = true;
    } else if(message === "0") {
      toggleBtn.checked = false;
    }
  };

  document.getElementById("toggleBtn").addEventListener("change", function () {
    const command = this.checked ? "1" : "0";
    websocket.send(command);
    console.log("Enviado:", command);
  });
});
