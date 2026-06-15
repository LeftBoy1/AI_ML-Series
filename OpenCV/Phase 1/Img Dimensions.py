import cv2

img = cv2.imread(r"F:\Devansh_Gupta\AI + ML\OpenCV\Phase 1\o.jpg")

if img is not None:
    h, w, c = img.shape     #h= height, w=width, c=color channels
    print(f"Height:{h}\nWidth:{w}\nColor:{c}\n")   
    
else:
    print("Could not load image!!")