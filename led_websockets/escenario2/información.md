# Escenario 2: Mantener la Base de Datos Como Fuente de Verdad

Si prefieres mantener la base de datos como la fuente principal de verdad para el estado del LED, puedes seguir utilizando WebSockets para notificar al servidor y al cliente sobre los cambios, pero manteniendo la lógica de consulta y actualización de la base de datos:

Cambio de Estado a Través de la Web: La interfaz web envía una solicitud para cambiar el estado del LED.

Actualizar la Base de Datos: El servidor actualiza la base de datos con el nuevo estado del LED.

Notificar al Arduino: Tras actualizar la base de datos, el servidor envía el comando al Arduino para cambiar el estado del LED.

Notificación de Cambio de Estado: El servidor notifica a la interfaz web (a través de WebSockets) que el cambio ha sido realizado con éxito.

```css
[ Usuario ] --(1) Cambia estado del switch--> [ Página Web ]
                                                 |
                                                 | (2) Envía mensaje ("1" o "0")
                                                 V
                                          [ Servidor WebSocket ]
                                                 |
                                                 |<-(3) Consulta/Actualiza DB
                                                 |
                                                 | (4) Escribe comando en el puerto serial
                                                 V
                                            [ Arduino (LED) ]
                                                 |
                                                 | (5) Cambia estado (Encendido/Apagado)
                                                 |
                            [ Feedback Visual en Página Web ]<-
                                                 |
                                                 | (6) Envia estado actual al cliente
                                                 V
                                          [ Servidor WebSocket ]
                                                 |
                                                 | (7) Mensaje con estado ("1" o "0")
                                                 V
                                       [ Página Web (Cliente) ]


```