# Patient Vital Signs Analyzer

print("==============================")
print("  PATIENT VITAL SIGNS ANALYZER")
print("==============================")

name = input("Patient name: ")
age = int(input("Age: "))

heart_rate = float(input("Heart rate (BPM): "))
temperature = float(input("Temperature (°C): "))
spo2 = float(input("SpO2 (%): "))

systolic = float(input("Systolic BP (mmHg): "))
diastolic = float(input("Diastolic BP (mmHg): "))


print("\n--------- RESULTS ---------")

print(f"\nPatient: {name}")
print(f"Age: {age}")

# Heart rate
if 60 <= heart_rate <= 100:
    print(f"Heart Rate: {heart_rate:.1f} BPM - Within reference range")
else:
    print(f"Heart Rate: {heart_rate:.1f} BPM - Outside reference range")

# Temperature
if 36.1 <= temperature <= 37.2:
    print(f"Temperature: {temperature:.1f} °C - Within reference range")
else:
    print(f"Temperature: {temperature:.1f} °C - Outside reference range")

# SpO2
if spo2 >= 95:
    print(f"SpO2: {spo2:.1f}% - Within reference range")
else:
    print(f"SpO2: {spo2:.1f}% - Below reference range")

# Blood pressure
if systolic < 120 and diastolic < 80:
    print(f"Blood Pressure: {systolic:.0f}/{diastolic:.0f} mmHg - Within reference range")
else:
    print(f"Blood Pressure: {systolic:.0f}/{diastolic:.0f} mmHg - Above the selected reference range")
