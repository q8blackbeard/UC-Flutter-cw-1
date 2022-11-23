void main() {
  // cw 2
  double height = 1.70, weight = 80, BMI;
  BMI = weight / (height * height);
  print(BMI < 18.6
      ? "Underweight"
      : BMI > 24.9
          ? "Overweight"
          : "Normal");
}
