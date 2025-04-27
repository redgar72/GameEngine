import pyglet
from pyglet.gl import glClearColor, glViewport
import moderngl
import numpy as np
from utils.config_loader import ConfigLoader
from utils.shader_loader import ShaderLoader


class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        # Load configuration
        self._settings = ConfigLoader()

        # Get window settings from config
        width = self._settings.get('window.width', 800)
        height = self._settings.get('window.height', 600)
        caption = self._settings.get('window.title', 'Game Engine')
        fullscreen = self._settings.get('window.fullscreen', False)
        vsync = self._settings.get('window.vsync', True)

        # Initialize window with config values
        super().__init__(
            width=width,
            height=height,
            caption=caption,
            fullscreen=fullscreen,
            vsync=vsync,
            *args,
            **kwargs
        )

        # Create ModernGL context
        self.ctx = moderngl.create_context()

        # Set up OpenGL state from config
        clear_color = self._settings.get(
            'graphics.clear_color',
            [0.0, 0.0, 0.0, 1.0]
        )
        glClearColor(*clear_color)

        if self._settings.get('graphics.depth_test', True):
            self.ctx.enable(moderngl.DEPTH_TEST)

        if self._settings.get('graphics.cull_face', True):
            self.ctx.enable(moderngl.CULL_FACE)

        # Load shaders
        self.shader_loader = ShaderLoader(self.ctx)
        self.prog = self.shader_loader.load_shader('basic.vert', 'basic.frag')

        if not self.prog:
            raise RuntimeError("Failed to load shaders")

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

    @property
    def config(self):
        """Get the configuration object."""
        return self._config

    def on_draw(self):
        """Render the scene."""
        self.clear()
        self.vao.render()

    def on_resize(self, width, height):
        """Handle window resize events."""
        super().on_resize(width, height)
        glViewport(0, 0, width, height)

    def cleanup(self):
        """Clean up resources."""
        if hasattr(self, 'vbo'):
            self.vbo.release()
        if hasattr(self, 'vao'):
            self.vao.release()
        if hasattr(self, 'prog'):
            self.prog.release()
        if hasattr(self, 'ctx'):
            self.ctx.release()


if __name__ == '__main__':
    window = GameWindow()
    try:
        pyglet.app.run()
    finally:
        window.cleanup()
