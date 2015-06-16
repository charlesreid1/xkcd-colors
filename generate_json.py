"""
Use Seaborn's built-in XKCD RGB color dictionary
to dump out a JSON file with the colors and their
hex values.
"""
import json
import seaborn as sns

with open('xkcd-colors.json','w') as f:
    json.dump(sns.xkcd_rgb,f,sort_keys=True, indent=4, separators=(',', ': '))

