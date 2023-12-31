/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        '../../**/*.py',
        './node_modules/flowbite/**/*.js',
    ],
    theme: {
        extend: {
            colors: {
                'primary': {
                    light: '#162F79',
                    DEFAULT: '#0A2472', // Bay of Many
                    dark: '#081B56',

                 },
                'secondary': '#58A7B8', // Fountain Blue
                'light': '#F1E9EE', // Dawn Pink
                'dark': {
                    light: '#333241',
                    DEFAULT: '#282737', // Steel Gray
                },
                'success': {
                    light: '#70A889',
                    DEFAULT: '#408B62', // Viridian
                    dark: '#30684A',
                },
                'warning': {
                    light: '#CE9C5F',
                    DEFAULT: '#BE7B2A', // Marigold
                    dark: '#8F5C20',
                },
                'danger': {
                    light: '#F6695E',
                    DEFAULT: '#F44336', // Pomegranate
                    dark: '#86251E',
                }
            }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        require('flowbite/plugin')
    ],
}
