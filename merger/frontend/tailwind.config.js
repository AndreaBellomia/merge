/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,vue}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#1F1F1F",
        primaryVariant: "#313131",
        secondary: "#A771FF",
        secondaryVariant: "#6E14FF",

        greenCustom: '#1ABD00',
        orangeCustom: '#FFB800',
        redCustom: '#FF1F00',
        redCustomVariant: '#C71800',

      },
      fontFamily: {
      },
    },
    screens: {
      xs: "480px",
      ss: "620px",
      sm: "768px",
      md: "1060px",
      lg: "1200px",
      xl: "1700px",
    },
  },
  plugins: [],
}