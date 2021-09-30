import random
import plotly.express as px
import plotly.figure_factory as ff

count = []
dice_result = []

for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    count.append(i)
    dice_result.append(dice1 + dice2)

# print(count,dice_result)

# fig = px.bar(x = dice_result,y = count)
fig = ff.create_distplot([dice_result],["result"],show_hist=False)
fig.show()