module.exports = {
  mode: "jit", // Activa el modo JIT
  content: [
    "./templates/**/*.html",   // Archivos de Django
    "./static/js/**/*.js",     // Archivos JS con clases dinámicas
    "./static/css/**/*.css",   // Estilos adicionales
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
