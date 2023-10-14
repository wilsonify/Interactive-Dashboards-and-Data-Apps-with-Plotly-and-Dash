
all: clean histogram_fig.html gdpPercap_vs_lifeExp_fig.html bar_letters_vs_floats.html income_share_p10_vs_country.html

clean:
	find . -type f -name "*.html" -exec rm -f {} \;

histogram_fig.html:
	python c015_hist_char_len.py

gdpPercap_vs_lifeExp_fig.html:
	python c005_gm_scatter_gdp_vs_expected_life.py

bar_letters_vs_floats.html:
	python c050_pl_ex.py

income_share_p10_vs_country.html:
	python c051_pl_ex.py