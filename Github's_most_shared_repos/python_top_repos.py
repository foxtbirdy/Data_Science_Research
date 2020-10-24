import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url_id = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url_id)



response_dict = r.json()
repo_dicts = response_dict["items"]

names , plot_dicts = [] , []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    plot_dict = {
        "value": repo_dict['stargazers_count'] ,
        "label": str(repo_dict["description"]),
        }

    plot_dicts.append(plot_dict)


############ Random Print ###############
print("Status code :" , r.status_code)
print("Total Repositories: " , response_dict["total_count"])
print("Repositories returned  " , len(repo_dicts))
if r.status_code == 200:
    print("Repositories Completed and Presented as SVG")
else:
    print("Repositories Completed and Presented as SVG but with irregular response")
############ Random Print ###############


    
########## Configuration ############
pygal_config = pygal.Config()
pygal_config.x_label_rotation = 45
pygal_config.show_legend = False
pygal_config.title_font_size = 24
pygal_config.label_font_size = 14
pygal_config.major_label_font_size = 18
pygal_config.truncate_label = 15
pygal_config.show_y_guides = False
pygal_config.width = 1000
########## Configuration ############

fav_style = LS("#800080" , base_style = LCS)
chart  = pygal.Bar(pygal_config, style=fav_style)
chart.title = "Github's most shared Python Based projects \nCoded by Climax_"
chart.x_labels = names
chart.add("" , plot_dicts)
chart.render_to_file("SVG/python_top_repos.svg")
