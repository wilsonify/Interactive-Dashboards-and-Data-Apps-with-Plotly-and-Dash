// Assuming you have already set up your layout and imported necessary modules

// Get the required DOM elements
const histMultiYearSelector = document.getElementById('hist_multi_year_selector');
const histIndicatorDropdown = document.getElementById('hist_indicator_dropdown');
const histBinsSlider = document.getElementById('hist_bins_slider');
const indicatorYearHistogram = document.getElementById('indicator_year_histogram');
const tableHistogramOutput = document.getElementById('table_histogram_output');

// Define a function to update the histogram and data table
function displayHistogram(selectedYears, selectedIndicator, selectedNbins) {
    if (!selectedYears || !selectedIndicator) {
        throw new Error('PreventUpdate');
    }

    // Fetch data for the selected years (replace with your actual data retrieval)
    fetch(`/data_endpoint?years=${selectedYears.join(',')}&indicator=${selectedIndicator}`) // Replace with the actual data endpoint
        .then(response => response.json())
        .then(data => {
            const fig = createHistogram(data, selectedIndicator, selectedNbins);
            Plotly.newPlot(indicatorYearHistogram, fig);

            // Create and update the data table using DataTables
            if ($.fn.dataTable.isDataTable('#data-table')) {
                $('#data-table').DataTable().destroy();
            }
            const dataTable = $('#data-table').DataTable({
                data: data,
                columns: [
                    { data: 'Country Name' },
                    { data: 'year' },
                    { data: selectedIndicator }
                ],
                paging: false,
                scrollY: '400px',
                searching: true,
                ordering: true,
                info: false,
                responsive: true,
                columnDefs: [
                    {
                        targets: [0, 1, 2],
                        render: $.fn.dataTable.render.ellipsis(10),
                    },
                ],
            });
        })
        .catch(error => console.error(error));
}

// Add event listeners to the form elements to trigger the function when values change
histMultiYearSelector.addEventListener('change', function () {
    const selectedYears = Array.from(this.selectedOptions, option => option.value);
    const selectedIndicator = histIndicatorDropdown.value;
    const selectedNbins = histBinsSlider.value;
    displayHistogram(selectedYears, selectedIndicator, selectedNbins);
});

histIndicatorDropdown.addEventListener('change', function () {
    const selectedYears = Array.from(histMultiYearSelector.selectedOptions, option => option.value);
    const selectedIndicator = this.value;
    const selectedNbins = histBinsSlider.value;
    displayHistogram(selectedYears, selectedIndicator, selectedNbins);
});

histBinsSlider.addEventListener('input', function () {
    const selectedYears = Array.from(histMultiYearSelector.selectedOptions, option => option.value);
    const selectedIndicator = histIndicatorDropdown.value;
    const selectedNbins = this.value;
    displayHistogram(selectedYears, selectedIndicator, selectedNbins);
});

// Initial call to populate the chart and data table based on the initial values
const initialYears = Array.from(histMultiYearSelector.selectedOptions, option => option.value); // Replace with the actual initial values
const initialIndicator = histIndicatorDropdown.value; // Replace with the actual initial value
const initialNbins = histBinsSlider.value; // Replace with the actual initial value
displayHistogram(initialYears, initialIndicator, initialNbins);
