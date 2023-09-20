import tkinter as tk
from PIL import Image, ImageTk


def mostrar_imagen(ruta_imagen, image_size: tuple[int, int]):
    ventana = tk.Tk()
    ventana.title("Imagen con Tkinter y Pillow")

    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize(size=image_size)
    imagen_tk = ImageTk.PhotoImage(imagen)

    etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
    etiqueta_imagen.pack()

    # etiqueta_imagen.image = imagen_tk
    ventana.mainloop()


# Llama a la función con la ruta de tu imagen
mostrar_imagen("8924570_2738.jpg", image_size=(200, 200))
