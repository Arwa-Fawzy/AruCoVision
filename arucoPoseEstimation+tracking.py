import numpy as np
import cv2
import pyrealsense2 as rs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Camera calibration parameters (replace with your actual calibration results)
camera_matrix = np.array([[387.921, 0,  322.792],
                          [0, 387.921, 237.912],
                          [0, 0, 1]])

dist_coeffs = np.array([0.0366562741, -0.153342145, -0.000307462615, -0.000078917106, 0.215865749])

# Initialize lists to store data for plotting
time_values = []
z_values_cm = []

# Function to display ArUco markers and print 3D coordinates
def aruco_display(corners, ids, rejected, image, depth_frame, depth_scale):
    if len(corners) > 0:
        ids = ids.flatten()
        for (markerCorner, markerID) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
            cv2.putText(image, "Depth: {:.2f} cm".format(depth_frame.get_distance(cX, cY) * depth_scale * 100), (topLeft[0], topLeft[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Print 3D coordinates
            depth = depth_frame.get_distance(cX, cY) * depth_scale
            print("[Inference] ArUco marker ID: {}, Depth: {:.2f} meters".format(markerID, depth*100))
            time_values.append(time.time())  # Record time
            z_values_cm.append(depth * 100)  # Record z-value in cm

    return image

# Create the RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)

# Initializing ArUco detector object
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
aruco_params = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

# Plot initialization for real-time z-value versus time
fig, ax = plt.subplots(figsize=(8, 6))
plt.ion()
plt.xlabel('Time')
plt.ylabel('Z-value (cm)')
plt.title('Z-value versus Time')

try:
    while True:
        # Wait for the next set of frames
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()
        if not color_frame or not depth_frame:
            continue

        # Get depth scale
        depth_sensor = pipeline.get_active_profile().get_device().first_depth_sensor()
        depth_scale = depth_sensor.get_depth_scale()
        
        # Converting color frame to numpy array
        color_image = np.asanyarray(color_frame.get_data())

        # Undistort the color image
        color_image_undistorted = cv2.undistort(color_image, camera_matrix, dist_coeffs)

        # Detect ArUco markers
        markerCorners, markerIds, _ = detector.detectMarkers(color_image_undistorted)

        # Displaying the detected markers and printing 3D coordinates
        detected_markers = aruco_display(markerCorners, markerIds, [], color_image_undistorted, depth_frame, depth_scale)
        cv2.imshow("ArUco Marker Detection", detected_markers)

        # Plot z-values versus time
        plt.plot(time_values, z_values_cm)
        plt.xlabel('Time')
        plt.ylabel('Z-value')
        plt.title('Z-value versus Time')
        plt.grid(True)
        plt.draw()
        plt.pause(0.01)
        

        # Checking for key press to exit
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        
finally:
    pipeline.stop()
    cv2.destroyAllWindows()
