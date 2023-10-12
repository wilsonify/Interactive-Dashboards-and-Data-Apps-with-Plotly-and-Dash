document.addEventListener('DOMContentLoaded', function() {
    // Get the country select element
    const countrySelect = document.getElementById('country-select');

    // Fetch the CSV file containing countries
    fetch('../data/PovStatsData.csv')
        .then(response => response.text())
        .then(data => {
            // Parse the CSV data using PapaParse
            const parsedData = Papa.parse(data, { header: true });

            // Extract country names from the parsed data
            const countries = parsedData.data.map(row => row['Country Name']);

            // Populate the country select options
            countries.forEach(country => {
                const option = document.createElement('option');
                option.value = country;
                option.text = country;
                countrySelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error loading countries:', error);
        });

    // Add an event listener to the country select
    countrySelect.addEventListener('change', function() {
        const selectedCountry = countrySelect.value;

        // Replace this logic with fetching data and updating the report div
        if (selectedCountry) {
            document.getElementById('report').innerHTML = `<h3>${selectedCountry}</h3>`;
        } else {
            document.getElementById('report').innerHTML = '';
        }
    });
});
