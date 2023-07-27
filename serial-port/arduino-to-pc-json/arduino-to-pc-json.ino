//Arduino送給PC
#include <ArduinoJson.h>

DynamicJsonDocument doc(1024);
unsigned long previousMillis = 0;
const long interval = 5;    // 設定間隔時間，1000ms
unsigned int data_number = 0;

void setup() {
    Serial.begin(19200);
}

void loop() {
    unsigned long currentMillis = millis();

    doc["number"] = data_number++;
    doc["time"] = currentMillis;
    doc["pid"] = random(256);
    doc["byte"][0] = random(256);
    doc["byte"][1] = random(256);
    doc["byte"][2] = random(256);
    doc["byte"][3] = random(256);
    doc["byte"][4] = random(256);
    doc["byte"][5] = random(256);
    doc["byte"][6] = random(256);
    doc["byte"][7] = random(256);
    doc["byte"][8] = random(256);
    doc["byte"][9] = random(256);
    doc["byte"][10] = random(256);
    doc["byte"][11] = random(256);
    doc["byte"][12] = random(256);
    doc["byte"][13] = random(256);
    doc["byte"][14] = random(256);
    doc["byte"][15] = random(256);
    doc["checksum"] = random(256);
    doc["baud"] = 9600;

    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;
        serializeJson(doc, Serial);
        Serial.println();
    }
}
