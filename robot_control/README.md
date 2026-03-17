# Robot Control Module

This module provides the motion-control stack for JetBot, from high-level
movement commands down to direct motor actuation.

## Purpose

- Wrap JetBot hardware control in reusable Python classes.
- Convert linear/angular velocity commands into left-right wheel motor values.
- Track robot runtime state (pose, velocity, status).
- Expose high-level movement primitives such as timed forward motion and turns.

## File Components

### jetbot_interface.py

Low-level hardware interface around `jetbot.Robot`.

Contains class `JetBotInterface`:
- Creates `Robot()` instance.
- `set_motors(left_speed, right_speed)`: directly sets motor values.
- Convenience methods:
	- `forward(speed)`
	- `backward(speed)`
	- `left(speed)`
	- `right(speed)`
	- `stop()`

Role:
- Thin adapter that isolates direct JetBot API calls.

### motor_controller.py

Velocity-to-wheel conversion layer.

Contains class `MotorController`:
- Owns `JetBotInterface`.
- Uses differential-drive kinematics with configurable `wheel_base`
	(default `0.1`).

Main method:
- `set_velocity(linear, angular)`:
	- Computes wheel commands:
		- `v_l = linear - (angular * wheel_base / 2)`
		- `v_r = linear + (angular * wheel_base / 2)`
	- Clamps both wheel values to `[-1.0, 1.0]`.
	- Sends result to motors via interface.
- `stop()`: stops motors.

Role:
- Converts robot-centric motion commands into actuator-ready wheel speeds.

### robot_state.py

In-memory runtime state container.

Contains class `RobotState`:
- Stores pose: `x`, `y`, `theta`.
- Stores velocity: `linear_velocity`, `angular_velocity`.
- Stores status string (default `IDLE`).

Methods:
- `update_pose(x, y, theta)`
- `update_velocity(linear, angular)`
- `update_status(status)`
- `get_state()` returns dictionary for logging/API/UI.

Role:
- Single source of current robot control-state snapshot.

### velocity_controller.py

Mid-level motion controller combining motor output with state updates.

Contains class `VelocityController`:
- Owns `MotorController` and `RobotState`.
- Exposes directional velocity commands:
	- `move_forward(speed=0.3)`
	- `move_backward(speed=0.3)`
	- `rotate_left(angular_speed=1.0)`
	- `rotate_right(angular_speed=1.0)`
	- `stop()`
- `get_robot_state()` returns current tracked state.

Role:
- Primary control API for setting motion while keeping state synchronized.

### movement_commands.py

High-level action primitives for timed maneuvers.

Contains class `MovementCommands`:
- Owns `VelocityController`.
- Provides macro-style actions:
	- `go_forward_distance(speed, duration)`
	- `turn_left_angle(angular_speed, duration)`
	- `turn_right_angle(angular_speed, duration)`
	- `emergency_stop()`
	- `get_state()`

Behavior:
- Executes command, waits with `time.sleep(duration)`, then stops.

Role:
- Simplifies sequencing for basic autonomous maneuvers.

## Control Hierarchy

1. `MovementCommands` (high-level timed actions)
2. `VelocityController` (semantic move/rotate commands)
3. `MotorController` (linear/angular to wheel-speed conversion)
4. `JetBotInterface` (direct motor actuation)
5. JetBot hardware

State is tracked in parallel by `RobotState` and surfaced via
`get_robot_state()` / `get_state()`.

## Typical Usage Flow

1. Create `MovementCommands()`.
2. Call forward/turn command with speed and duration.
3. Module sends velocity commands to motors.
4. Module updates status and velocity in `RobotState`.
5. Read current state dictionary when needed.

## Notes

- Speed values are clamped at motor controller level to protect actuator range.
- Timed commands approximate distance/angle and depend on calibration,
	battery level, and surface friction.
- This module requires JetBot runtime and hardware support for full execution.
