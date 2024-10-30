import cv2

# Muat file kaskade Haar untuk deteksi wajah
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Inisialisasi objek kamera
cap = cv2.VideoCapture(0)  # Angka 0 mengacu pada kamera utama (biasanya webcam internal)

# Inisialisasi variabel jumlah orang
person_count = 0


import time
import paho.mqtt.client as paho

broker="127.0.0.1"
#broker="mqtt.ardumeka.com"#"broker.emqx.io"
#port = 11219
port = 1883
detect_time_prev = 0
detect_time = 0
topic_test = ""


def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    t = str(message.topic)

    if(msg[0] == 'c'):
        val =  1
    else:
        val = (msg)
    
    if (t == "testestes"):
        global topic_test
        topic_test = (msg)
        print(topic_test)
        

client= paho.Client("PC_0")
client.on_message=on_message

print("connecting to broker ",broker)
client.connect(broker,port)#connect
print(broker," connected")
    
client.loop_start()
print("Subscribing")

client.subscribe("testestes")





while True:
    # Ambil frame dari kamera
    ret, frame = cap.read()

    # Konversi frame ke mode Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Loop melalui daftar kotak deteksi dan gambarkan kotak tersebut pada frame asli
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Update jumlah orang
    person_count = len(faces)
    
    detect_time = time.time() - detect_time_prev
    if (person_count > 0):
        client.publish("IoTDevice2024/lamp",str("ON"))
        
        detect_time_prev = time.time()
    
    
    if ((person_count == 0) and (detect_time > 1)):
        client.publish("IoTDevice2024/lamp",str("OFF"))
        
    
    
    # Tampilkan jumlah orang
    cv2.putText(frame, f'Jumlah Orang: {person_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Tampilkan frame dengan kotak deteksi wajah
    cv2.imshow('Deteksi Wajah', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela tampilan
cap.release()
cv2.destroyAllWindows()
