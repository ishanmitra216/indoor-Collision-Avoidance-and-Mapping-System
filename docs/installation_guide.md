# Installation Guide

## 1. Flash Jetson Nano

Install JetPack 4.6 (Ubuntu 18.04)

## 2. Install ROS Melodic

sudo apt install ros-melodic-desktop-full

## 3. Clone Project

git clone <repo>

## 4. Run Setup

bash setup.sh

## 5. Launch System

roslaunch jetbot_navigation full_system.launch

## 6. Start API

uvicorn main:app --reload