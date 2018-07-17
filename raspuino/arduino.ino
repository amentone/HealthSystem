#define USE_ARDUINO_INTERRUPTS true
#include <PulseSensorPlayground.h>


// costanti
#define buttonPin 2      // pin: pulsante
#define buttonLedPin 12  // pin: quando il led si accende indica che é possibile effettuare una misurazione 

#define pulsePinAnalog 0 // pin: sensore battito
#define pulseLedPin 13   // pin: quando il led si accende indica che il sensore ha rilevato il nostro battito
#define threshold 450

// variabili
int buttonState = 0;         // stato: per controllare lo stato del pulsante
int i = 0;

PulseSensorPlayground pulseSensor; // istanza di PulseSensorPlayground

void setup()
{
  // serial monitor
  Serial.begin(9600);

  // configurazione oggetto pulseSensor
  pulseSensor.analogInput(pulsePinAnalog);  // assegnazione pin analogico all'oggetto 
  pulseSensor.blinkOnPulse(pulseLedPin);
  pulseSensor.setThreshold(threshold);      // assegnazione della soglia massima per evitare segnalazioni errate
  
  // inizializza la modalitá del buttonLedPin come OUTPUT
  pinMode(buttonLedPin, OUTPUT);
  // inizializza la modalitá del buttonPin come INPUT
  pinMode(buttonPin, INPUT);

  pulseSensor.begin();
}

void loop()
{
  int myBPM;
	
  buttonState = digitalRead(buttonPin); // legge lo stato attuale del pulsante

  // controlla se il pulsante é "cliccato". Se si, lo stato é HIGH:
  if (buttonState == HIGH)
  {
    // accendi il LED:
    digitalWrite(buttonLedPin, HIGH);
  
    // inizia la misurazione
    myBPM = pulseSensor.getBeatsPerMinute();

    if(pulseSensor.sawStartOfBeat())        
      Serial.println(myBPM);     
	
    delay(50);
  }
  else
  {
    // spegni il LED:
    digitalWrite(buttonLedPin, LOW);
  }
}
