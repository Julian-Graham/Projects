import matplotlib.pyplot as plt
import matplotlib as mpl
import math 

mpl.rcParams['keymap.back'] = []
mpl.rcParams['keymap.forward'] = []
mpl.rcParams['keymap.pan'] = []
mpl.rcParams['keymap.zoom'] = []
mpl.rcParams['keymap.save'] = []
mpl.rcParams['keymap.home'] = []

L1=3.8
L2=5.8
L3=7.8

step = 0

N = [
    [   # Leg 0, end effector at (18.2, -7.8, 18.2)
        (16.2, -7.8, 18.2),
        (16.2, -5.8, 18.2),
        (20.2, -5.8, 18.2),
        (20.2, -7.8, 18.2)
    ],
    [   # Leg 1, end effector at (0.0, -7.8, 25.7)
        (2.0, -5.8, 25.7),
        (2.0, -7.8, 25.7),
        (-2.0, -7.8, 25.7),
        (-2.0, -5.8, 25.7)
    ],
    [   # Leg 2, end effector at (-18.2, -7.8, 18.2)
        (-20.2, -7.8, 18.2),
        (-20.2, -5.8, 18.2),
        (-16.2, -5.8, 18.2),
        (-16.2, -7.8, 18.2)
    ],
    None,   # Index 3 (no leg)
    [   # Leg 4, end effector at (-18.2, -7.8, -18.2)
        (-16.2, -5.8, -18.2),
        (-16.2, -7.8, -18.2),
        (-20.2, -7.8, -18.2),
        (-20.2, -5.8, -18.2)
    ],
    [   # Leg 5, end effector at (0.0, -7.8, -25.7)
        (-2.0, -7.8, -25.7),
        (-2.0, -5.8, -25.7),
        (2.0, -5.8, -25.7),
        (2.0, -7.8, -25.7)
    ],
    [   # Leg 6, end effector at (18.2, -7.8, -18.2)
        (20.2, -5.8, -18.2),
        (20.2, -7.8, -18.2),
        (16.2, -7.8, -18.2),
        (16.2, -5.8, -18.2)
    ]
]

S = []
for leg in N:
    if leg is None:
        S.append(None)
    else:
        S.append(leg[::-1])

W = [
    [  # Leg 0, end effector at (18.2, -7.8, 18.2)
        (18.2, -7.8, 20.2),
        (18.2, -5.8, 20.2),
        (18.2, -5.8, 16.2),
        (18.2, -7.8, 16.2)
    ],
    [  # Leg 1, end effector at (0.0, -7.8, 25.7)
        (0.0, -5.8, 23.7),
        (0.0, -7.8, 23.7),
        (0.0, -7.8, 27.7),
        (0.0, -5.8, 27.7)
    ],
    [  # Leg 2, end effector at (-18.2, -7.8, 18.2)
        (-18.2, -7.8, 20.2),
        (-18.2, -5.8, 20.2),
        (-18.2, -5.8, 16.2),
        (-18.2, -7.8, 16.2)
    ],
    None,  # Index 3 (no leg)
    [  # Leg 4, end effector at (-18.2, -7.8, -18.2)
        (-18.2, -5.8, -20.2),
        (-18.2, -7.8, -20.2),
        (-18.2, -7.8, -16.2),
        (-18.2, -5.8, -16.2)
    ],
    [  # Leg 5, end effector at (0.0, -7.8, -25.7)
        (0.0, -7.8, -23.7),
        (0.0, -5.8, -23.7),
        (0.0, -5.8, -27.7),
        (0.0, -7.8, -27.7)
    ],
    [  # Leg 6, end effector at (18.2, -7.8, -18.2)
        (18.2, -5.8, -20.2),
        (18.2, -7.8, -20.2),
        (18.2, -7.8, -16.2),
        (18.2, -5.8, -16.2)
    ]
]

E = []
for leg in W:
    if leg is None:
        E.append(None)
    else:
        E.append(leg[::-1])

NE = [
    [   # Leg 0, end effector at (18.2, -7.8, 18.2)
        (17.7, -7.8, 18.2),
        (17.7, -5.8, 18.2),
        (18.7, -5.8, 18.2),
        (18.7, -7.8, 18.2)
    ],
    [   # Leg 1, end effector at (0.0, -7.8, 25.7)
        (0.5, -5.8, 25.7),
        (0.5, -7.8, 25.7),
        (-.5, -7.8, 25.7),
        (-.5, -5.8, 25.7)
    ],
    [   # Leg 2, end effector at (-18.2, -7.8, 18.2)
        (-18.7, -7.8, 18.2),
        (-18.7, -5.8, 18.2),
        (-17.7, -5.8, 18.2),
        (-17.7, -7.8, 18.2)
    ],
    None,   # Index 3 (no leg)
    [   # Leg 4, end effector at (-18.2, -7.8, -18.2)
        (-16.2, -5.8, -18.2),
        (-16.2, -7.8, -18.2),
        (-20.2, -7.8, -18.2),
        (-20.2, -5.8, -18.2)
    ],
    [   # Leg 5, end effector at (0.0, -7.8, -25.7)
        (-2.0, -7.8, -25.7),
        (-2.0, -5.8, -25.7),
        (2.0, -5.8, -25.7),
        (2.0, -7.8, -25.7)
    ],
    [   # Leg 6, end effector at (18.2, -7.8, -18.2)
        (20.2, -5.8, -18.2),
        (20.2, -7.8, -18.2),
        (16.2, -7.8, -18.2),
        (16.2, -5.8, -18.2)
    ]
]

NW = [
    [   # Leg 0, end effector at (18.2, -7.8, 18.2)
        (16.2, -7.8, 18.2),
        (16.2, -5.8, 18.2),
        (20.2, -5.8, 18.2),
        (20.2, -7.8, 18.2)
    ],
    [   # Leg 1, end effector at (0.0, -7.8, 25.7)
        (2.0, -5.8, 25.7),
        (2.0, -7.8, 25.7),
        (-2.0, -7.8, 25.7),
        (-2.0, -5.8, 25.7)
    ],
    [   # Leg 2, end effector at (-18.2, -7.8, 18.2)
        (-20.2, -7.8, 18.2),
        (-20.2, -5.8, 18.2),
        (-16.2, -5.8, 18.2),
        (-16.2, -7.8, 18.2)
    ],
    None,   # Index 3 (no leg)
    [   # Leg 4, end effector at (-18.2, -7.8, -18.2)
        (-18.7, -5.8, -18.2),
        (-18.7, -7.8, -18.2),
        (-17.7, -7.8, -18.2),
        (-17.7, -5.8, -18.2)
    ],
    [   # Leg 5, end effector at (0.0, -7.8, -25.7)
        (-.5, -7.8, -25.7),
        (-.5, -5.8, -25.7),
        (0.5, -5.8, -25.7),
        (0.5, -7.8, -25.7)
    ],
    [   # Leg 6, end effector at (18.2, -7.8, -18.2)
        (18.7, -5.8, -18.2),
        (18.7, -7.8, -18.2),
        (17.7, -7.8, -18.2),
        (17.7, -5.8, -18.2)
    ]
]

SE = []
for leg in NW:
    if leg is None:
        SE.append(None)
    else:
        SE.append(leg[::-1])

SW = []
for leg in NE:
    if leg is None:
        SW.append(None)
    else:
        SW.append(leg[::-1])

current_direction = "forward"
current_gait = N

def on_key(event):
    global current_direction
    if event.key == "8":
        current_direction = "north"
    elif event.key == "9":
        current_direction = "northeast"
    elif event.key == "6":
        current_direction = "east"
    elif event.key == "3":
        current_direction = "southeast"
    elif event.key == "2":
        current_direction = "south"
    elif event.key == "1":
        current_direction = "southwest"
    elif event.key == "4":
        current_direction = "west"
    elif event.key == "7":
        current_direction = "northwest"
    elif event.key == "5":
        ax.view_init(elev=0, azim=135, roll=-90)  # Top view

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig.canvas.mpl_connect("key_press_event", on_key)

def IK2D(x,y,elbow_up=False):
    d=math.sqrt(x**2+y**2)  #distance to target
    if d>(L2+L3):   #check if distance is reachable
        print("Target is out of reach")
        return None  
    cos_J3=(d**2-L2**2-L3**2)/(2*L2*L3)
    cos_J3=max(min(cos_J3,1),-1)
    phi=math.atan2(y,x)
    cos_beta=(x**2+y**2+L2**2-L3**2)/(2*L2*d)
    cos_beta=max(min(cos_beta,1),-1)
    beta=math.acos(cos_beta)
    if elbow_up:
        J3=math.degrees(math.acos(cos_J3))
        J2=math.degrees(phi-beta)
    else:
        J3=-math.degrees(math.acos(cos_J3))
        J2=math.degrees(phi+beta)
    return round(J2,2),round(J3,2)

def IK3D(x, y, z):

    # Base rotation
    J1 = math.degrees(math.atan2(z, x))

    # Horizontal distance from robot center
    horizontal = math.sqrt(x**2 + z**2)

    # Remove coxa length
    horizontal -= L1

    # Existing 2D IK
    J2, J3 = IK2D(horizontal, y)

    return J1, J2, J3

def FK3D(J1, J2, J3):

    # Coxa endpoint
    x0 = L1 * math.cos(math.radians(J1))
    y0 = 0
    z0 = L1 * math.sin(math.radians(J1))

    # Femur (measured from the coxa)
    r1 = L2 * math.cos(math.radians(J2))
    y1 = L2 * math.sin(math.radians(J2))

    # Tibia (measured from the coxa)
    r2 = L2 * math.cos(math.radians(J2)) + L3 * math.cos(math.radians(J2 + J3))
    y2 = L2 * math.sin(math.radians(J2)) + L3 * math.sin(math.radians(J2 + J3))

    # Rotate into world coordinates
    x1 = x0 + r1 * math.cos(math.radians(J1))
    z1 = z0 + r1 * math.sin(math.radians(J1))

    x2 = x0 + r2 * math.cos(math.radians(J1))
    z2 = z0 + r2 * math.sin(math.radians(J1))

    return x0, y0, z0, x1, y1, z1, x2, y2, z2

def draw_leg(mx, my, mz, target=None):
    
    # if mz > 0:  # all legs parallel
    #     J1 = 90
    # else:
    #     J1 = -90

    J1 = math.degrees(math.atan2(mz, mx))   # perpendicular
    x0, y0, z0, x1, y1, z1, x2, y2, z2 = FK3D(J1, -15, 90)

    # ax.scatter(mx, my, mz, color="black")
    ax.plot(
        [mx, mx+x0, mx+x1, mx+x2],
        [my, my+y0, my+y1, my+y2],
        [mz, mz+z0, mz+z1, mz+z2],
        color="black"
    )
    ax.scatter(
        [mx, mx+x0, mx+x1, mx+x2],
        [my, my+y0, my+y1, my+y2],
        [mz, mz+z0, mz+z1, mz+z2],
        color="black"
    )
    
def draw_body(step):

    ax.text2D(
        0.5, 1.1,
        "All the numbers on the numpad correspond to a direction.\n"
        "8=go N, 9=go NE, 6=go E, 3=go SE\n"
        "2=go S, 1=go SW, 4=go W, 7=go NW\n"
        "5=home view",
        transform=ax.transAxes,
        ha="center",
        va="top"
    )

    angles = [22.5, 67.5, 112.5, 157.5,
              202.5, 247.5, 292.5, 337.5]

    vertices = []

    R = 17.4

    for angle in angles:
        angle = math.radians(angle)

        x = R * math.cos(angle)
        y = 0
        z = R * math.sin(angle)

        vertices.append((x, y, z))

    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    z = [v[2] for v in vertices]

    x.append(vertices[0][0])
    y.append(vertices[0][1])
    z.append(vertices[0][2])

    ax.plot(x, y, z, color="black")
    ax.scatter(x, y, z, color="black")

    for i in range(len(x)-1):

        mx = (x[i]+x[i+1])/2
        my = (y[i]+y[i+1])/2
        mz = (z[i]+z[i+1])/2

        if abs(mz) < 1e-6:
            continue

        # print(f"Leg {i}: ({mx:.5f}, {my:.5f}, {mz:.5f})")

        if i in(0, 1, 2, 4, 5, 6):
            target_x, target_y, target_z = current_gait[i][step]
        else:
            draw_leg(mx, my, mz)
            continue

        local_x = target_x - mx
        local_y = target_y - my
        local_z = target_z - mz
        # print(f"Leg {i}")
        # print(f"Target = ({target_x}, {target_y}, {target_z})")
        # print(f"Local  = ({local_x:.2f}, {local_y:.2f}, {local_z:.2f})")
        J1, J2, J3 = IK3D(local_x, local_y, local_z)
        x0, y0, z0, x1, y1, z1, x2, y2, z2 = FK3D(J1, J2, J3)

        ax.plot(
            [mx, mx+x0, mx+x1, mx+x2],
            [my, my+y0, my+y1, my+y2],
            [mz, mz+z0, mz+z1, mz+z2],
            color="black"
        )
        ax.scatter(
            [mx, mx+x0, mx+x1, mx+x2],
            [my, my+y0, my+y1, my+y2],
            [mz, mz+z0, mz+z1, mz+z2],
            color="black"
        )        

while True:
    if current_direction == "north":
        current_gait = N
    elif current_direction == "northeast":
        current_gait = NE
    elif current_direction == "east":
        current_gait = E
    elif current_direction == "southeast":
        current_gait = SE
    elif current_direction == "south":
        current_gait = S
    elif current_direction == "southwest":
        current_gait = SW
    elif current_direction == "west":
        current_gait = W
    elif current_direction == "northwest":
        current_gait = NW
    ax.clear()
    ax.set_xlim(-35, 35)
    ax.set_ylim(-35, 35)
    ax.set_zlim(-35, 35)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    draw_body(step)    
    plt.pause(.2)
    step = (step + 1) % len(current_gait[0])  # Loop through the steps