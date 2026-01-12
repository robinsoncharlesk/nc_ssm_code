/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'deep-blue': '#1e3a5f',
        'warm-gold': '#d4af37',
        'soft-white': '#f8f9fa',
      },
      fontFamily: {
        'serif': ['Georgia', 'serif'],
      }
    },
  },
  plugins: [],
}
