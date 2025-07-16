from machine import Pin, PWM, ADC, I2C
from pico_i2c_lcd import I2cLcd
import time
import urandom

class ServoCircuitGame:
    def __init__(self):
        # Pin setup
        self.potentiometer = ADC(26)  # Potentiometer on ADC0
        self.servo_pin = 18           # Servo control pin
        
        # I2C LCD setup
        self.i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
        self.I2C_ADDR = self.i2c.scan()[0]
        self.lcd = I2cLcd(self.i2c, self.I2C_ADDR, 2, 16)
        
        # Servo setup
        self.servo = PWM(Pin(self.servo_pin))
        self.servo.freq(50)  # 50Hz for servo control
        
        # Servo duty cycle constants (adjust for your servo)
        self.MIN_DUTY = 1802   # 0 degrees
        self.MAX_DUTY = 7864   # 180 degrees
        
        # Game state
        self.current_angle = 90  # Start at center position
        self.target_angle = 90
        self.score = 0
        self.tolerance = 5  # Degrees tolerance for "correct" position
        self.game_level = 1
        self.moves_completed = 0
    
    def map_value(self, value, from_min, from_max, to_min, to_max):
        """Map a value from one range to another"""
        return int((value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min)
    
    def set_servo_angle(self, angle):
        """Set servo to specific angle (0-180 degrees)"""
        # Constrain angle to valid range
        angle = max(0, min(180, angle))
        
        # Map angle to duty cycle
        duty = self.map_value(angle, 0, 180, self.MIN_DUTY, self.MAX_DUTY)
        self.servo.duty_u16(duty)
        
        return angle
    
    def read_potentiometer_angle(self):
        """Read potentiometer and convert to servo angle"""
        pot_reading = self.potentiometer.read_u16()
        angle = self.map_value(pot_reading, 0, 65535, 0, 180)
        return angle
    
    def generate_new_target(self):
        """Generate a new random target angle"""
        # Ensure new target is significantly different from current
        while True:
            new_target = urandom.randint(10, 170)  # Avoid extreme edges
            if abs(new_target - self.current_angle) > 20:  # Must be at least 20 degrees different
                self.target_angle = new_target
                break
    
    def display_instruction(self):
        """Display movement instruction on LCD"""
        self.lcd.clear()
        
        # Calculate difference and direction
        difference = self.target_angle - self.current_angle
        
        if abs(difference) <= self.tolerance:
            self.lcd.putstr("CORRECT!")
            self.lcd.move_to(0, 1)
            self.lcd.putstr(f"Score: {self.score}")
        else:
            # Show direction and amount
            if difference > 0:
                direction = "RIGHT"
            else:
                direction = "LEFT"
            
            amount = abs(difference)
            
            # First line: direction and amount
            self.lcd.putstr(f"Turn {direction}")
            self.lcd.move_to(0, 1)
            self.lcd.putstr(f"{amount} degrees")
    
    def check_win_condition(self):
        """Check if player has reached the target"""
        if abs(self.current_angle - self.target_angle) <= self.tolerance:
            self.score += 10
            self.moves_completed += 1
            
            # Level up every 5 successful moves
            if self.moves_completed % 5 == 0:
                self.game_level += 1
                self.tolerance = max(2, self.tolerance - 1)  # Make it harder but not impossible
            
            # Brief success display
            self.lcd.clear()
            self.lcd.putstr("SUCCESS!")
            self.lcd.move_to(0, 1)
            self.lcd.putstr(f"Level: {self.game_level}")
            time.sleep(1)
            
            # Generate new target
            self.generate_new_target()
            return True
        
        return False
    
    def display_startup(self):
        """Display game startup message"""
        self.lcd.clear()
        self.lcd.putstr("Servo Circuit")
        self.lcd.move_to(0, 1)
        self.lcd.putstr("Game Starting...")
        time.sleep(2)
        
        self.lcd.clear()
        self.lcd.putstr("Turn pot to")
        self.lcd.move_to(0, 1)
        self.lcd.putstr("match target!")
        time.sleep(2)
    
    def cleanup(self):
        """Clean up resources when game ends"""
        self.lcd.clear()
        self.lcd.putstr("Game Over")
        self.lcd.move_to(0, 1)
        self.lcd.putstr(f"Final Score: {self.score}")
        self.servo.duty_u16(0)  # Turn off servo
        print(f"Final Score: {self.score}")
        print("Thanks for playing!")
    
    def run(self):
        """Main game loop"""
        print("Servo Circuit Game Starting!")
        print("Turn the potentiometer to match the target angle shown on LCD")
        
        # Initialize servo to center position
        self.current_angle = self.set_servo_angle(90)
        self.display_startup()
        
        # Generate first target
        self.generate_new_target()
        
        # Main game loop
        try:
            while True:
                # Read potentiometer and update servo
                pot_angle = self.read_potentiometer_angle()
                self.current_angle = self.set_servo_angle(pot_angle)
                
                # Check for win condition
                if not self.check_win_condition():
                    # Display current instruction
                    self.display_instruction()
                
                # Small delay for smooth operation
                time.sleep(0.1)
        
        except KeyboardInterrupt:
            print("\nGame stopped")
            self.cleanup()

# Create and run the game
game = ServoCircuitGame()
game.run()
