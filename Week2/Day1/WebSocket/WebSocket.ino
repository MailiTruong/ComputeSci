#include <WiFi.h>  
#include <WebSocketsServer.h>

#define BUTTON_PIN 23

const char* ssid = "SFR_8450"; // Replace with your network SSID  
const char* password = "uhq55dykr8fni27ucvb4"; // Replace with your network password  
bool lastButtonState = HIGH;

WebSocketsServer webSocket = WebSocketsServer(80); // Port 81  

void webSocketEvent(uint8_t num, WStype_t type, uint8_t* payload, size_t length) {
  switch(type) {
    case WStype_DISCONNECTED:
      Serial.printf("Client disconnected: %u\n", num);
      break;
    case WStype_CONNECTED:
      Serial.printf("Client connected: %u\n", num);
      break;
    case WStype_TEXT:
      Serial.printf("Message from client: %s\n", payload);
      break;
  }
}

void setup() {
  Serial.begin(115200);  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {  
    delay(1000);  
    Serial.println("Connecting to WiFi...");  
  }  
  Serial.println("Connected to WiFi");  
  Serial.print("IP address: ");  
  Serial.println(WiFi.localIP());  
  webSocket.begin();  
  webSocket.onEvent(webSocketEvent);  

  pinMode(BUTTON_PIN, INPUT_PULLUP);
}  

void loop() {  
  webSocket.loop(); 
  bool buttonState = digitalRead(BUTTON_PIN);
  if (lastButtonState == HIGH && buttonState == LOW)
  {
    Serial.println("the button is pressed"); 
    webSocket.broadcastTXT("Button pressed");
    delay(200);
  }
  buttonState = lastButtonState; 
}  
