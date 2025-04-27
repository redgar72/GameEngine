#version 330

// Input from vertex shader
in vec2 frag_uv;

// Output color
out vec4 fragColor;

void main() {
    // Simple white color for now
    fragColor = vec4(1.0, 1.0, 1.0, 1.0);
} 