import speech_recognition as sr
import googlesearch as gs   
import webbrowser as wb 
import pyttsx3
def main():
    x=pyttsx3.init()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        query=''
        x.say("Welcome I am Angel")
        try:
                while('exit the terminal' not in query):
                        x.say("Please say what you want to search:")
                        x.runAndWait()
                        audio=r.listen(source)
                        try:
                            x.say("You have said:\n"+ r.recognize_google(audio))
                            x.runAndWait()
                            query=r.recognize_google(audio)
                            query=query.lower()
                            if('exit terminal' not in query):
                                first_link=gs.search(query,num=1,tld="co.in",stop=1,pause=0)
                                for i in first_link:
                                    wb.open_new_tab(i)
                        except Exception as e:
                            print("Error 2: " + str(e))
        except Exception as e:
            print("Error 3: " + str(e))
if(__name__=="__main__"):
    main()