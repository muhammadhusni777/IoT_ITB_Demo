#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>


// Replace the next variables with your SSID/Password combination
const char* ssid = "Wifihusni12";
const char* password = "12345678";
const char* mqtt_server = "192.168.126.142";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;


// LED Pin
const int led1_pin = 15;
const int led2_pin = 2;
const int led3_pin = 4;
const int led4_pin = 5;



void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  pinMode(led1_pin, OUTPUT);
  pinMode(led2_pin, OUTPUT);
  pinMode(led3_pin, OUTPUT);
  pinMode(led4_pin, OUTPUT);


  

}

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* message, unsigned int length) {
  //Serial.print("Message arrived on topic: ");
  //Serial.print(topic);
  //Serial.print(". Message: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    //Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  //Serial.println();

  
  if (String(topic) == "led1") {
    //Serial.print("Changing output to ");
    if(messageTemp == "ON"){
      //Serial.println("ON");
      digitalWrite(led1_pin, HIGH);
    }
    else if(messageTemp == "OFF"){
      //Serial.println("OFF");
      digitalWrite(led1_pin, LOW);
    }
  }

  if (String(topic) == "led2") {
    //Serial.print("Changing output to ");
    if(messageTemp == "ON"){
      //Serial.println("ON");
      digitalWrite(led2_pin, HIGH);
    }
    else if(messageTemp == "OFF"){
      //Serial.println("OFF");
      digitalWrite(led2_pin, LOW);
    }
  }

  if (String(topic) == "led3") {
    //Serial.print("Changing output to ");
    if(messageTemp == "ON"){
      //Serial.println("ON");
      digitalWrite(led3_pin, HIGH);
    }
    else if(messageTemp == "OFF"){
      //Serial.println("OFF");
      digitalWrite(led3_pin, LOW);
    }
  }

  
  if (String(topic) == "IoTDevice2024/lamp") {
    //Serial.print("Changing output to ");
    if(messageTemp == "ON"){
      //Serial.println("ON");
      digitalWrite(led4_pin, HIGH);
    }
    else if(messageTemp == "OFF"){
      //Serial.println("OFF");
      digitalWrite(led4_pin, LOW);
    }
  }
  



 


}



void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP32Client_IOT22938924782")) {
      Serial.println("connected");

      client.subscribe("led1");
      client.subscribe("led2");
      client.subscribe("led3");
      client.subscribe("IoTDevice2024/lamp");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}


void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();


  long now = millis();
  if (now - lastMsg > 1000) {
    lastMsg = now;


  }
}
