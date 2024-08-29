/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				blue: {
					975: '#1D2145'
				},
				amber: {
					350: '#F5C665'
				}
			},
			fontSize: {
				'6.5xl': '4rem'
			}
		}
	},
	plugins: []
};
