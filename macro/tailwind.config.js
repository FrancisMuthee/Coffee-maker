/** @type {import('tailwindcss').Config} */
export const content = ['./staticfiles/css/**/*.html', './templates/**/*.js'];
export const theme = {
  extend: {},
};
export const plugins = [require('@tailwindcss/aspect-ratio')];
