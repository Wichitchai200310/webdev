module.exports = {
  content: [
    './templates/**/*.html',     // Django templates
    './**/templates/**/*.html',  // In case of multiple apps
    './static/**/*.js',          // Any custom JavaScript files where you might use Tailwind classes
    './static/**/*.css',         // Any CSS files that may contain Tailwind classes
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
