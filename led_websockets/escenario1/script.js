document.addEventListener("DOMContentLoaded", () => {
  const websocket = new WebSocket("ws://localhost:8765");
  websocket.onopen = () => console.log("Conectado al servidor WebSocket");

  // Manejar el estado inicial del LED enviado por el servidor
  websocket.onmessage = (event) => {
    const ledState = event.data;
    console.log("Estado inicial del LED recibido:", ledState);
    const toggleBtn = document.getElementById("toggleBtn");
    if (ledState === "1") {
      toggleBtn.checked = true;
    } else {
      toggleBtn.checked = false;
    }
  };

  document.getElementById("toggleBtn").addEventListener("change", function () {
    const command = this.checked ? "1" : "0";
    websocket.send(command);
    console.log("Comando enviado al servidor:", command);
  });
});
