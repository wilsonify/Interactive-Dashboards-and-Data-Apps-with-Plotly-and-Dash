// Assuming you have already set up your layout and imported necessary modules

// Get the required DOM elements
const giniCountryDropdown = document.getElementById('gini_country_dropdown');
const giniCountryBarchart = document.getElementById('gini_country_barchart');

// Define a function to update the bar chart
function plotGiniCountryBarchart(selectedCountries) {
    if (selectedCountries.length === 0) {
        throw new Error('PreventUpdate');
    }

    // Fetch data for the selected countries (replace with your actual data retrieval)
    fetch(`/data_endpoint?countries=${selectedCountries.join(',')}`) // Replace with the actual data endpoint
        .then(response => response.json())
        .then(data => {
            const fig = createBarchart(data, selectedCountries);
            Plotly.newPlot(giniCountryBarchart, fig);
        })
        .catch(error => console.error(error));
}

// Add an event listener to the dropdown to trigger the function when the value changes
giniCountryDropdown.addEventListener('change', function () {
    const selectedCountries = Array.from(this.selectedOptions, option => option.value);
    plotGiniCountryBarchart(selectedCountries);
});

// Initial call to populate the chart based on the initial values in the dropdown
const initialCountries = Array.from(giniCountryDropdown.selectedOptions, option => option.value); // Replace with the actual initial values
plotGiniCountryBarchart(initialCountries);
