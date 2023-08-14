import cv2

imagem = cv2.imread('solar-system.jpg')

cv2.imshow('Resultado',img)



cv2.waitKey(0)

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )


       