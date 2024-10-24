import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

st.title("Fisika Komputasi Awan")
st.title("Norma Azzahra Widyasti :cat:")

circle = Circle((0, 0), 1, color='red', fill=False, linewidth=2, linestyle='-', alpha=0.2)

if st.button("Data"):
    # Reset data setiap kali tombol ditekan
    x = [0]
    y = [0]
    color = [(0., .7, 0.)]
    size = [371]

    for i in range(111):
        x0 = 2 * (random.random() - .5)
        y0 = 2 * (random.random() - .5)
        if (x0**2 + y0**2) > 1.:
            if y0 > 0:
                y0 = np.sqrt(1 - x0**2)
            else:
                y0 = -np.sqrt(1 - x0**2)

        x.append(x0)
        y.append(y0)
        color.append((random.random(), random.random(), random.random()))
        size.append(3713 * random.random())

    # Membuat figure dan ax
    fig, ax = plt.subplots(figsize=(16, 16))
    ax.add_patch(circle)

    # Plot garis dari titik pusat ke titik acak
    for i in range(1, len(x)):
        ax.plot([0, x[i]], [0, y[i]], color='green', linestyle='--', alpha=0.2)

    # Plot titik acak dengan warna dan ukuran acak
    ax.scatter(x, y, c=color, s=size, alpha=0.5)

    ax.set_ylabel("y")
    ax.set_xlabel("x")
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    ax.set_title('Data Acak yang berubah setiap tombol ditekan')
    ax.grid(True, linestyle='-.')

    # Mengatur batas lingkaran
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)

st.caption("Lingkaran dengan ukuran dan warna acak dan tersebar didalam lingkaran dengan radius 1")
st.divider()
