// gl-font.js

class Font {
    constructor(source) {
        this.source = source;
        this.altas_tex = undefined;
    }
    
    release() {
        if(this.altas_tex) {
            gl.deleteTexture(this.altas_tex);
            this.altas_tex = undefined;
        }
    }
    
    promise() {
        
    }
    
    render(text, transform) {
        // gl.QUAD_STRIP
    }
}