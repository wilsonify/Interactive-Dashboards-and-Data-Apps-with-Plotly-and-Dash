// Assuming you have already set up your layout and imported necessary modules

// Get the required DOM elements
const giniYearDropdown = document.getElementById('gini_year_dropdown');
const giniYearBarchart = document.getElementById('gini_year_barchart');

// Define a function to update the bar chart
function plotGiniYearBarchart(selectedYear) {
    if (!selectedYear) {
        throw new Error('PreventUpdate');
    }

    // Fetch data for the selected year (replace with your actual data retrieval)
    fetch(`/data_endpoint?year=${selectedYear}`) // Replace with the actual data endpoint
        .then(response => response.json())
        .then(data => {
            const fig = createBarchart(data, selectedYear);
            Plotly.newPlot(giniYearBarchart, fig);
        })
        .catch(error => console.error(error));
}

// Add an event listener to the dropdown to trigger the function when the value changes
giniYearDropdown.addEventListener('change', function () {
    const selectedYear = this.value;
    plotGiniYearBarchart(selectedYear);
});

// Initial call to populate the chart based on the initial value of the dropdown
const initialYear = giniYearDropdown.value; // Replace with the actual initial value
plotGiniYearBarchart(initialYear);
