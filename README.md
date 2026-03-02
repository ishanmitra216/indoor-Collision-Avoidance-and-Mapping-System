# <span style="color:#2E86C1;">Indoor Collision Avoidance and Mapping System</span>  
## <span style="color:#8E44AD;">Visual Odometry-Based (JetBot V2.0)</span>

---

## <span style="color:#117A65;">Authors</span>

<span style="color:#1F618D;"><strong>Ishan Mitra</strong></span>  
AMC Engineering College, VTU  
(Visvesvaraya Technological University)

<span style="color:#1F618D;"><strong>GopiMohan Mukherjee</strong></span>  
AMC Engineering College, VTU  
(Visvesvaraya Technological University)

<span style="color:#7D3C98;"><strong>Srikanth Nanda</strong></span>  
Hochschule Emden/Leer  
University of Applied Sciences

---

# <span style="color:#148F77;">1. Project Purpose</span>

Design and develop a <span style="color:#C0392B;"><strong>real-time indoor collision avoidance and mapping system</strong></span> using:

- <span style="color:#2E86C1;">Monocular Camera</span>  
- <span style="color:#8E44AD;">Visual Odometry (VO)</span>  
- <span style="color:#D68910;">JetBot V2.0 (Jetson Nano platform)</span>  
- <span style="color:#117A65;">ROS (Robot Operating System)</span>  

## <span style="color:#AF601A;">Core Objectives</span>

- <span style="color:#1ABC9C;">Scan indoor environments in real time</span>  
- <span style="color:#5B2C6F;">Estimate robot motion using Visual Odometry</span>  
- <span style="color:#2874A6;">Generate a 2D top-view occupancy map</span>  
- <span style="color:#C0392B;">Detect frontal obstacles</span>  
- <span style="color:#CA6F1E;">Enable real-time collision avoidance</span>  
- <span style="color:#196F3D;">Provide safe indoor navigation without GPS</span>  

---

# <span style="color:#2E86C1;">2. Target Environments (GPS-Denied)</span>

- Hospitals  
- Shopping malls  
- Airports  
- Warehouses  
- Smart homes  
- Assistive navigation systems  

---

# <span style="color:#8E44AD;">3. System Overview</span>

Indoor localization is achieved using:

- <span style="color:#2E86C1;">Monocular Camera</span>  
- <span style="color:#8E44AD;">Visual Odometry algorithms</span>  
- <span style="color:#117A65;">ROS-based mapping</span>  

The system performs three primary tasks:

## <span style="color:#148F77;">Step 1: Visual Scanning</span>

- Continuous image frame capture  

## <span style="color:#6C3483;">Step 2: Motion Estimation (Visual Odometry)</span>

- ORB Feature Extraction  
- Feature Matching (BFMatcher / FLANN)  
- Essential Matrix Estimation  
- Pose Recovery  

## <span style="color:#C0392B;">Step 3: Mapping + Collision Avoidance</span>

- 2D occupancy grid map generation  
- Frontal obstacle detection  
- Reactive avoidance control  

---

# <span style="color:#D68910;">4. Working Principle</span>

```
Input      → Camera Frames  
Processing → Visual Odometry + Mapping  
Output     → 2D Map + Robot Pose + Collision Avoidance  
```

---

# <span style="color:#7D3C98;">5. Algorithms Used</span>

## <span style="color:#2E86C1;">5.1 Visual Odometry</span>

- ORB Feature Detection  
- Feature Matching  
- Essential Matrix Computation  
- Relative Pose Estimation  

## <span style="color:#117A65;">5.2 Mapping</span>

- Occupancy Grid Mapping  
- Free / Occupied / Unknown cell classification  

## <span style="color:#C0392B;">5.3 Collision Avoidance</span>

- Motion-based depth approximation  
- Threshold-based obstacle detection  
- Differential drive motion control  

---

# <span style="color:#148F77;">6. Hardware Constraints (JetBot V2.0)</span>

## <span style="color:#2E86C1;">Processing Unit</span>

Jetson Nano  
- Quad-core ARM CPU  
- 4GB RAM  
- 128-core Maxwell GPU  
- 32GB microSD storage  

## <span style="color:#8E44AD;">Sensor</span>

- Monocular Raspberry Pi Camera V2  

## <span style="color:#AF601A;">Mobility</span>

- 2 DC motors  
- Integrated motor driver  
- Differential drive system  

## <span style="color:#196F3D;">Power Supply</span>

- 5V battery pack  

---

# <span style="color:#2E86C1;">7. Software Requirements</span>

## <span style="color:#148F77;">Operating System</span>

Ubuntu 18.04 (Jetson Nano compatible)

## <span style="color:#8E44AD;">Middleware</span>

ROS Melodic

## <span style="color:#117A65;">Libraries</span>

- OpenCV  
- NumPy  
- cv_bridge  
- tf  
- nav_msgs  

## <span style="color:#AF601A;">Visualization</span>

- RViz  
- Gazebo (Simulation)  

---

# <span style="color:#7D3C98;">8. Expected Output</span>

## <span style="color:#148F77;">Top View</span>

- 2D occupancy grid map  
- Free space representation  
- Obstacle representation  
- Robot pose visualization  

## <span style="color:#C0392B;">Front View</span>

- Distance estimation of obstacles ahead  
- Real-time collision warning  

## <span style="color:#2E86C1;">Localization</span>

- Continuous pose estimation  
- Trajectory plotting  

---

# <span style="color:#AF601A;">9. Applications</span>

- Indoor autonomous robots  
- Assistive mobility systems  
- Smart building navigation  
- Warehouse automation  
- Educational robotics
