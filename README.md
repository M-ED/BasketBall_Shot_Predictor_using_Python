
# Basketball Shot Predictor using OpenCV, CvZone, and Python

Basketball shot predictor using computer vision techniques to predict whether a basketball shot will result in a basket by tracking the ball's trajectory.







## Prerequisites
- Python 3.9.0 or higher 
- OpenCV
- CvZone
- NumPy
- Math

## Installation

1. Clone the repository:

```bash
  git clone https://github.com/M-ED/BasketBall_Shot_Predictor_using_Python.git
```

2. Create virtual environment using following commands:
```bash
  conda create -n projects_CV python==3.9.0
  conda activate projects_CV
```

3. Install the necessary libraries in requirements file
```bash
   pip install -r requirements.txt
```

4. Run the script
```bash
  python main.py
```


## Usage

1. Place your video file in the `Videos/` directory.

2. Run the script:
```bash
  python basketball_shot_predictor.py
```

3. The system will display the video with the ball's trajectory and the prediction of whether it will go into the basket.
    
## Features

Following are the key features:
- Detects and tracks the basketball in the video.
- Predicts the trajectory of the ball usinf polynomial regression.
- Displays whether the ball will make it into the basket or miss.




## Acknowledgements

- OpenCV: [https://opencv.org/](https://opencv.org/)
- Scikit-Learn: [hhttps://scikit-learn.org/stable//](https://github.com/google-ai-edge/mediapipe)



## License

[MIT](https://choosealicense.com/licenses/mit/)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Author

- [@mohtadia_naqvi](https://github.com/M-ED)

