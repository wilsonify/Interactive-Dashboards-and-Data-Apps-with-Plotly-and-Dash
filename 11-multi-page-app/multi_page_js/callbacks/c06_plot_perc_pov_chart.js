// Assuming you have already set up your layout and imported necessary modules

// Get the required DOM elements
const percPovYearSlider = document.getElementById('perc_pov_year_slider');
const percPovIndicatorSlider = document.getElementById('perc_pov_indicator_slider');
const percPovScatterChart = document.getElementById('perc_pov_scatter_chart');

// Define a function to update the scatter chart
function plotPercPovChart(selectedYear, selectedIndicator) {
    // Translate the indicator value to the corresponding column (replace with your mapping logic)
    const indicator = percPovCols[selectedIndicator];

    // Fetch data for the selected year and indicator (replace with your actual data retrieval)
    fetch(`/data_endpoint?year=${selectedYear}&indicator=${indicator}`) // Replace with the actual data endpoint
        .then(response => response.json())
        .then(data => {
            const fig = createScatterChart(data, indicator, selectedYear);
            Plotly.newPlot(percPovScatterChart, fig);
        })
        .catch(error => console.error(error));
}

// Add event listeners to the sliders to trigger the function when their values change
percPovYearSlider.addEventListener('input', function () {
    const selectedYear = this.value;
    const selectedIndicator = percPovIndicatorSlider.value;
    plotPercPovChart(selectedYear, selectedIndicator);
});

percPovIndicatorSlider.addEventListener('input', function () {
    const selectedYear = percPovYearSlider.value;
    const selectedIndicator = this.value;
    plotPercPovChart(selectedYear, selectedIndicator);
});

// Initial call to populate the chart based on the initial values
const initialYear = percPovYearSlider.value; // Replace with the actual initial value
const initialIndicator = percPovIndicatorSlider.value; // Replace with the actual initial value
plotPercPovChart(initialYear, initialIndicator);
