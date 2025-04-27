import pyglet
from pyglet.gl import glClearColor, glViewport
import moderngl
import numpy as np


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create ModernGL context
        self.ctx = moderngl.create_context()

        # Enable depth testing
        self.ctx.enable(moderngl.DEPTH_TEST)

        # Set up basic OpenGL state
        glClearColor(0.0, 0.0, 0.0, 1.0)

        # Set up basic shader program (we'll improve this later)
        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                in vec2 in_vert;
                void main() {
                    gl_Position = vec4(in_vert, 0.0, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                out vec4 fragColor;
                void main() {
                    fragColor = vec4(1.0, 1.0, 1.0, 1.0);
                }
            ''',
        )

        # Create a simple triangle
        vertices = np.array([
            -0.6, -0.6,
            0.6, -0.6,
            0.0, 0.6,
        ], dtype='f4')

        self.vbo = self.ctx.buffer(vertices.tobytes())
        self.vao = self.ctx.vertex_array(
            self.prog, [(self.vbo, '2f', 'in_vert')]
        )

    def on_draw(self):
        self.clear()
        self.vao.render()

    def on_resize(self, width, height):
        super().on_resize(width, height)
        glViewport(0, 0, width, height)


if __name__ == '__main__':
    window = GameWindow(width=800, height=600, caption='Game Engine')
    pyglet.app.run()
