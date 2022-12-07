
int sensorPin = A0;    // connect o LDR no A0
int sensorValue = 0;  // variavel que armazena o valor do sensor
int thresholdValue = 45; // aqui voce vai colocar o valor para o dinossouro pular de acordo com a luz da tela.
// use o serial do arduino para colocar o valor exato. 
void setup() {
  Serial.begin(9600);  // serial begin 9600. Importante se voce trocar esse numero, lembre-se de trocar no python tambem.
}

void loop() {
  // Le o valor do sensor: 
  sensorValue = analogRead(sensorPin); // lendo o sensor.
  Serial.println(sensorValue);  // variavel para voce encotrar o valor do sensor e colocar no ( int thresholdValue ).
  // voce pode comentar se quiser. 
  
  if(sensorValue <= thresholdValue){   // detectando o obstaculo. 
    Serial.println(1);                 // manda para o serial se for verdadeira.
  }
  delay(40);                         
}
