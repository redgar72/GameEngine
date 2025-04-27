import os
from typing import Optional
import moderngl
from .logger import logger


class ShaderLoader:
    def __init__(self, ctx: moderngl.Context):
        self.ctx = ctx
        self.shader_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'shaders'
        )
        logger.debug(f"Shader directory set to: {self.shader_dir}")

    def load_shader(
            self,
            vertex_path: str,
            fragment_path: str) -> Optional[moderngl.Program]:
        """Load and compile a shader program from files."""
        try:
            vertex_path_full = os.path.join(self.shader_dir, vertex_path)
            fragment_path_full = os.path.join(self.shader_dir, fragment_path)

            logger.debug(f"Loading vertex shader: {vertex_path_full}")
            with open(vertex_path_full, 'r') as f:
                vertex_shader = f.read()

            logger.debug(f"Loading fragment shader: {fragment_path_full}")
            with open(fragment_path_full, 'r') as f:
                fragment_shader = f.read()

            logger.debug("Compiling shader program")
            program = self.ctx.program(
                vertex_shader=vertex_shader,
                fragment_shader=fragment_shader,
            )
            logger.info("Shader program compiled successfully")
            return program

        except Exception as e:
            logger.error(f"Error loading shader: {e}")
            return None
