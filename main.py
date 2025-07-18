from machine import Pin, PWM, UART
import time
uart = UART(0,9600)#rx 0 tx1

d0 = Pin(6, Pin.IN)
d1 = Pin(7, Pin.IN)
d2 = Pin(8, Pin.IN)
d3 = Pin(9, Pin.IN)

IN1 = Pin(10, Pin.OUT)
IN2 = Pin(11, Pin.OUT)

IN3 = Pin(12, Pin.OUT)
IN4 = Pin(13, Pin.OUT)
IN5 = Pin(18, Pin.OUT)
IN6 = Pin(19, Pin.OUT)

IN7 = Pin(20, Pin.OUT)
IN8 = Pin(21, Pin.OUT)

def read_rf():
    return (d0.value() + d1.value()* 2 + d2.value() * 4 + d3.value() * 8)
def forward():
        # קידמי שמאלי (IN1 - IN2)
        IN1.value (1)
        IN2.value (0)
            
        #שמאל אחורי (IN3- IN4)
        IN3.value (1)
        IN4.value (0)
            
        # ימיני אחורי (IN5 - IN6)
        IN5.value (1)
        IN6.value (0)
            
        # קידמי ימיני
        IN7.value (1)
        IN8.value (0)

def backward():
        # קידמי שמאלי (IN1 - IN2)
        IN1.value (0)
        IN2.value (1)
            
        #שמאל אחורי (IN3- IN4)
        IN3.value (0)
        IN4.value (1)
            
        # ימיני אחורי (IN5 - IN6)
        IN5.value (0)
        IN6.value (1)
            
        # קידמי ימיני
        IN7.value (0)
        IN8.value (1)



def stop():
    
        # קידמי שמאלי (IN1 - IN2)
        IN1.value (0)
        IN2.value (0)
            
        #שמאל אחורי (IN3- IN4)
        IN3.value (0)
        IN4.value (0)
            
        # ימיני אחורי (IN5 - IN6)
        IN5.value (0)
        IN6.value (0)
            
        # קידמי ימיני
        IN7.value (0)
        IN8.value (0)







def backward_right():
    
        # קידמי שמאלי (IN1 - IN2)
        IN1.value(0)
        IN2.value(1)

        # קידמי ימיני (IN7 - IN8)
        IN7.value(0)
        IN8.value(0)

        # ימיני אחורי (IN5 - IN6)
        IN5.value(0)
        IN6.value(1)

        # שמאל אחורי (IN3- IN4)
        IN3.value(0)
        IN4.value(0)



def driving_right():
    
        # קידמי שמאלי (IN1 - IN2)
        IN1.value(1)
        IN2.value(0)

        # קידמי ימיני (IN7 - IN8)
        IN7.value(0)
        IN8.value(1)

        # ימיני אחורי (IN5 - IN6)
        IN5.value(0)
        IN6.value(1)

        # שמאל אחורי (IN3- IN4)
        IN3.value(1)
        IN4.value(0)


def parking_right():
    
        # קידמי שמאלי (IN1 - IN2)
        IN1.value(0)
        IN2.value(1)

        # קידמי ימיני (IN7 - IN8)
        IN7.value(1)
        IN8.value(0)

        # ימיני אחורי (IN5 - IN6)
        IN5.value(0)
        IN6.value(1)

        # שמאל אחורי (IN3- IN4)
        IN3.value(1)
        IN4.value(0)
        
        
        
        
        
        
def backward_left():
    
            # קידמי שמאלי (IN1 - IN2)
        IN1.value(0)
        IN2.value(0)

        # קידמי ימיני (IN7 - IN8)
        IN7.value(0)
        IN8.value(1)

        # ימיני אחורי (IN5 - IN6)
        IN5.value(0)
        IN6.value(0)

        # שמאל אחורי (IN3- IN4)
        IN3.value(0)
        IN4.value(1)
        
def driving_left():
    
            # קידמי שמאלי (IN1 - IN2)
        IN1.value(0)
        IN2.value(1)

        # קידמי ימיני (IN7 - IN8)
        IN7.value(1)
        IN8.value(0)

        # ימיני אחורי (IN5 - IN6)
        IN5.value(1)
        IN6.value(0)

        # שמאל אחורי (IN3- IN4)
        IN3.value(0)
        IN4.value(1)
        
def parking_left():
    
            # קידמי שמאלי (IN1 - IN2)
        IN1.value(1)
        IN2.value(0)

        # קידמי ימיני (IN7 - IN8)
        IN7.value(0)
        IN8.value(1)

        # ימיני אחורי (IN5 - IN6)
        IN5.value(1)
        IN6.value(0)

        # שמאל אחורי (IN3- IN4)
        IN3.value(0)
        IN4.value(1)

while True:
    if uart.any():
        data = uart.read()
        print(data)
        if data==b'forward':
            forward()
        elif data==b'stop':
            stop()
        elif data==b'backward':
            backward()
        elif data==b'parking right':
            parking_right()
        elif data==b'parking left':
            parking_left()    
        elif data==b'driving right':
            driving_right()
        elif data==b'driving left':
            driving_left()
        elif data==b'backward right':
            backward_right()
        elif data==b'backward left':
            backward_left()
    data_from_rf = read_rf()
    if data_from_rf == 0:
        stop()
    elif data_from_rf == 1:
        forward()
    elif data_from_rf == 2:
        backward()
    elif data_from_rf == 3:
        parking_right()
    elif data_from_rf == 4:
        parking_left()
    elif data_from_rf == 5:
        driving_right()
    elif data_from_rf == 6:
        driving_left()
    elif data_from_rf == 7:
        backward_right()
    elif data_from_rf == 8:
        backward_left()
        