#include <Adafruit_GFX.h>
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "HTTPSRedirect.h"
#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>
 
PN532_I2C pn532_i2c(Wire);
int ledpin1 = D1;
int ledpin2 = D2;
NfcAdapter nfc = NfcAdapter(pn532_i2c);
String tagId1 = "75 4A 85 2A";
String tagId2 = "5A 6F DC 73";
String tagId = "None";
byte nuidPICC[4];
 
// Enter network credentials:
const char* ssid = "Surya";
const char* password = "surya001";
 
// Enter Google Script Deployment ID:
const char* GScriptId = "AKfycbz866S47_Uj3B-in3b4r3YG5Rq_dmW0wXwGvE-4qLx4ugw0Mh2vgG3qsluP3jcf24oy";

// Enter command (insert_row or append_row) and your Google Sheets sheet name (default is Sheet1):
String payload_base = "{\"command\": \"insert_row\", \"sheet_name\": \"Sheet1\", \"values\": ";
String payload = "";
 

const char* host = "script.google.com";
const int httpsPort = 443;
const char* fingerprint = "";
String url = String("/macros/s/") + GScriptId + "/exec";
HTTPSRedirect* client = nullptr;
 

String user = "";
String id = "";
String enter = "";
 
void setup() {
  Serial.begin(115200);
  Serial.println("Starting...");
  Serial.println('\n');
  pinMode(ledpin1, OUTPUT);
  pinMode(ledpin2, OUTPUT);
  Serial.println("System initialized");
 
  nfc.begin();
  digitalWrite(ledpin1, LOW);
  digitalWrite(ledpin2, LOW);
  
  // Connect to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to ");
  Serial.print(ssid);
  Serial.println(" ...");
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println('\n');
  Serial.println("Connection established!");
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());
 
  // Use HTTPSRedirect class to create a new TLS connection
  client = new HTTPSRedirect(httpsPort);
  client->setInsecure();
  client->setPrintResponseBody(true);
  client->setContentTypeHeader("application/json");
  
  Serial.print("Connecting to ");
  Serial.println(host);
 
  // Try to connect for a maximum of 5 times
  bool flag = false;
  for (int i = 0; i < 5; i++) { 
    int retval = client->connect(host, httpsPort);
    if (retval == 1) {
      flag = true;
      Serial.println("Connected");
      break;
    } else {
      Serial.println("Connection failed. Retrying...");
    }
  }
  if (!flag) {
    Serial.print("Could not connect to server: ");
    Serial.println(host);
    return;
  }
  delete client;    
  client = nullptr; 
}
 
void loop() {
  // Wait for NFC input
  readNFC();
  
  // Check for tagId1
  if (tagId == tagId1) {
    if (digitalRead(ledpin1) == 0) {
      digitalWrite(ledpin1, HIGH);
      user = "Gowtham";
      id = "192111137";
      enter = "present";
      updatesheet(user, id, enter);
      tagId = "";
      delay(1000);
    } else if (digitalRead(ledpin1) == 1) {
      digitalWrite(ledpin1, LOW);
      user = "Gowtham";
      id = "192111137";
      enter = "present";
      updatesheet(user, id, enter);
      tagId = "";
      delay(1000);
    }
  }
  
  // Check for tagId2
  if (tagId == tagId2) {
    if (digitalRead(ledpin2) == 0) {
      digitalWrite(ledpin2, HIGH);
      user = "Bharathwaj";
      id = "192124033";
      enter = "present";
      updatesheet(user, id, enter);
      tagId = "";
      delay(1000);
    } else if (digitalRead(ledpin2) == 1) {
      digitalWrite(ledpin2, LOW);
      user = "Bharathwaj";
      id = "192124033";
      enter = "present";
      updatesheet(user, id, enter);
      tagId = "";
      delay(1000);
    }
  }
}

void updatesheet(String user, String id, String enter) {
  static bool flag = false;
  if (!flag) {
    client = new HTTPSRedirect(httpsPort);
    client->setInsecure();
    flag = true;
    client->setPrintResponseBody(true);
    client->setContentTypeHeader("application/json");
  }
  if (client != nullptr) {
    if (!client->connected()) {
      client->connect(host, httpsPort);
    }
  } else {
    Serial.println("Error creating client object!");
  }
  
  // Create json object string to send to Google Sheets
  payload = payload_base + "\"" + user + "," + id + "," + enter + "\"}";
  
  // Publish data to Google Sheets
  Serial.println("Publishing data...");
  Serial.println(payload);
  if (client->POST(url, host, payload)) {
    // do stuff here if publish was successful
  } else {
    // do stuff here if publish was not successful
    Serial.println("Error while connecting");
  }
  
  // A delay of several seconds is required before publishing again    
  delay(5000);
}

void readNFC() {
  if (nfc.tagPresent()) {
    NfcTag tag = nfc.read();
    tag.print();
    tagId = tag.getUidString();
    Serial.println("Tag id");
    Serial.println(tagId);
  }
  delay(1000);
}