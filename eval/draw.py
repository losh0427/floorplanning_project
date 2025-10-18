import sys
import matplotlib.pyplot as plt
import sys
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def parse_input(lines):
    soft_modules = {}
    fixed_modules = {}
    triangles = []
    triangles2 = []
    connection = []
    chip_width, chip_height = None, None

    i = 0
    while i < len(lines):
        line = lines[i].split()
        module_type = line[0]
        if module_type == "CHIP":
            chip_width, chip_height = int(line[1]), int(line[2])
            i += 1
        elif module_type == "SOFTMODULE":
            num_modules = int(line[1])
            i += 1
            for _ in range(num_modules):
                num_corners = int(lines[i].split()[1])
                corners = []
                for j in range(num_corners):
                    x, y = map(int, lines[i + 1 + j].split())
                    corners.append((x, y))
                soft_modules[lines[i].split()[0]] = corners
                i += num_corners + 1
        elif module_type == "FIXEDMODULE":
            num_modules = int(line[1])
            i += 1
            for _ in range(num_modules):
                name, x, y, width, height = lines[i].split()
                fixed_modules[name] = (int(x), int(y), int(width), int(height))
                i += 1
        elif module_type == "triangle":
            num_modules = int(line[1])
            i += 1
            for _ in range(num_modules ):
                if (lines[i].split()[0] == "trianglee"):
                    break
                x0, y0, x1, y1 = map(int, lines[i].split())
                triangles.append(((x0, y0), (x1, y1)))
                i += 1
        elif module_type == "connection":
            num_modules = int(line[1])
            i += 1
            for _ in range(num_modules ):
                x0, y0, x1, y1 = map(int, lines[i].split())
                connection.append(((x0, y0), (x1, y1)))
                i += 1
        elif module_type == "trianglee":
            num_modules = int(line[1])
            i += 1
            for _ in range(num_modules):
                x0, y0, x1, y1 = map(int, lines[i].split())
                triangles2.append(((x0, y0), (x1, y1)))
                i += 1
        else:
            i += 1

    return chip_width, chip_height, soft_modules, fixed_modules, triangles, triangles2, connection


def plot_modules(chip_width, chip_height, soft_modules, fixed_modules, triangles, triangles2, connection):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 0, chip_width, chip_width, 0], y=[0, chip_height, chip_height, 0, 0], mode='lines', name="chip"))
    if chip_height > chip_width :
        fig.add_trace(go.Scatter(x=[0, 0, chip_height, chip_height, 0], y=[0, chip_height, chip_height, 0, 0], mode='lines', name="rec"))
    else :
        fig.add_trace(go.Scatter(x=[0, 0, chip_width, chip_width, 0], y=[0, chip_width, chip_width, 0, 0], mode='lines', name="rec"))
    for name, corners in soft_modules.items():
        x_coords, y_coords = zip(*corners + [corners[0]])  # Add first corner at the end to complete the shape
        fig.add_trace(go.Scatter(x=x_coords, y=y_coords, mode='lines', name=name))

    for name, (x, y, width, height) in fixed_modules.items():
        x_coords = [x, x + width, x + width, x, x]
        y_coords = [y, y, y + height, y + height, y]
        fig.add_trace(go.Scatter(x=x_coords, y=y_coords, mode='lines', fill='toself', fillcolor='grey', line=dict(color='black'), name=name))

    for (x0, y0), (x1, y1) in triangles:
        # fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='blue'), name="triangle"))
        fig.add_annotation(
            x=x1,      
            y=y1,      
            ax=x0,     
            ay=y0,     
            xref='x',
            yref='y',
            axref='x',
            ayref='y',
            showarrow=True,
            arrowhead=1,
            arrowwidth=2,
            arrowcolor='red',  
        )
    for (x0, y0), (x1, y1) in triangles2:
        # fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='blue'), name="triangle"))
        fig.add_annotation(
            x=x1,      
            y=y1,      
            ax=x0,     
            ay=y0,     
            xref='x',
            yref='y',
            axref='x',
            ayref='y',
            showarrow=True,
            arrowhead=1,
            arrowwidth=2,
            arrowcolor='blue',  
        )
    for (x0, y0), (x1, y1) in connection:
        fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='black'), name="connection"))
        # fig.add_annotation(
        #     x=x1,      
        #     y=y1,      
        #     ax=x0,     
        #     ay=y0,     
        #     xref='x',
        #     yref='y',
        #     axref='x',
        #     ayref='y',
        #     showarrow=True,
        #     arrowhead=1,
        #     arrowwidth=2,
        #     arrowcolor='black',  
        # )


    fig.update_xaxes(scaleanchor="y")
    fig.update_yaxes(scaleanchor="x")
    fig.update_layout(
        title="ar100_0.001_10w",
        xaxis_title="X coordinate",
        yaxis_title="Y coordinate",
        showlegend=True,
    )

    fig.show()


def main():
    if len(sys.argv) != 2:
        print("Usage: python draw.py <filename>")
        return

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    chip_width, chip_height, soft_modules, fixed_modules, triangles, triangles2, connection = parse_input(lines)
    plot_modules(chip_width, chip_height, soft_modules, fixed_modules, triangles, triangles2, connection)


if __name__ == "__main__":
    main()
