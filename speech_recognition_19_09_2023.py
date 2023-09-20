import speech_recognition as sr

r = sr.Recognizer()

# Usa el micrófono como fuente de audio y escucha
with sr.Microphone() as source:
    print("Dime algo...")
    audio = r.listen(source)

# Intenta reconocer el audio
try:
    print("Creo que dijiste: " + r.recognize_google(audio, language="es-ES"))
    texto_reconocido = r.recognize_google(audio, language="es-ES")

    if "hola" in texto_reconocido:
        print("Suscríbete al canal de Dimas")
    else:
        print("Comando no detectado")

except sr.UnknownValueError:
    print("No pude entender el audio.")
except sr.RequestError:
    print("Hubo un error con la API de Google")
