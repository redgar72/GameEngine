#version 330

// Input vertex attributes
in vec2 in_vert;

// Output to fragment shader
out vec2 frag_uv;

void main() {
    // Pass through the vertex position
    gl_Position = vec4(in_vert, 0.0, 1.0);
    
    // Calculate UV coordinates (assuming we'll add texture support later)
    frag_uv = (in_vert + vec2(1.0)) * 0.5;
} 