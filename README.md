# Windows-Forms-Photoplethysmogram-for-PPG-data-acquisition
This application is intend to use for creating a database for machine learning projects. Subjects physical data and blood pressure, measured from external device are entered. Measurement system that is part of this solution provide PPG signals of observed person in real time from hardware. This hardware system is based on embedded device for sensing and Python source code for data processing. It is non invasive light reflective method with two wavelengths.
## Hardware
![Hardware](/Pictures/Hardware.jpg)

Hardware is consist of two development boards from MikroElektronika.
[Hart rate click](https://www.mikroe.com/heart-rate-click) have MAX30100 pulse oximeter integrated circuit.
[PIC clicker](https://www.mikroe.com/clicker-pic18fj) is board that have microcontroller, micro BUS and USB port.
Firmware SPO2.hex must be downloaded to PIC clicker. It’s possible thru integrated Bootloader or with mikroProg for PIC programmer.
It’s send values of reflected Infra-Red and Red lights via USB that is defined like virtual COM-port. Frequency of acquisition is 50 Hz.
This Firmware is develop using two libraries: “Virtual COM Port Demo” and “Heart rate click” form MIKROE libstock site.

## Windows Forms Application
![WFA](Pictures/Aplikacija.jpg)

Windows Forms Application named “PPG Acquisition System” collects: entered, calculated, and measured data to one textual file with CSV format. Each subject should have own file that bears the name of that subject ID. Entered values are: ID, Gender, Age, Height, Weight, Systolic Pressure, Diastolic Pressure, and Heart Rate. Calculated values from PPG signal are: Heart Rate HR, Blood Saturation SPO2, and Perfusion Index PI. Measured data are PPG signal from subjects three fingers, measured with 16bit precision and two wavelength with reflected method. 
