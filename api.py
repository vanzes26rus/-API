import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Cоздание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)
# сохранение ответа API в переменной.
response_dict = r.json()
# Обработка результатов
print(response_dict.keys())
# Анализ информации о репрозиториях.
print(f'Total repositories:{response_dict["total_count"]}')
repo_dicts = response_dict['items']
print(f"Repositiries returned:{len(repo_dicts)}")
# анализ первого репрозитория.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {'value': repo_dict['stargazers_count'],
                 'label': repo_dict['description'],
                 'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

# создание настроек
my_config = pygal.Config()
# Метки проворачивают на 45 градусов
my_config.x_label_rotation = 45
# на диаграмму наносится только одна серия данных
my_config.show_legend = False
# Шрифт для столбцов и заголовка
my_config.title_font_size = 24
my_config.major_label_font_size = 18
# используестся для сокращения длинных имен
my_config.truncate_label = 15
# скрываются горизотальные линии
my_config.show_y_guides = False


# построение визуализации.
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add("", plot_dicts)
chart.render_to_file("python_repos.svg")


