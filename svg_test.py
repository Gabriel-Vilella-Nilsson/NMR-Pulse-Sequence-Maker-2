import svgwrite

dwg = svgwrite.Drawing('.\\output\\test.svg')

# bar = svgwrite.shapes.Rect(insert=(0, 0), size=(10, 5))
#bar = dwg.rect((0, 0), ("3cm", "3cm"), fill='black')

#for p in range(5):
#    dwg.add(dwg.rect((p * 50, p * 50), ("3cm", "3cm"), fill='black'))

start_buffer = 200
gap = 20
bar_y = 400
bar_thickness = 20

bar = dwg.add(dwg.rect((start_buffer, bar_y), (900, bar_thickness)))


thin_b = dwg.add(dwg.rect((start_buffer+gap, bar_y+bar_thickness), (25, 120)))

thin_t = dwg.add(dwg.rect((start_buffer+gap, bar_y-120), (25, 120)))


dwg.save(pretty=True)

