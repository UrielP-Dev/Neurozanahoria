import cv2
import numpy as np


lower_orange = np.array([5, 150, 70])
upper_orange = np.array([15, 255, 255])

# Iniciar la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir a espacio de color HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Filtrar colores dentro del rango naranja
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    
    # Encontrar contornos
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Calcular el área del contorno
        area = cv2.contourArea(contour)
        
        # Si el área es suficientemente grande, dibujar un rectángulo y etiquetar como "naranja"
        if area > 100:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 165, 255), 2)
            cv2.putText(frame, 'Zanahoria', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 165, 255), 2)
    
    # Mostrar el video en vivo
    cv2.imshow('Demo NeuroZanahoria', frame)
    
    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
