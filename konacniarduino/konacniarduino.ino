#include <Servo.h>
                            
const int trigPin = 12;
const int echoPin = 11;
const int servo = 9;
const int crvena = 8;
const int zelena = 6;
const int svetloPin = 5;
const int buzzerPin = 4;
const int foto = 0;
const int termo = 1;
int p, a, t, i, j, r, mintemp = 400, maxtemp = 500, valtemp = 0, pos = 0;
char _status = 'a';
Servo motor;
void setup () {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);              //definisemo svaki pin
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(svetloPin, OUTPUT);
  pinMode(zelena, OUTPUT);
  pinMode(crvena, OUTPUT);
  pinMode(servo, OUTPUT);
  delay (100);
  digitalWrite(svetloPin, LOW);          //na pocetku rada sve diode stavimo da ne svetle
  digitalWrite(zelena, LOW);
  digitalWrite(crvena, LOW);
  motor.attach(servo);                   //ukljucujemo servo motor

}

void fotoIntenzitet() {                  //funkcija sluzi za pametno svetlo
  int osvetljenje = analogRead(foto);
  int intenzitet = map(osvetljenje, 0, 1023, 255, 0);
  if ((intenzitet < 43) || p) {         //ispod odredjene granice dioda ne svetli
    p = 1;
    if ( intenzitet > 50) p = 0;
    analogWrite(svetloPin, LOW);
  }                                     //iznad granice, dioda ce svetleti odredjenim intenzitetom, u zavisnosti od osvetljenja u prostoriji
  else  analogWrite(svetloPin, intenzitet);
}

void garaza() {                         //funkcija sluzi za pametnu garazu

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long vreme = pulseIn(echoPin, HIGH);
  int razdaljina = (vreme / 2) * 0.0343;
  if ((razdaljina <  10)) {             //proveravamo da li je razdaljina iznad ili ispod 10cm, ako je manja od 10cm, ukljucujemo buzzer
    j = 5 * round(razdaljina) + 10;     
  }
  if (i < j) {
    tone (buzzerPin, 500);
    i++;
  }
  else {
    noTone(buzzerPin);
    i++;
    if (i >= 2 * j) {                   //ako je veca od 10cm, ne cuje se buzzer
      i = 0;
      j = 0;
    }
  }
}
void klima() {                          //funkcija sluzi za pametno regulisanje temperature
  valtemp = analogRead(termo);
  if ((valtemp > 540) || t) {           //proveramo da li se temperatura nalazi iznad ili ispod zadate granice, pa u zavisnosti od toga okrecemo servo motor pod odredjenim uglom
    if (!t) {
      t = 1;
      motor.write(90);          
    }
    if (valtemp < 520) {
      t = 0;
      a = 1;
    }
  }
  else if (a) {
    motor.write(0);
    a = 0;
  }
}
void alarm() {                         //funkcija alarm sluzi za paljenje crvene diode i buzzera
  
    digitalWrite(crvena, HIGH);
    tone (buzzerPin, 1500);
    delay(500);
    digitalWrite(crvena, LOW);
    noTone(buzzerPin);
    delay(500);
}
void loop () {
  //Serial.println(_status);
  if ((_status == 'a') && Serial.available()) _status = Serial.read();
  if (_status == '0') alarm();        //ako nam se iz python-a posalje '0' pozivamo funkciju alarm
  if (_status == '1') {               //ako nam se iz python-a posalje '1' pozivamo funkcije za pametno svetlo, pametnu garazu i pametnu regulaciju temperature, i ukljucujemo zelenu diodu
    fotoIntenzitet();
    garaza();
    klima();
    digitalWrite(zelena, HIGH);
  }
}

