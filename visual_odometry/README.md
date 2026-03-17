# Visual Odometry Module

This module estimates camera motion from monocular video using ORB features,
feature matching, essential-matrix pose recovery, and trajectory accumulation.

## Purpose

- Detect and match visual features between consecutive frames.
- Estimate relative camera motion `(R, t)`.
- Accumulate global pose over time.
- Visualize and export trajectory data.

## File Components

### vo_main.py

Main runtime pipeline.

What it does:
- Opens camera stream (`cv2.VideoCapture(0)`).
- Initializes all VO components (`CameraModel`, `ORBDetector`,
	`FeatureMatcher`, `PoseEstimator`, `Trajectory`).
- For each frame:
	- Converts to grayscale.
	- Detects ORB keypoints/descriptors.
	- Matches current descriptors with previous frame descriptors.
	- Estimates relative motion if enough matches are available.
	- Builds a 4x4 transform and updates global pose.
	- Stores trajectory point.
	- Draws trajectory and shows camera preview.
- Stops on `Esc` key.

### camera_model.py

Camera intrinsics container.

Contains class `CameraModel`:
- `focal` length value (`718.8560`).
- Principal point `(cx, cy)` = `(320, 240)`.
- `get_matrix()` returns 3x3 intrinsic matrix.

Role:
- Provides intrinsics used by essential matrix and pose recovery.

### orb_detector.py

Feature extraction component.

Contains class `ORBDetector`:
- Configures ORB with `nfeatures` (default `2000`).
- `detect(frame)` returns `(keypoints, descriptors)`.

Role:
- Produces robust, fast visual features for matching.

### feature_matcher.py

Descriptor matching component.

Contains class `FeatureMatcher`:
- Uses brute-force Hamming matcher (`BFMatcher`, cross-check enabled).
- `match(des1, des2)`:
	- Returns empty list if descriptors are missing.
	- Matches and sorts by match distance.
	- Keeps top 200 matches.

Role:
- Connects feature tracks across consecutive frames.

### pose_estimator.py

Relative-pose estimation component.

Contains class `PoseEstimator`:
- Uses matched keypoint coordinates to compute:
	- Essential matrix via `cv2.findEssentialMat` (RANSAC).
	- Relative rotation and translation via `cv2.recoverPose`.
- Returns `(R, t)`.

Role:
- Converts feature correspondences into camera motion estimate.

### trajectory.py

Trajectory state container.

Contains class `Trajectory`:
- Stores list of 2D positions.
- `update(pose)` extracts `(x, y)` from pose matrix (`x = pose[0,3]`,
	`y = pose[2,3]`).
- `get_positions()` returns NumPy array of tracked positions.

Role:
- Maintains accumulated path for plotting and export.

## Utilities (`utils/`)

### utils/visualization.py

Trajectory plotting helper.

Contains:
- Global image canvas `traj_img`.
- `draw_trajectory(positions)`:
	- Draws each trajectory point in green.
	- Shows the trajectory window via OpenCV.

### utils/math_utils.py

Numeric helper function:
- `normalize_points(points)` standardizes points by mean and standard
	deviation.

### utils/file_utils.py

File/output helpers:
- `create_dir(path)` creates directory if missing.
- `save_trajectory(path, positions)` writes trajectory points to text file.

## Typical VO Flow

1. Capture current camera frame.
2. Detect ORB keypoints/descriptors.
3. Match with previous frame descriptors.
4. Estimate relative pose `(R, t)` from matched points.
5. Update global pose matrix.
6. Append trajectory point and visualize.

## Notes and Limitations

- This is monocular VO, so absolute scale can drift.
- Reliability depends on texture, lighting, and motion blur.
- Intrinsic camera values should be calibrated for your actual camera.
- Current pipeline uses simple sequential matching and may need outlier
	filtering/tuning for challenging scenes.

