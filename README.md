# SmartAttendance

The objective of this project is to process live video-stream of students entering their classroom and generate the list of students attending the class.
The system is coded in Python 3.8 using OpenCv, Tkinter and Numpy libraries.
The file in the directory are:
* main.py : This is the main  script of the project.
                    It implements the GUI of the project and calls functions from the modules package developed.

* Cascade/haarcascade_frontalface_default.xml : This file is taken from the OpenCV library and contains trained configurations of Voila-Jones Algorithm for detecting faces.

* student_detail.py : This file contains the function which store the student's information in MySQL database

* train.py : This file train the face dataset collected in student_detail.py, trained the model and store the outcome into classifier.xml file.

* facial_recognition.py : This file recognize the student through camera and store its information into attendance.csv

* attendace.py : This file contains the function which allow user to edit or save it in separate file
   

## Getting Started
### Prerequisites

The system needs Python 3.8 installed along with OpenCV libraries.

### Installing

The steps to install OpenCV with the extra module can be found [here](https://github.com/opencv/opencv_contrib).
The project also requires [Tkinter](https://docs.python.org/3/library/tk.html) and [Numpy](http://www.numpy.org/).


## Built With

* [OpenCV](https://docs.opencv.org/master/) - Implementation of Algorithms
* [Tkinter](https://docs.python.org/3/library/tk.html) - GUI Implementation
* [Numpy](http://www.numpy.org/) - Used to manage computaions.
* [MySQL](https://dev.mysql.com/doc/) - Used to store student detail.


## Authors

- [Ananta Pandey](https://github.com/ananta15)
- [Akshat Mishra](https://github.com/akshat-20)
- [Anshika Gupta]()
