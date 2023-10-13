document.addEventListener('DOMContentLoaded', function () {
    const countrySelect = document.getElementById('country-select');
    const reportDiv = document.getElementById('report');
    const yearSelect = document.getElementById('year-select');
    const populationChartDiv = document.getElementById('population-chart');

    // Fetch the population data from the JSON file
    fetch('populationData.json')
        .then(response => response.json())
        .then(data => {
            const populationData = data;

            // Populate the country dropdown with unique country names
            const uniqueCountryNames = [...new Set(populationData['Country Name'])];
            uniqueCountryNames.forEach(countryName => {
                const option = document.createElement('option');
                option.value = countryName;
                option.textContent = countryName;
                countrySelect.appendChild(option);
            });

            // Populate the year dropdown with available years (exclude null values)
            const availableYears = Object.keys(populationData).filter(year => !isNaN(year));
            availableYears.forEach(year => {
                const option = document.createElement('option');
                option.value = year;
                option.textContent = year;
                yearSelect.appendChild(option);
            });

            // Add an event listener for country selection
            countrySelect.addEventListener('change', () => {
                const selectedCountry = countrySelect.value;
                const selectedYear = yearSelect.value;

                // Your code to generate a report and chart based on the selected country and year
                if (selectedCountry && selectedYear) {
                    // Get the population for the selected country and year
                    const population = populationData[selectedYear][uniqueCountryNames.indexOf(selectedCountry)];

                    // Display the population report
                    reportDiv.textContent = `${selectedCountry} Population in ${selectedYear}: ${population}`;
                }
            });
        })
        .catch(error => {
            console.error('Error loading population data:', error);
        });
});
