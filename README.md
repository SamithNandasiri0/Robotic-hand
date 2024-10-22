# Robotic Hand with Arduino Nano and Python

This project demonstrates how to create a robotic hand using an **Arduino Nano** to control five servo motors via **Python**. The servos are moved based on finger positions detected through the camera feed.

## Pin Connections:
- **Servo 1** : D8
- **Servo 2** : D9
- **Servo 3** : D10
- **Servo 4** : D11
- **Servo 5** : D12
- **All Servo VCC pins** : Connect to an external 5V 2A power supply (+)
- **All Servo GND pins** : Connect to the external power supply ground (-)
- **GND** : Ensure to connect the Arduino Nano GND pin and external power supply GND pin together for common grounding.

## Arduino Setup

1. **Open Arduino IDE**.
2. Go to `Files -> Examples -> Firmata -> StandardFirmata`.
3. Select the correct board and port.
4. Upload the `StandardFirmata` code to your Arduino Nano board.

## Running the Project

This project is divided into two Python scripts:
- `Controller.py`: Handles the servo motor movements based on detected finger positions.
- `Camera.py`: Uses a camera to detect hand gestures.

### Steps to Run:

1. First, ensure that the Arduino Nano is connected to the system.
2. Run the **Controller** script:
   ```bash
   python Controller.py
