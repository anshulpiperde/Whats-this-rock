import plotly.figure_factory as ff


def confusion_matrix(labels, y, _y):

    l = [ 0 for _ in range(len(labels))]
    z = [ [0 for _ in range(len(labels))] for _ in range(len(labels))]
    h = [ [0 for _ in range(len(labels))] for _ in range(len(labels)) ]

    for i, j in zip(y, _y):
        z[j][i] += 1
        l[i] += 1

    x = labels.copy()
    y = labels.copy()

    z_labels = [ [ str(col) if col != 0 else '' for col in row ] for row in z]

    for i in range(len(labels)):
        for j in range(len(labels)):
            if i == j:
                h[i][j] = 'Correctly predicted ' + str(z[i][j]) + ' out of ' + str(l[i]) + ' ' + labels[i] + ' with accuracy ' + str(z[i][j] / l[i])
            else:
                if z[j][i] == 0:
                    h[j][i] = ''
                else:
                    h[j][i] = 'Incorrectly predicted ' + str(z[j][i]) + ' out of ' + str(l[i]) + ' ' + labels[i] + ' as ' + labels[j]

    fig = ff.create_annotated_heatmap(z, x = x, y = y, text = h, annotation_text = z_labels, hoverinfo = 'text', colorscale ='Blues')

    fig.update_layout(width = 850, height = 550)
    fig.update_layout(margin = dict(t = 100, l = 200))

    fig.add_annotation(dict(font=dict(color="#094973",size=16), x = 0.5, y = -0.10, showarrow = False, text="True Class", xref="paper", yref="paper"))
    fig.add_annotation(dict(font=dict(color="#094973",size=16), x = -0.17, y = 0.5, showarrow = False, text="Predicted Class", textangle=-90, xref="paper", yref="paper"))

    fig.show()
    return fig