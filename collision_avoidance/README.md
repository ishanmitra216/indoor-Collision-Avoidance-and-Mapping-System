# Collision Avoidance Module

This module provides a lightweight obstacle-avoidance pipeline for JetBot.
It combines vision-based obstacle cues, motion-based distance estimation,
safety timeout checks, and low-level motion execution.

## Folder Components

### avoidance_controller.py

Contains `AvoidanceController`, the decision layer.

Responsibilities:
- Stores a configurable `safe_distance` threshold (default `0.5`).
- Chooses a high-level action with `decide(obstacle_detected, distance)`.

Decision behavior:
- If no obstacle is detected: returns `FORWARD`.
- If obstacle is detected and distance is below threshold: returns `STOP`.
- If obstacle is detected but distance is not critically close: returns `TURN_LEFT`.

### obstacle_detector.py

Contains `ObstacleDetector`, the perception layer for obstacle presence.

Responsibilities:
- Converts camera frame to grayscale.
- Focuses only on the center region of the image.
- Computes two cues:
	- Mean brightness (`mean_intensity`)
	- Edge density (`edge_count`) using Canny edges
- Returns tuple:
	- `(obstacle_detected, mean_intensity, edge_count)`

Detection logic:
- Obstacle is flagged if center brightness is too low
	(`mean_intensity < intensity_threshold`, default `50`).
- Obstacle is also flagged if edge count is high
	(`edge_count > edge_threshold`, default `1500`).

### depth_estimator.py

Contains `DepthEstimator`, a simple distance proxy estimator using optical flow.

Responsibilities:
- Tracks previous grayscale frame.
- Computes dense optical flow (Farneback) between frames.
- Converts flow vectors to magnitude and averages motion strength.
- Estimates distance with inverse relation: `distance = 1.0 / avg_motion`.

Behavior notes:
- First frame returns `None` because there is no previous frame yet.
- If motion is zero, returns a large default distance (`10.0`).
- This is an approximation, not metric depth from a depth sensor.

### safety_monitor.py

Contains `SafetyMonitor`, a watchdog for fail-safe behavior.

Responsibilities:
- Tracks time of last positive detection.
- Updates timestamp with `update_detection(detected)` when detection is true.
- Triggers emergency with `check_emergency()` if elapsed time exceeds timeout
	(default `2.0` seconds).

Use case:
- If sensing/updates stall or become unreliable, the caller can stop the robot
	when emergency condition is true.

### motion_planner.py

Contains `MotionPlanner`, the actuator execution layer using `jetbot.Robot`.

Responsibilities:
- Creates a `Robot` instance.
- Executes string commands via `execute(command)`:
	- `FORWARD` -> move forward at speed `0.3`
	- `STOP` -> stop motors
	- `TURN_LEFT` -> turn left at speed `0.3`, short delay, then stop
	- `TURN_RIGHT` -> turn right at speed `0.3`, short delay, then stop

## Typical Pipeline Flow

1. Capture frame from camera.
2. Run `ObstacleDetector.detect(frame)`.
3. Run `DepthEstimator.estimate(frame)` for distance proxy.
4. Run `AvoidanceController.decide(obstacle_detected, distance)`.
5. Execute returned command with `MotionPlanner.execute(command)`.
6. Update/check fail-safe state with `SafetyMonitor`.

## Notes and Limitations

- The current controller favors `TURN_LEFT` as default avoidance turn.
- Distance from optical flow depends on camera motion and scene texture.
- Thresholds in detector are heuristic and should be tuned per environment.
- `MotionPlanner` requires JetBot hardware/software (`jetbot` package).
