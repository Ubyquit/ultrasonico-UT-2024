# Escenario 1: Uso Directo de WebSockets para Controlar el LED

En este escenario, la base de datos se utiliza principalmente para registrar el estado inicial del LED o para mantener un registro histórico de los cambios de estado. Cuando un usuario cambia el estado del LED a través de la interfaz web:

Cambio de Estado: La interfaz web envía un mensaje a través de WebSockets al servidor para cambiar el estado del LED.

Actualizar el Arduino: El servidor recibe el mensaje y envía el comando correspondiente al Arduino para cambiar el estado del LED.

Actualizar la Base de Datos: Opcionalmente, después de cambiar el estado del LED, el servidor puede actualizar la base de datos con el nuevo estado para mantener un registro histórico.

En este escenario, la base de datos no se consulta constantemente para verificar el estado del LED. En su lugar, actúa como un registro que se actualiza solo cuando se realiza un cambio de estado.

```css
[ Usuario ] --(1) Cambia estado del switch--> [ Página Web ]
                                                 |
                                                 | (2) Envía mensaje ("1" o "0")
                                                 V
                                          [ Servidor WebSocket ]
                                                 |
                                                 | (3) Escribe comando en el puerto serial
                                                 V
                                            [ Arduino (LED) ]
                                                 |
                                                 | (4) Cambia estado (Encendido/Apagado)
                                                 V
                                       [ Feedback Visual en Página Web ]

```