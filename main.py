import flet as ft
import requests


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
    field_weather_temp.value = f"Температура {temp}°С"
    field_weather_condition.value = condition
    page.update()
    
  
  def change_theme(event):
    page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
    page.update()
    
  
  field_weather_temp = ft.Text('')
  field_weather_condition = ft.Text('')
  
  weather_elements = field_weather_condition, field_weather_temp
  
  user_city_input = ft.TextField(label='Введите город', width=300)
  change_theme_button = ft.IconButton(ft.icons.SUNNY, on_click=change_theme)
  weather_start_text = ft.Text('Погодные условия')
  confirm_user_city_button = ft.ElevatedButton(text='К прогнозу', on_click=get_info)
  
  user_elements = change_theme_button, weather_start_text, user_city_input, confirm_user_city_button

  for elem in user_elements:    
    page.add(      
      ft.Row([elem], alignment=ft.MainAxisAlignment.CENTER)
    )
  for elem in weather_elements:  
      page.add(      
        ft.Row([elem], alignment=ft.MainAxisAlignment.CENTER)
      )

ft.app(target=main)



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
