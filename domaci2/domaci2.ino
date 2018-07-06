#include <Servo.h>


const int echoPin = 12;
const int trigPin = 11;
const int buzzerPin = 10;
const int svetloPin = 9;
const int zelena = 8;
const int crvena = 7;
const int servo = 6;

const int foto = 0;
const int termo = 1;

long vreme;
int razdaljina, intenzitet, osvetljenje, mintemp=400, maxtemp=500, valtemp=0, pos=0;

Servo motor;

void setup () {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(svetloPin, OUTPUT);
  pinMode(zelena, OUTPUT);
  pinMode(crvena, OUTPUT);
  pinMode(servo, OUTPUT);
//  motor.attach(6);
 
  delay (100);
  
  digitalWrite(svetloPin, LOW);
  digitalWrite(zelena, LOW);
  digitalWrite(crvena, LOW);
  
}

void loop (){
  osvetljenje = analogRead(foto);
  intenzitet = map(osvetljenje, 0, 1023, 255, 0);
  if (intenzitet < 50)
  {
    analogWrite(svetloPin, LOW);
    }
    else{
  analogWrite(svetloPin, intenzitet);
  }

    
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  vreme = pulseIn(echoPin, HIGH);
  razdaljina = (vreme/2)*0.0343;
  if (razdaljina < 10) {
    Serial.println("Previse blizu");
    tone (buzzerPin, 750);
    delay(300);
    noTone(buzzerPin);
  }
  else{
   Serial.print("Razdaljina je: "); 
   Serial.println(razdaljina);
  }
  
//Pametni sistem regulacije temperature

//  valtemp = analogRead(termo);
//  Serial.print(valtemp);
//   delay(100);
//  pos = map(valtemp, mintemp, maxtemp, 0, 180);   //u zavisnosti od temperature menjamo ugao servo motora
//  motor.write(pos);
//  
}

