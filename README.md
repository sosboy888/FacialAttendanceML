# FacialAttendanceML

A real-time face-recognition attendance system in Python. It detects faces in a webcam feed, identifies each person with a classifier trained on face embeddings, and marks them present in a SQLite database. A Tkinter GUI shows the live feed and lets you capture photos for training.



## How it works

```
webcam frame ─► face detection ─► face embedding ─► SVM classifier ─► person ID ─► SQLite attendance
                (dlib CNN)        (dlib, 128-d)     (scikit-learn)                  (Personnel.db)
```

1. **Collect:** the GUI's *Click Photo* button saves webcam frames to `clickedImages/`.
2. **Organise:** sort the photos into one folder per person, named by their numeric ID (`DataSet/1/`, `DataSet/2/`, ...).
3. **Train:** `DataExtract.py` computes a face embedding for every photo that contains exactly one face and fits an SVM (`sklearn.svm.SVC`) on them. The model is saved to `trainedData.sos`.
4. **Recognise:** for each webcam frame, faces are detected with dlib's CNN detector, embedded, and classified. A box and the person's name are drawn on the frame.
5. **Mark attendance:** the first time a person is recognised in a session, they are marked `Present` in `Personnel.db`.

Only the lightweight SVM is trained on your photos. Face detection and the embeddings come from pretrained dlib models, accessed through the [`face_recognition`](https://github.com/ageitgey/face_recognition) library, so adding people means retraining a small classifier, not a neural network.

## Tech stack

Python, OpenCV, dlib / `face_recognition`, scikit-learn, Tkinter + Pillow, SQLite, joblib.

## Setup

```bash
git clone https://github.com/sosboy888/FacialAttendanceML.git
cd FacialAttendanceML
pip install face_recognition opencv-python scikit-learn joblib pillow docopt
mkdir clickedImages
```

- `face_recognition` depends on **dlib**. The CNN face detector is slow on CPU, so a **CUDA-enabled dlib build** is strongly recommended (`Main.py` prints `dlib.DLIB_USE_CUDA` at startup). Developed on a GTX 1060.
- Tkinter ships with the standard Python installers on Windows and macOS.

## Usage

```bash
python DataExtract.py   # train the classifier from DataSet/ (edit the dataset path in the last line first)
python GUI.py           # live recognition + "Click Photo" button
```

The `*.sos` files (`count.sos`, `imagesCount.sos`, `trainedData.sos`) are joblib files. `count.sos` holds the number of registered people and `imagesCount.sos` is the photo counter; both must exist before the scripts start.

## Database

`Personnel.db` (SQLite) is expected to contain:

| Table | Columns used |
|---|---|
| `students` | `id`, `Name` |
| `presentee28` | `id`, `presentee` |

`students.id` must match the folder names in `DataSet/`. IDs should run `1..n`, because the once-per-session check indexes people by `id - 1`.

## Project structure

| File | Role |
|---|---|
| `GUI.py` | Tkinter app: live video, *Click Photo*, saves the photo counter on exit |
| `Main.py` | Per-frame pipeline: recognise faces, draw boxes and names, mark attendance once per run |
| `DataRecognize.py` | `Recognizer` class: face detection, embedding and SVM prediction |
| `DataExtract.py` | Builds training data from `DataSet/` and trains the SVM |
| `AttendanceMarker.py` | SQLite helpers: `markAttendance`, `getName` |
| `Registration.py` | Console registration helper (work in progress, see below) |
| `Personnel.db` | SQLite database |
| `trainedData.sos`, `count.sos`, `imagesCount.sos` | Trained model, number of people, photo counter |
| `cascade.xml` | Cascade classifier file, not used by the main scripts |

Other helper scripts: `CamTest.py`, `trial.py`.

## Limitations

- **No unknown-person rejection.** The classifier always returns one of the registered IDs, so a stranger is assigned to the closest match.
- **Attendance has no date or time.** It is a single `Present` flag per person, and the once-per-session check lives in memory, so it resets on restart.
- **Registration is unfinished.** `Registration.py` does not save the name or image yet. People are currently added by hand to `students` and `DataSet/`.
- **No evaluation yet** on held-out photos or different lighting conditions.

## Roadmap

- [ ] Reject unknown faces with a distance or probability threshold
- [ ] Date-stamped attendance log with CSV export
- [ ] Finish registration: webcam capture, `DataSet/` update and automatic retraining
- [ ] Parameterised SQL queries
- [ ] `requirements.txt` and an accuracy evaluation on held-out photos

## Acknowledgements

[`face_recognition`](https://github.com/ageitgey/face_recognition) by Adam Geitgey, [dlib](http://dlib.net/) by Davis King, and OpenCV.
