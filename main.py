import flet as ft
import requests
import datetime


def main(page: ft.Page):
  page.title = 'Weather App'
  page.theme_mode = 'dark'
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  

  def get_info(event):
    if len(user_city_input.value) < 1:
      print('Нет такого')
      return
    
    API = '6f9576c296b0795de68e82f32df1f7d5'
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_city_input.value}&appid={API}&units=metric&lang=ru').json()
    print(weather)
    
    temp = weather['main']['temp']
    condition = weather['weather'][-1]['description']
    wind_speed = weather['wind']['speed']
    
    field_weather_temp.value = f"Температура: {temp}°С"
    field_weather_condition.value = f"Условия: {condition}"
    field_weather_wind.value = f"Скорость ветра: {wind_speed} м/c"
    
    # url_icon_condition = f"https://openweathermap.org/img/wn/{weather['weather'][-1]['icon'].replace('d', 'n')}@2x.png"
    # condition_icon.src = url_icon_condition
    
    page.update()
    
  
  def change_theme(event):
    page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
    page.update()
    
    
  def view_date_time():
    date_time = datetime.datetime.now().strftime('%d %h %Y | %H:%M')
    date_time_text.value = date_time
    page.update()
  
  
  # condition_icon = ft.Image()
  
  field_weather_temp = ft.Text('')
  field_weather_condition = ft.Text('')
  field_weather_wind = ft.Text('')
  
  weather_elements = field_weather_condition, field_weather_temp, field_weather_wind
  
  change_theme_button = ft.IconButton(ft.icons.SUNNY, on_click=change_theme)
  user_city_input = ft.TextField(label='Введите город', width=300)
  date_time_text = ft.Text('')
  weather_start_text = ft.Text('Погодные условия')
  confirm_user_city_button = ft.ElevatedButton(text='К погоде', on_click=get_info)
  
  user_elements = change_theme_button, weather_start_text, date_time_text, user_city_input, confirm_user_city_button
  view_date_time()
  
  for elem in user_elements:    
    page.add(      
      ft.Row([elem], alignment=ft.MainAxisAlignment.CENTER)
    )
    
  # page.add(ft.Container(content=ft.Control(icon), alignment=ft.MainAxisAlignment.CENTER))
  
  for elem in weather_elements:  
      page.add(      
        ft.Row([elem], alignment=ft.MainAxisAlignment.CENTER)
      )
  

ft.app(target=main, view=ft.AppView.WEB_BROWSER)



# label = ft.Text('Info', color='yellow')
#     user_input = ft.TextField(value='0', width=150, text_align=ft.TextAlign.CENTER)

#     def get_info(event):
#         label.value = user_input.value
#         page.update()


#     page.add(
#         ft.Row(
#             [ 
#                 ft.IconButton(ft.icons.HOME, on_click=get_info),
#                 ft.IconButton(ft.icons.BACK_HAND),
#                 ft.ElevatedButton(text='PUSH', on_click=get_info),
#                 ft.OutlinedButton(text='PUSH', on_click=get_info),
#                 ft.Checkbox(label='Agree?', value=True, on_change=get_info)


#             ],
#             alignment=ft.MainAxisAlignment.CENTER
#         ),
#         ft.Row(
#             [
#                 label,
#                 user_input
#             ],
#             alignment=ft.MainAxisAlignment.CENTER
#         )
#     )
