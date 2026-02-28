from mapping.grid_mapper import GridMapper

mapper = GridMapper()
mapper.update_robot_pose(0.5, 0.0, 0)
mapper.update_obstacle(0.5)

print("Mapping test passed!")