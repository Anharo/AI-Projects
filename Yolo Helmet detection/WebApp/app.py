from flask import Flask, Response, render_template, request, jsonify
import cv2
from ultralytics import YOLO

app = Flask(__name__)
MODEL_PATH = r"C:\\Users\\anish\\OneDrive\\Desktop\\YoloV11 object detection\\helmet-detection.v10i.yolov11\\yolo11_Custom.pt"
model = YOLO(MODEL_PATH)
video_capture = cv2.VideoCapture(0)
detection_enabled = True

def generate_frames():
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        if detection_enabled:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = model(rgb_frame)
            for r in results:
                for box in r.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    confidence = box.conf.item()
                    label = f"{r.names[int(box.cls)]} {confidence:.2f}"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/toggle_detection", methods=["POST"])
def toggle_detection():
    global detection_enabled
    detection_enabled = not detection_enabled
    status = "enabled" if detection_enabled else "disabled"
    return jsonify({"status": status})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
