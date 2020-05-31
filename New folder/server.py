from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  import speech_recognition as sr
  r = sr.Recognizer()
  
  with sr.Microphone() as source:
     print("Talk")
     audio_text = r.listen(source)
     print("Time over, thanks")
     
     try: 
        print("Text: "+r.recognize_google(audio_text))
     except:
         print("Sorry, I did not get that")
  #return r.recognize_google(audio_text)
  return render_template("index.html", text=r.recognize_google(audio_text))

def demo(text,key):
    if key == 0:
        return text
    else:
        
        cipher = ""
        for x in range(len(text)):
            if text[x].isalpha():   
                if text[x].islower():  
                    cipher += chr((ord(text[x]) - 97 + key) % 26 + 97)
                else:  # uppercase
                    cipher += chr((ord(text[x]) - 65 + key) % 26 + 65)
            else:
                cipher += text[x]
        return cipher
 
   

@app.route('/y-link/<text>')
def y_link(text):
  
  import pyttsx3 
  
 
  engine = pyttsx3.init() 
  a=demo(text,4)
 
  engine.say(a) 
  
  engine.runAndWait() 
  return render_template("index.html", text1=a)


def decrypt(text,key): 
    if key == 0:
        return text
    else:
        
        cipher = ""
        for x in range(len(text)):
            if text[x].isalpha():   
                if text[x].islower():   
                    cipher += chr((ord(text[x]) - 97 - key) % 26 + 97)
                else:   
                    cipher += chr((ord(text[x]) - 65 - key) % 26 + 65)
            else:
                cipher += text[x]
        return cipher

@app.route('/m-link/<text>')
def m_link(text):
  
 
  import pyttsx3 
  
 
  engine = pyttsx3.init() 
  b=decrypt(text,4)
 
  engine.say(b) 
  
  engine.runAndWait() 
  return render_template("index.html", text2=b)
if __name__ == '__main__':
  app.run(debug=True)