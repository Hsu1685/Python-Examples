//Arduino送給PC
#define SEND_START_1    214
#define SEND_START_2    228
#define SEND_START_3    110         //[V011j]
#define ID    2
#define CMD    7
#define LEN    4



unsigned char data1 = 0;
unsigned char data2 = 0;
unsigned char data3 = 0;
unsigned char data4 = 0;
unsigned char checksum = 0;

void setup() {
    Serial.begin(19200);
}

void loop() {
    Serial.write (SEND_START_1);
    Serial.write (SEND_START_2);
    Serial.write (SEND_START_3);
    Serial.write (ID);
    Serial.write (CMD);
    // Serial.write (37);             //資料長度  //ES34追加 - 20160823
    Serial.write (LEN);             //資料長度  //ES34追加 - 20160823

    data2 = random(255);
    data4 = random(128);

    Serial.write (data1);
    Serial.write (data2);
    Serial.write (data3);
    Serial.write (data4);

    data1++;
    data3--;

    checksum = ID + CMD +LEN + data1 + data2 + data3 + data4;

    Serial.write (checksum);
    delay(17);
}
