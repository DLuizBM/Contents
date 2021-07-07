
var websocket = new WebSocket("ws://localhost:8080/setores/painel");
websocket.onopen = function(event) {
    websocket.send("Olá mundo");
}

