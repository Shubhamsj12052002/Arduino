#include <ArduinoTimer.h>

// Pin configurations
const int lm35Pin = A0;    // LM35 temperature sensor pin
const int ledPin = 13;     // Onboard LED pin

// Temperature thresholds
const int lowTempThreshold = 30;  // Below this temperature, LED blinks every 250ms
const int highTempThreshold = 30; // Above this temperature, LED blinks every 500ms

// Timer for LED blinking
Timer<1, millis> ledBlinkTimer;

// Function declarations
void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set LM35 pin as input
  pinMode(lm35Pin, INPUT);

  // Set LED pin as output
  pinMode(ledPin, OUTPUT);

  // Attach timer callback functions
  ledBlinkTimer.every(250, blinkLedLowTemp);
  ledBlinkTimer.every(500, blinkLedHighTemp);
}

void loop() {
  // Read temperature from LM35 sensor
  int temperature = readTemperature();

  // Check temperature and trigger corresponding timer callback
  if (temperature < lowTempThreshold) {
    ledBlinkTimer.update();
  } else if (temperature > highTempThreshold) {
    ledBlinkTimer.update();
  }

  // You can include additional logic here based on temperature readings
}

// Function to read temperature from LM35 sensor
int readTemperature() {
  // Read the analog value from LM35
  int sensorValue = analogRead(lm35Pin);

  // Convert the analog value to temperature in Celsius
  float temperatureC = (sensorValue * 5.0 / 1024.0) * 100.0;

  // Print temperature to serial monitor (optional)
  Serial.print("Temperature: ");
  Serial.print(temperatureC);
  Serial.println(" °C");

  return temperatureC;
}

// Callback function for low temperature LED blinking
void blinkLedLowTemp() {
  digitalWrite(ledPin, !digitalRead(ledPin)); // Toggle LED state
}

// Callback function for high temperature LED blinking
void blinkLedHighTemp() {
  digitalWrite(ledPin, !digitalRead(ledPin)); // Toggle LED state
}
