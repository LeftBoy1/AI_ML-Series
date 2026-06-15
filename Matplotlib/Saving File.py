#plt.savefig('filename.extension', dpi = value, bbox_inches = 'tight')
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [5,15,10,20]

plt.plot(x, y, color = 'red', marker = 'o')
plt.title('Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.savefig('line_plot.png', dpi = 300, bbox_inches = 'tight')
'''
    bbox(Bounding Box) - It controls how much extra space is saved around the plot.

        Example - 
            bbox_inches='tight'
                Means:“Crop the image tightly around the content.
            
            
            
            
    DPI(Dots Per Inch) - It controls image resolution when saving.

        Example - 
            plt.savefig('line_plot.png', dpi=300)
                Means:
                    More DPI → more pixels → sharper image
                    Less DPI → fewer pixels → blurrier image”



'''
plt.show()