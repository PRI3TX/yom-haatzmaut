import qrcode

# Datos a codificar
datos = "https://www.canva.com/design/DAGjnLLS9RA/YtcwVyONgRhx20KHtIE-DA/edit?utm_content=DAGjnLLS9RA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"

# Crear el objeto QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=5,  
    border=1.5,
)

# Agregar datos al QR
qr.add_data(datos)
qr.make(fit=True)

# Crear imagen QR
imagen = qr.make_image(fill="black", back_color="white")

# Guardar imagen
imagen.save("codigo_qr.png")

# Mostrar imagen
imagen.show()


