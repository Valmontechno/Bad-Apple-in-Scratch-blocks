import cv2

video_path = "BadApple.mp4"
out_path = "data.txt"
new_width, new_height = 28, 20
pixel_ratio = 113 / 108
display_scale = 50
fps = 30
threshold = 128  # Seuil pour noir/blanc

proc_witdh = new_width
proc_height = int(new_height * pixel_ratio)
out = []

# Ouvrir la vidéo
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise FileNotFoundError(f"Impossible d'ouvrir la vidéo : {video_path}")

# Récupérer le FPS original
original_fps = cap.get(cv2.CAP_PROP_FPS)
assert original_fps >= fps 
frame_interval = original_fps / fps  # Saut de frames

print("Start")

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # if frame_count > 60:
    #     break

    # Ne prendre qu'une frame toutes les "frame_interval"
    if frame_count % frame_interval == 0:
        # Redimensionner
        resized = cv2.resize(frame, (proc_witdh, proc_height), interpolation=cv2.INTER_NEAREST)

        # Conversion en niveaux de gris
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        frame_ligne = []
        for y in range(proc_height):
            for x in range(proc_witdh):
                pixel = gray[y, x]  # 0 = noir, 255 = blanc
                if pixel >= threshold:
                    frame_ligne.append("1")
                else:
                    frame_ligne.append("0")
        out.append("".join(frame_ligne))

        # Affichage
        # _, bw = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        # display_img = cv2.resize(bw, (new_width * display_scale, new_height * display_scale), interpolation=cv2.INTER_NEAREST)
        # cv2.imshow(video_path, display_img)

    frame_count += 1

cap.release()
cv2.destroyAllWindows()

with open(out_path, "w", encoding="utf-8") as file:
    file.write("\n".join(out))

print("Done")