// firstName, lastName , age ,hobby
void main() {
  // cw 1
  String firstName = "Salman", lastName = "Ali";
  int age = 27;
  var hobby = "Programming";
  print(
      "First Name: ${firstName.toUpperCase()}\nLast Name: ${lastName.toLowerCase()}\nI'm $age, my hobby is $hobby\n");
  // bonus
  double tempF = 80.0, tempC;
  tempC = (tempF - 32) / 1.8;
  print("$tempF°F = ${tempC.roundToDouble()}°C");
}
