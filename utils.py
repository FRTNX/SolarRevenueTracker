import PIL
from PIL import Image
from matplotlib import pyplot as plt

def plot_revenue(params):
    plt.plot(params['payload'])
    plt.xlabel(params['xlabel'])
    plt.ylabel(params['ylabel'])
    plt.title(params['title'])
    plt.grid(params['grid'])
    plt.savefig(params['image_name'], bbox_inches='tight')
    img = Image.open(params['image_name'])
    wpercent = (400 / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((400, hsize), PIL.Image.ANTIALIAS)
    img.show()