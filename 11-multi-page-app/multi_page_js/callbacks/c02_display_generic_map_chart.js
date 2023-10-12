// Define a function to update the chart and details
function displayGenericMapChart(indicator) {
    if (indicator === null) {
        throw new Error('PreventUpdate');
    }

    // Select the container element for the chart
    const chartContainer = document.getElementById('indicator_map_chart');

    // Select the container element for the details
    const detailsContainer = document.getElementById('indicator_map_details_md');

    // Fetch data and create the chart using Plotly
    fetch('/path/to/data/endpoint') // Replace with the actual data endpoint
        .then(response => response.json())
        .then(data => {
            const fig = createMapChart(data, indicator);
            Plotly.newPlot(chartContainer, fig);

            // Fetch and set the details
            fetch('/path/to/details/endpoint') // Replace with the actual details endpoint
                .then(response => response.json())
                .then(details => {
                    if (details.isEmpty) {
                        detailsContainer.innerHTML = "No details available on this indicator";
                    } else {
                        const markdown = generateMarkdown(details, indicator);
                        detailsContainer.innerHTML = markdown;
                    }
                });
        })
        .catch(error => console.error(error));
}

// Call the function when the dropdown value changes
document.getElementById('indicator_dropdown').addEventListener('change', function () {
    const indicator = this.value;
    displayGenericMapChart(indicator);
});

// Initial call to populate the chart and details based on the initial value of the dropdown
displayGenericMapChart(initialIndicator); // Replace 'initialIndicator' with the actual initial value
