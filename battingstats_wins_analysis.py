from pybaseball import team_batting
import matplotlib.pyplot as plt
import numpy as np

# Data
batting = team_batting(2015, 2025, ind=1)
df = batting[['Team', 'Season', 'AVG', 'OBP', 'SLG', 'OPS', 'WAR']].copy()

# Plot
stats   = ['AVG',  'OBP',   'SLG',     'OPS']
colors  = ['red',  'blue',  'green',   'purple']
labels  = ['Batting Average (AVG)', 'On-Base Percentage (OBP)',
           'Slugging Percentage (SLG)', 'On-Base Plus Slugging (OPS)']

fig, axes = plt.subplots(2, 2, figsize=(14, 12), layout='constrained')
fig.suptitle('Which Batting Stat Best Predicts Team Value? (2015–2025)',
             fontsize=16, fontweight='bold')

for ax, stat, color, label in zip(axes.flatten(), stats, colors, labels):
    corr = df[stat].corr(df['WAR'])

    # Scatter
    ax.scatter(df[stat], df['WAR'], alpha=0.4, color=color)

    # Trend line
    m, b = np.polyfit(df[stat], df['WAR'], 1)
    x_line = np.linspace(df[stat].min(), df[stat].max(), 100)
    ax.plot(x_line, m * x_line + b, color='black', linewidth=2)

    ax.set_xlabel(label)
    ax.set_ylabel('WAR')
    ax.set_title(f'{stat} vs WAR  |  r = {corr:.2f}')

plt.savefig('obp_wins_analysis.png', dpi=150, bbox_inches='tight')
plt.show()
