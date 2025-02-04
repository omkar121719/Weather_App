import tkinter as tk
import requests
from PIL import Image,ImageTk

root= tk.Tk()

root.title("Weather App")
root.geometry("600x500")

# API Key --> f5f200d5a416b382544c0cce42400080
# API URL --> https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def format_response(weather):
    try:
        city= weather['name']
        condition= weather['weather'][0]['description']
        temp= weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature: %s'%(city, condition, temp)
    except:
        final_str = 'There was a problem retrieving the weather data'
    return final_str

def get_weather(city):
    weather_key= 'f5f200d5a416b382544c0cce42400080'
    url= 'https://api.openweathermap.org/data/2.5/weather'
    params= {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response= requests.get(url, params)
    #  print(response.json()) #prints the data in terminal
    weather= response.json()

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])

    result['text']= format_response(weather)

    icon_name= weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size= int(frame_two.winfo_height()*0.25)
    img= ImageTk.PhotoImage(Image.open('./img/'+ icon+ '.png').resize((size,size)))
    wetaher_icon.delete('all')
    wetaher_icon.create_image(0,0,anchor='nw',image=img)
    wetaher_icon.image= img

img= Image.open('./bg.png')
img = img.resize((600, 500), Image.Resampling.LANCZOS)
img_photo= ImageTk.PhotoImage(img)

bg_lbl= tk.Label(root, image= img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

heading_title= tk.Label(bg_lbl, text='Earth including over 2,00,000 cities!', fg='red', bg='skyblue', font=('Times new Roman', 18, 'bold'))
heading_title.place(x=80, y=18)

frame_one= tk.Frame(bg_lbl, bg="#42c2f4", bd=5)
frame_one.place(x=80, y=50, width=450, height=50)

txt_box= tk.Entry(frame_one, font=('Times new Roman', 25), width=17)
txt_box.grid(row=0, column=0, sticky='W')

btn= tk.Button(frame_one, text='Get Weather', fg='green', font=('Times new Roman', 16, 'bold'), command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two= tk.Frame(bg_lbl, bg="#42c2f4", bd=5)
frame_two.place(x=80, y=130, width=450, height=300)

result= tk.Label(frame_two, font=40, bg='white', justify='left', anchor='nw')
result.place(relwidth=1, relheight=1)

wetaher_icon= tk.Canvas(result, bg='white', bd=0, highlightthickness=0)
wetaher_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()