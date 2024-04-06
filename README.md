# RGB Marker Detection
ArUco marker for pose estimation, camera calibration, and augmented reality to track object movement.

### What is ArUco Markers?
ArUco markers are square or rectangular patterns of black and white squares used in computer vision for object tracking and pose estimation.

### What is Open Source package can be used for this marker?
OpenCV: Open Source Computer Vision Library 
### How many ArUco Markers pattern provided in OpenCV?
The aruco module in OpenCV has a total of 25 predefined dictionaries of markers. 
All the markers in a dictionary contain the same number of blocks or bits(4×4, 5×5, 6×6 or 7×7), and each dictionary contains a fixed number of markers(50, 100, 250 or 1000).

### Marker patterns available on the market

| Name      | Shape   | Color      | Encoding      | Marker                                                                                                    |
|-----------|---------|------------|---------------|-----------------------------------------------------------------------------------------------------------|
| AprilTag  | Square  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/2a576aa2-fb1e-48e9-ae85-2be51e104a28) | 
| ARTag     | Square  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/7a753a51-4c3c-4375-9366-97f885298cdd) | 
| ARToolKit | Square  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/ebe39f1b-4230-4ab7-86da-55bfbb7f32f8) | 
| ArUco     | Square  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/776deb7d-a9be-4af5-b33b-5f8bb5211d83) | 
| BullsEye  | Circle  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/98b9a514-a909-44ef-b881-4258c7c5734a) | 
| CATag     | Square  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/6421dc40-1b36-4a90-8b2f-2d1794e7a904) | 
| CCC       | Circle  | Monochrome | Not Supported | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/ea6e29ef-d433-4e9a-8a0e-ceaaebd61d46) |
| CCTag     | Circle  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/3530e90c-8d63-4b6b-8018-017c69b3a6e4) | 
| ChromaTag | Square  | Multicolor | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/560e0147-9adb-4b7c-8ab4-6c8b58c255a4) | 
| FourierTag| Circle  | Grayscale  | Freq. Spectrum| ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/de0f5c9c-925a-4fca-9c2c-0c3932c95677) | 
| Multi-ring| Circle  | Multicolor | Not Supported | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/f610b9e6-abfb-49da-ab1e-411bb1149a5d) | 
| Pi-Tag    | Square  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/e48d2d86-4639-44dc-a53e-bcf57fab1435) |
| RuneTag   | Circle  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/5f0537d1-5a94-4978-9632-d09bd13ebb55) |
| STag      | Square  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/db0fce55-62cd-492e-bb3b-79334ffcc5c8) |
| WhyCode   | Circle  | Monochrome | Topological   | ![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/18f0576f-9459-4fb2-ba4b-140ff52676ca) | 

### What are the requirments for the markers?

1. **Distinct Pattern**: ArUco markers must have a unique black and white pattern.
2. **Contrast**: The pattern should have clear contrast for reliable detection.
3. **Size**: Marker size should suit the application and distance from the camera.
4. **Resolution**: The pattern resolution should enable accurate detection.
5. **Orientation**: Markers should be detectable from any orientation.

### What are the IDs of markers detected? 
There are 5 samples of ArUco markers was printed in 3D cube shape, where each face has a marker pattern and one face is blank white. 

<img src="https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/01de48d7-d724-49cb-9e40-74a03832c07c" alt="img" width="400">

### What is the camera used for this code? 
Intel(R) RealSense(TM) Depth Camera 435i

<img src="https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/ae5feb8e-a463-4ae6-9474-654d97657a61" alt="Img" width="200">

### ArUco Marker detection output:

![image](https://github.com/Arwa-Fawzy/AruCoVision/assets/101527083/f32739e3-0e60-4e60-a1e2-fd511242e632)

### ArUco Marker Pose estimation output:


<img src="https://github.com/Arwa-Fawzy/RGB-Marker-Detection/assets/101527083/e474ff01-df5b-4269-bae9-7b83e4536ed9" alt="Img" width="200">



