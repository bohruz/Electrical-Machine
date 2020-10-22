import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():

    def angular_velocity(frequency):
        return 2 * np.pi * frequency

    def B1(w, t, phase):

        return np.sin(w * t + phase) * (np.cos(phase) + 1j * np.sin(phase))

    def B2(w, t, phase):

        return np.sin(w * t + phase) * \
            (np.cos(phase) + 1j * np.sin(phase))

    def B3(w, t, phase):

        return np.sin(w * t + phase) * \
            (np.cos(phase) + 1j * np.sin(phase))

    def create_arrow(B, color, name):
        arrow = ax.arrow(0, 0, B.real, B.imag, head_width=0.05,
                         head_length=0.1, fc=color, ec=color, length_includes_head=True, label=name)
        ax.legend(loc='upper right', fontsize='medium')

        return arrow

    def create_circle():
        circle = plt.Circle((0, 0), 1.5, color='gray',
                            fill=False)
        ax.add_artist(circle)

    fig, ax = plt.subplots(figsize=(7, 7))

    def set_format():
        ax.set(xlim=(-2, 2), ylim=(-2, 2))
        ax.set_aspect('equal', adjustable='box')

        plt.title("Campo Magnético Girante", fontsize=16)
        plt.xlabel(r"$B \mathbf{\vec X}$", fontsize=14)
        plt.ylabel(r"$B \mathbf{\vec Y}$", fontsize=14)

    names = [r"$\vec B_{a}$", r"$\vec B_{b}$",
             r"$\vec B_{c}$", r"$\vec B_{net}$"]

    phase = {"A": 0.0, "B": - 2 * np.pi/3, "C": 2 * np.pi/3}

    colors = ['k', 'b', 'm', 'r']

    def fields(time, freq=60.0):

        t = time/(freq * 100)

        w = angular_velocity(freq)

        Ba = B1(w, t, phase["A"])
        Bb = B2(w, t, phase["B"])
        Bc = B3(w, t, phase["C"])

        Bnet = Ba + Bb + Bc

        return [Ba, Bb, Bc, Bnet]

    def animate(time):

        ax.cla()
        create_circle()
        set_format()

        magnetic_fields = zip(fields(time), colors, names)

        for field, color, name in magnetic_fields:

            create_arrow(field, color, name)

    ani = animation.FuncAnimation(fig, animate, interval=20, frames=100)
    ani.save("Campo-Girante.gif")
    plt.show()


if __name__ == "__main__":
    main()
