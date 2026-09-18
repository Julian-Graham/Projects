# Mini Project 2 – Automated Garage Door

## Overview

This project is an automated garage door system built using a Raspberry Pi.
The system uses RFID authentication to control access, IR sensors to detect
the door's position, and a continuous-rotation servo to operate the door.

## Objective

The goal was to design and implement a functional automated garage door
that could open using an authorized RFID tag, detect its fully open and
closed positions, and automatically close after a set amount of time.

## Hardware

- Raspberry Pi
- RFID module
- RFID card/fob
- FT90R continuous-rotation servo
- 2× IR sensors
- Blue LED
- Breadboard
- Jumper wires
- Paracord
- 3D-printed garage door/mechanical components

## How It Works

### 1. RFID Authentication
When a valid RFID card or fob is presented, the Raspberry Pi
activates the servo and begins opening the garage door.

### 2. Door Movement
The FT90R continuous-rotation servo moves the garage door through
a paracord-based pulley mechanism.

### 3. Position Detection

Two IR sensors monitor the position of the garage door. When the top IR sensor is triggered, the servo stops, leaving the door fully open. The bottom IR sensor performs the same function when the door is closing. When the door is fully open, an LED turns on to notify the user that the door is open. The IR sensor and LED setup is shown in `LED and IR.jpg`.

### 4. Automatic Closing
After the door opens, a timer begins. The system continuously checks whether the RFID tag is presented again or whether the programmed timeout has been reached. Scanning the RFID tag again closes the door immediately, while the door closes automatically when the timeout expires.

## Programming

The program uses Python's `time.time()` function to track how long the garage remains open. The system continuously checks whether the RFID tag is presented again or whether the timeout has expired.

## Mechanical Design

The garage structure was constructed using 3D-printed components.
A paracord-based pulley mechanism connects the servo to the door.

## Challenges / Engineering Decisions

One of the main challenges was integrating the RFID functionality with
the `time.time()` timer. When the two pieces of code were initially
combined, the program produced several errors and would sometimes
crash.

I found that the RFID functionality needed to be organized into
separate function definitions and controlled using `if` statements.
I also discovered that the placement of `time.time()` within the
program affected its behavior. Placing it directly after the RFID
code caused the program to crash, so I had to reorganize the program's
logic and control flow to allow both the RFID input and timer to
operate correctly.
