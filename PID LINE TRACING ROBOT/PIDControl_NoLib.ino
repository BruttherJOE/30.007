const uint8_t SensorPins[] = {A1,A2,A3,A4};
uint8_t SensorCount = 0;

const uint16_t blackThreshold[] = {700, 700, 850, 700};
const uint16_t sensorDist[] = {1, 9, 13, 21}; //1,8,16,23 original
const uint16_t ldrThreshold = 400; //800 for touch

//constants in PID
float Kp = 10; 
float Ki = 0;
float Kd = 16;
float P;
float I;
float D;

int lastError = 0;
boolean onoff = false; //state of robot (true for permanently on and skip LDR phase)

//Increasing the maxspeed can damage the motors - at a value of 255 the 6V motors will receive 7.4 V
//comments are previous test params that worked, but the actual ones worked better
const uint8_t basespeedA = 100; //left motor 100
const uint8_t basespeedB = 100; //right 100
const uint8_t maxspeedA = 160; //left motor 150
const uint8_t maxspeedB = 160; //right 150
const float dutycycle = 0.5;
int cycletime = 50;
//200 max 100 base was our initial test - too fast

//Set up the drive motor carrier pins
int ML_Dir = 4;
int ML_Speed = 5;
int MR_Dir = 7;
int MR_Speed = 6;
int LDR = A0;

void setup() {
  Serial.begin(9600);
  SensorCount = sizeof(SensorPins)/sizeof(uint8_t); //Length of array
  for (int i = 0; i < SensorCount; i++){
    pinMode(SensorPins[i], INPUT);
  }

  pinMode(ML_Dir, OUTPUT);
  pinMode(ML_Speed, OUTPUT);
  pinMode(MR_Dir, OUTPUT);
  pinMode(MR_Speed, OUTPUT);

  delay(500);
  pinMode(LED_BUILTIN, OUTPUT);

  boolean Ok = false;
  forward_brake(0, 0);
}

void loop() {
  float lastPosition = 2.5;
  if (onoff == false){
    forward_brake(0, 0);
    Serial.println(analogRead(LDR));
    if (analogRead(LDR) < ldrThreshold)
      onoff = true;  
  }
  
  else {
    PID_control();
  }
}
void forward_brake(int motorspeedA, int motorspeedB) {
  Serial.print(motorspeedA);Serial.print(" ");Serial.println(motorspeedB);
  digitalWrite(ML_Dir, HIGH);
  digitalWrite(MR_Dir, HIGH);
  analogWrite(ML_Speed, motorspeedA);
  analogWrite(MR_Speed, motorspeedB);
  delay(cycletime * dutycycle);
  analogWrite(ML_Speed, 0);
  analogWrite(MR_Speed, 0);
  delay(cycletime * (1-dutycycle));
}

void PID_control() {
  float position = ReadSensors(blackThreshold);
  Serial.print(position);
  Serial.print("\n");
  float error = 0;
  if (position == 0)
    error = lastError;
  else
    error = 12 - position;
  Serial.println(position); 
  Serial.println(error);
  P = error;
  I = I + error;
  D = error - lastError;
  lastError = error;
  int motorspeed = P*Kp + I*Ki + D*Kd;
  int motorspeedA = basespeedA - motorspeed;
  int motorspeedB = basespeedB + motorspeed;
  
  if (motorspeedA > maxspeedA) {
    motorspeedA = maxspeedA;
  }
  if (motorspeedB > maxspeedB) {
    motorspeedB = maxspeedB;
  }
  if (motorspeedA < 0) {
    motorspeedA = 0;
  }
  if (motorspeedB < 0) {
    motorspeedB = 0;
  }
  
  forward_brake(motorspeedA, motorspeedB);
}

int ReadSensors(uint16_t threshold[]){
  float total = 0;
  int blackCount = 0;
  for (int i = 0; i < SensorCount; i++){
    Serial.print(SensorPins[i]);
    Serial.print(": ");
    Serial.print(analogRead(SensorPins[i]));
    Serial.print("\t\t");
    int reading = analogRead(SensorPins[i]);

    if (reading > threshold[i]){
      total += sensorDist[i];
      blackCount++;
    }
  }
  //Serial.println();
  if (blackCount == 0)
    return 0;
  return total/blackCount;
}
