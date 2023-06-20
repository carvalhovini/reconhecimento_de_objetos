import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Cores das caixas delimitadoras e etiquetas
DEFAULT_BOX_COLOR = (0, 255, 0)  # Verde
DEFAULT_LABEL_COLOR = (0, 255, 0)  # Verde

# Cores adicionais
COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Função para processar o frame da câmera e atualizar a interface
def process_frame():
    global object_count

    ret, frame = video_capture.read()

    height, width, channels = frame.shape

    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    object_count = 0

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = COLORS[class_ids[i] % len(COLORS)] if use_random_colors.get() else DEFAULT_BOX_COLOR
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            object_count += 1

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(frame)
    image = ImageTk.PhotoImage(image)

    # Obter as dimensões do canvas
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Calcular o deslocamento para centralizar a imagem
    offset_x = (canvas_width - image.width()) // 2
    offset_y = (canvas_height - image.height()) // 2

    # Limpar o canvas
    canvas.delete("all")

    # Desenhar a imagem centralizada no canvas
    canvas.create_image(offset_x, offset_y, anchor='nw', image=image)
    canvas.image = image

    label_count.config(text=f"Objetos: {object_count}")

    if not is_paused.get():
        window.after(1, process_frame)

# Função para iniciar a contagem de objetos
def start_counting():
    global object_count

    object_count = 0
    label_count.config(text="Objetos: 0")
    is_paused.set(False)
    process_frame()

# Função para pausar a contagem de objetos
def pause_counting():
    is_paused.set(True)

# Função para limpar a tela
def clear_screen():
    canvas.delete("all")

# Função para alterar as cores das caixas delimitadoras e das etiquetas
def change_colors():
    box_color = tuple(int(c) for c in entry_box_color.get().split(","))
    label_color = tuple(int(c) for c in entry_label_color.get().split(","))
    DEFAULT_BOX_COLOR = box_color
    DEFAULT_LABEL_COLOR = label_color

# Criar a janela principal
window = tk.Tk()
window.title("Contador de Objetos")
window.geometry("800x650")

# Criar o canvas para exibir o vídeo da câmera
canvas = tk.Canvas(window, width=800, height=500)
canvas.pack()

# Criar o botão para iniciar a contagem
button_start = tk.Button(window, text="Iniciar Contagem", command=start_counting)
button_start.pack()

# Criar o botão para pausar a contagem
is_paused = tk.BooleanVar()
button_pause = tk.Button(window, text="Pausar Contagem", command=pause_counting)
button_pause.pack()

# Criar o botão para limpar a tela
button_clear = tk.Button(window, text="Limpar Tela", command=clear_screen)
button_clear.pack()

# Criar o rótulo para exibir o número de objetos
label_count = tk.Label(window, text="Objetos: 0", font=("Arial", 18))
label_count.pack()

# Criar uma caixa de seleção para ativar/desativar cores aleatórias
use_random_colors = tk.BooleanVar()
check_random_colors = tk.Checkbutton(window, text="Usar Cores Aleatórias", variable=use_random_colors)
check_random_colors.pack()

# Criar uma entrada para alterar a cor das caixas delimitadoras
label_box_color = tk.Label(window, text="Cor da Caixa Delimitadora (R, G, B):")
label_box_color.pack()
entry_box_color = tk.Entry(window)
entry_box_color.pack()

# Criar uma entrada para alterar a cor das etiquetas
label_label_color = tk.Label(window, text="Cor das Etiquetas (R, G, B):")
label_label_color.pack()
entry_label_color = tk.Entry(window)
entry_label_color.pack()

# Criar o botão para alterar as cores
button_change_colors = tk.Button(window, text="Alterar Cores", command=change_colors)
button_change_colors.pack()

# Carregar as configurações e os pesos pré-treinados do YOLO
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# Carregar a lista de classes
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Configurações do YOLO
layer_names = net.getLayerNames()
output_layers = ['yolo_82', 'yolo_94', 'yolo_106']


# Inicialização do contador
object_count = 0

# Inicialização do vídeo da câmera
video_capture = cv2.VideoCapture(0)

window.mainloop()
