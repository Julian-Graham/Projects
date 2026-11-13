import board
import busio
import math
import time
from adafruit_servokit import ServoKit

stop=[ 
    [(0, 0, -6.79)],
    [(0.00, 0, -9.60)], 
    [(0, 0, -6.79)],
    None,
    [(0, 0, -6.79)],
    [(0.00, 0, -9.60)], 
    [(0, 0, -6.79)]
    ]

N = [
    [(0, 0, -6.79),
     (0, 0, -6.79),
     (0, 0, -6.79),
     (0, 0, -6.79)],
    
    [(0.00, 0, -9.60),
     (0.00, 0, -9.60),
     (0.00, 0, -9.60),
     (0.00, 0, -9.60)],
    
    [(.1, 0, -6.79),
     (-1, 0, -6.79),
     (0, 0, -6.79),
     (0, 0, -6.79)],
    
    None,
    
    [(0, 0, -6.79),
     (0, 0, -6.79),
     (0, 0, -6.79),
     (0, 0, -6.79)],
    
    [(0.00, 0, -9.60),
     (0.00, 0, -9.60),
     (0.00, 0, -9.60),
     (0.00, 0, -9.60)],
    
    [(0, 0, -6.79),
     (0, 0, -6.79),
     (0, 0, -6.79),
     (0, 0, -6.79)]
    ]

S = []
for leg in N:
    if leg is None:
        S.append(None)
    else:
        S.append(leg[::-1])

# Create I2C bus (shared by both boards)
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)

# Two ServoKit instances with different addresses
kit1 = ServoKit(channels=16, i2c=i2c, address=0x40)  # PCA1: 1,2,3
kit2 = ServoKit(channels=16, i2c=i2c, address=0x41)  # PCA2: 4,5,6

J1_4_a=8
J2_4_a=9
J3_4_a=10

J1_5_a=4
J2_5_a=5
J3_5_a=6

J1_6_a=0
J2_6_a=1
J3_6_a=2

#pca 2
J1_0_b=8
J2_0_b=9
J3_0_b=10

J1_1_b=4
J2_1_b=5
J3_1_b=6

J1_2_b=0
J2_2_b=1
J3_2_b=2

L1=3.8
L2=5.8  #length for link 2
L3=7.8  #length for link 3

pace=.5

def IK2D(x, y):
    d = math.sqrt(x**2 + y**2)

    if d > (L2 + L3):
        print("Target is out of reach")
        return None

    cos_J3 = (d**2 - L2**2 - L3**2) / (2 * L2 * L3)
    cos_J3 = max(min(cos_J3, 1), -1)

    phi = math.atan2(y, x)

    cos_beta = (x**2 + y**2 + L2**2 - L3**2) / (2 * L2 * d)
    cos_beta = max(min(cos_beta, 1), -1)
    beta = math.acos(cos_beta)

    J3 = abs(math.degrees(math.acos(cos_J3)))
    J2 = abs(math.degrees(beta-phi))

    return round(J2, 2), round(J3, 2)

def IK3D(x, y, z):

    # Base rotation
    J1 = abs(math.degrees(math.atan2(z, x)))

    # Horizontal distance from robot center
    horizontal = math.sqrt(x**2 + z**2)

    # Remove coxa length
    horizontal -= L1

    # Existing 2D IK
    J2, J3 = IK2D(horizontal, y)

    return J1, J2, J3


def pca1(leg_id, J1, J2, J3):
    J1 = max(0, min(180, J1))
    J2 = max(0, min(180, J2))
    J3 = max(0, min(180, J3))
    if leg_id == 4:
        kit1.servo[J1_4_a].angle = J1
        kit1.servo[J2_4_a].angle = J2
        kit1.servo[J3_4_a].angle = J3
    elif leg_id==5:
        kit1.servo[J1_5_a].angle = J1
        kit1.servo[J2_5_a].angle = J2
        kit1.servo[J3_5_a].angle = J3
    elif leg_id==6:
        kit1.servo[J1_6_a].angle = J1
        kit1.servo[J2_6_a].angle = J2
        kit1.servo[J3_6_a].angle = J3
 
def pca2(leg_id, J1, J2, J3):
    J1 = 180 - J1
    J2 = 180 - J2
    J3 = 180 - J3
    J1 = max(0, min(180, J1))
    J2 = max(0, min(180, J2))
    J3 = max(0, min(180, J3))
    if leg_id ==0:
        kit2.servo[J1_0_b].angle =J1
        kit2.servo[J2_0_b].angle =J2
        kit2.servo[J3_0_b].angle =J3
    elif leg_id==1:
        kit2.servo[J1_1_b].angle =J1
        kit2.servo[J2_1_b].angle =J2
        kit2.servo[J3_1_b].angle =J3
    elif leg_id==2:
        kit2.servo[J1_2_b].angle = J1
        kit2.servo[J2_2_b].angle = J2
        kit2.servo[J3_2_b].angle = J3



def forward():
    global pace
    # Step through both legs together
    for step in range(4):
        # -------- LEG 0
        x,y,z = N[0][step]
        J1,J2,J3 = IK3D(x, y, z)
        print(f"Leg 0: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca2(0,J1,J2,J3)

        # -------- LEG 1 --------
        x,y,z = N[1][step]
        J1,J2,J3 = IK3D(x, y, z)
        # print(f"Leg 1: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca2(1,J1,J2,J3)

        # -------- LEG 2 --------
        x,y,z = N[2][step]
        J1,J2,J3 = IK3D(x, y, z)
        # print(f"Leg 2: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca2(2,J1,J2,J3)
    
        #leg 4
        x,y,z = N[4][step]
        J1,J2,J3 = IK3D(x, y, z)
#         print(f"Leg 4: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}° | ({x,y,z})")
        pca1(4,J1,J2,J3)
        
        #leg 5
        x,y,z = N[5][step]
        J1,J2,J3 = IK3D(x, y, z)
#         print(f"Leg 5: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca1(5,J1,J2,J3)

        # -------- LEG 6 --------
        x,y,z = N[6][step]
        J1,J2,J3 = IK3D(x, y, z)
#         print(f"Leg 6: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca1(6,J1,J2,J3)
        time.sleep(pace)

def backward():
    global pace
    for step in range(4):
        # -------- LEG 0
        x,y,z = S[0][step]
        J1,J2,J3 = IK3D(x, y, z)
        # print(f"Leg 0: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca2(0,J1,J2,J3)

        # -------- LEG 1 --------
        x,y,z = S[1][step]
        J1,J2,J3 = IK3D(x, y, z)
        # print(f"Leg 1: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca2(1,J1,J2,J3)

        # -------- LEG 2 --------
        x,y,z = S[2][step]
        J1,J2,J3 = IK3D(x, y, z)
        # print(f"Leg 2: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca2(2,J1,J2,J3)
    
        #leg 4
        x,y,z = S[4][step]
        J1,J2,J3 = IK3D(x, y, z)
        # print(f"Leg 0: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca1(4,J1,J2,J3)
        
        #leg 5
        x,y,z = S[5][step]
        J1,J2,J3 = IK3D(x, y, z)
        # print(f"Leg 1: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca1(5,J1,J2,J3)

        # -------- LEG 6 --------
        x,y,z = S[6][step]
        J1,J2,J3 = IK3D(x, y, z)
        # print(f"Leg 2: J1={J1:.1f}°, J2={J2:.1f}°, J3={J3:.1f}°")
        pca1(6,J1,J2,J3)
        time.sleep(pace)

def halt():
    for step in range(4):
        # -------- LEG 0
        x,y,z = stop[0][step]
        J1,J2,J3 = IK3D(x, y, z)
        print(f"Leg 0: J1={J1:.2f}°, J2={J2:.2f}°, J3={J3:.2f}° | ({x,y,z})")
        pca2(0,J1,J2,J3)

        # -------- LEG 1 --------
        x,y,z = stop[1][step]
        J1,J2,J3 = IK3D(x, y, z)
        print(f"Leg 1: J1={J1:.2f}°, J2={J2:.2f}°, J3={J3:.2f}° | ({x,y,z})")
        pca2(1,J1,J2,J3)

        # -------- LEG 2 --------
        x,y,z = stop[2][step]
        J1,J2,J3 = IK3D(x, y, z)
        print(f"Leg 2: J1={J1:.2f}°, J2={J2:.2f}°, J3={J3:.2f}° | ({x,y,z})")
        pca2(2,J1,J2,J3)
        
        # -------- LEG 4
        x,y,z = stop[4][step]
        J1,J2,J3 = IK3D(x, y, z)
        print(f"Leg 4: J1={J1:.2f}°, J2={J2:.2f}°, J3={J3:.2f}° | ({x,y,z})")
        pca1(4,J1,J2,J3)

        # -------- LEG 5 --------
        x,y,z = stop[5][step]
        J1,J2,J3 = IK3D(x, y, z)
        print(f"Leg 5: J1={J1:.2f}°, J2={J2:.2f}°, J3={J3:.2f}° | ({x,y,z})")
        pca1(5,J1,J2,J3)
        # -------- LEG 6 --------
        x,y,z = stop[6][step]
        J1,J2,J3 = IK3D(x, y, z)
        print(f"Leg 6: J1={J1:.2f}°, J2={J2:.2f}°, J3={J3:.2f}° | ({x,y,z})")
        pca1(6,J1,J2,J3)
             
while True:
    forward()