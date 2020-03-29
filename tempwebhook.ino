

int led = D7;


void setup() {
    pinMode(led, OUTPUT);
    
     Particle.subscribe("hook-response/temp", myHandler, MY_DEVICES);
}

void myHandler(const char *event, const char *data) {
  // Handle the integration response


}

void loop() {
    
    
    digitalWrite(led, HIGH);   
    
String temp = String(random(60, 80));
  Particle.publish("temp",  temp, PRIVATE);
  

  delay(30000);               

  digitalWrite(led, LOW);    
  delay(30000);         

}