# 252
def update_score(nscore):
    score = max_score()

    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))

        else:
            f.write(str(nscore))

def max_score():
    with open('scores', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score

""" 265   label = font.render("HIGH SCORE " + str(score), 1, (255, 255, 255))

    sx = top_left_x - 200
    sy = top_left_y + 200

    surface.blit(label, (sx + 20, sy + 180))"""

"""301         if level_time/1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005"""