unsigned long previousMillis = 0;
const long interval = 1000;    // 設定間隔時間，1000ms
unsigned int data_number = 0;

void setup() {
    Serial.begin(19200);
}

void loop() {
    unsigned long currentMillis = millis();

    char str1[] = "{\"firstName\":\"John\",\"lastName\":\"Smith\",\"sex\":\"male\",\"age\":";
    char str3[] = "}";
    int age =  random(13, 36);

    // 轉換數字為string
    char buf1[16];
    // char *buf1 = (char*)malloc(16); 如果free(buf1)是在下方時間間隔到了才執行，會造成記憶體在loop()下配置太多，系統停擺
    itoa(age, buf1, 10);

    // 把3個字串合在一起
    char buf2[128];
    // char *buf2 = (char*)malloc(128); 和buf1同樣的狀況，不能在這裡配置記憶體
    strcpy(buf2, str1);
    strcat(buf2, buf1);
    strcat(buf2, str3);


    if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;
        Serial.println(buf2);
        // free(buf1);
        // free(buf2);
    }
}
