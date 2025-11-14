import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.transforms import Affine2D

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_facecolor('white')


pink_color = '#FFB6C1' 
dark_pink = '#FF69B4' 
nose_color = '#FF1493'
black = '#000000'
white = '#FFFFFF'

def triangle(x, y, w, h, rotation=0, facecolor=pink_color, edgecolor=dark_pink, linewidth=2):
    points = [[x-w/2, y-h/2], [x+w/2, y-h/2], [x, y+h/2]]
    
    if rotation == 0:
        ax.add_patch(patches.Polygon(points, facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth))
    else:
        rad = np.radians(rotation)
        cos_angle = np.cos(rad)
        sin_angle = np.sin(rad)
        
        rotated_points = []
        for px, py in points:
            dx = px - x
            dy = py - y
            new_x = x + dx * cos_angle - dy * sin_angle
            new_y = y + dx * sin_angle + dy * cos_angle
            rotated_points.append([new_x, new_y])
        
        ax.add_patch(patches.Polygon(rotated_points, facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth))

def ellipse(x, y, w, h, facecolor=pink_color, edgecolor=dark_pink, linewidth=2):
    ax.add_patch(patches.Ellipse((x, y), w, h, facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth))

def circle(x, y, r, facecolor=pink_color, edgecolor=dark_pink, linewidth=2):
    ax.add_patch(patches.Circle((x, y), r, facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth))

def line(x, y, length, angle=0, color='black', linewidth=2):
    rad = np.radians(angle)
    end_x = x + length * np.cos(rad)
    end_y = y + length * np.sin(rad)
    
    ax.plot([x, end_x], [y, end_y], color=color, linewidth=linewidth)

def rectangle(x, y, width, height, facecolor=pink_color, edgecolor=dark_pink, linewidth=2):
    rect = patches.Rectangle((x - width/2, y - height/2), width, height,
                           facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth) 
    ax.add_patch(rect)

# Рисуем мини-пига
# Тело
rectangle(3.4, 3.7, 0.5, 1.5)
rectangle(4.2, 3.7, 0.5, 1.5)
rectangle(5.8, 3.7, 0.5, 1.5)
rectangle(6.6, 3.7, 0.5, 1.5)
ellipse(5, 4.5, 4, 2.5)

# Голова
triangle(5.70, 6.5, 1, 1, 30)
triangle(5.70+1.5, 6.5, 1, 1, 330)
circle(6.45, 5.80, 1)
ellipse(6.45, 5.8, 0.75, 0.5, nose_color)
circle(6.35, 5.8, 0.02, black, black)
circle(6.55, 5.8, 0.02, black, black)

# Пятачок
circle(6.90, 6.25, 0.2, white, white)
circle(6.05, 6.25, 0.2, white, white)
circle(6.90, 6.25, 0.03, black, black)
circle(6.05, 6.25, 0.03, black, black)

# Рот
line(6.45, 5.2, 0.3, 15)
line(6.45, 5.2, 0.3, 165)

# Хвост
line(3.04, 4.8, 0.3, 160, dark_pink)
line(2.75, 4.89, 0.2, 100, dark_pink)
line(2.71, 5.10, 0.2, 40, dark_pink)
line(2.86, 5.23, 0.15, 340, dark_pink)
line(2.99, 5.19, 0.15, 280, dark_pink)
line(3.01, 5.04, 0.1, 220, dark_pink)
line(2.94, 4.99, 0.1, 160, dark_pink)

ax.axis('off')
plt.title('Мини-пиг', fontsize=16, fontweight='bold', color='#8B4513')
plt.tight_layout()
plt.show()