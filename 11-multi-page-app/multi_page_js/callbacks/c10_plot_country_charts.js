// Get the required DOM elements
const countryHeading = document.getElementById('country_heading');
const countryPageGraph = document.getElementById('country_page_graph');
const countryTable = document.getElementById('country_table');
const countryPageCountryDropdown = document.getElementById('country_page_country_dropdown');
const countryPageIndicatorDropdown = document.getElementById('country_page_indicator_dropdown');

// Define a function to update the page content
function updateCountryPageContent(pathname, selectedCountries, selectedIndicator) {
    let country = 'unknown';

    if (!selectedCountries || !selectedIndicator) {
        return;
    }

    // Check if the pathname corresponds to the selected country
    if (selectedCountries.includes(pathname)) {
        country = pathname;
    }

    // Fetch and process data (replace with your data retrieval and processing logic)
    fetch(`/data_endpoint?country=${country}&indicator=${selectedIndicator}`)
        .then(response => response.json())
        .then(data => {
            // Create or update the graph and table using Plotly.js or other chart libraries
            const fig = createGraph(data, selectedIndicator, selectedCountries);
            Plotly.newPlot(countryPageGraph, fig);

            // Update the heading
            countryHeading.innerHTML = `${country} Poverty Data`;

            // Create or update the table
            const table = createTable(data);
            countryTable.innerHTML = '';
            countryTable.appendChild(table);
        })
        .catch(error => console.error(error));
}

// Add event listeners to the dropdowns to trigger the function when values change
countryPageCountryDropdown.addEventListener('change', function () {
    const selectedCountries = Array.from(this.selectedOptions, option => option.value);
    const selectedIndicator = countryPageIndicatorDropdown.value;
    const pathname = window.location.pathname.slice(1); // Get the pathname
    updateCountryPageContent(pathname, selectedCountries, selectedIndicator);
});

countryPageIndicatorDropdown.addEventListener('change', function () {
    const selectedCountries = Array.from(countryPageCountryDropdown.selectedOptions, option => option.value);
    const selectedIndicator = this.value;
    const pathname = window.location.pathname.slice(1); // Get the pathname
    updateCountryPageContent(pathname, selectedCountries, selectedIndicator);
});

// Initial call to populate the page content based on the initial values
const initialCountries = Array.from(countryPageCountryDropdown.selectedOptions, option => option.value);
const initialIndicator = countryPageIndicatorDropdown.value;
const initialPathname = window.location.pathname.slice(1); // Get the initial pathname
updateCountryPageContent(initialPathname, initialCountries, initialIndicator);
