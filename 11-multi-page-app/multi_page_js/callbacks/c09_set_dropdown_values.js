// Assuming you have already set up your layout and imported necessary modules

// Get the required DOM elements
const countryPageCountryDropdown = document.getElementById('country_page_country_dropdown');

// Define a function to set the dropdown value based on the pathname
function setDropdownValueFromPathname() {
    const pathname = window.location.pathname;
    const selectedCountry = pathname.slice(1); // Remove the leading '/'
    if (countries.includes(selectedCountry)) {
        countryPageCountryDropdown.value = selectedCountry;
    }
}

// Call the function to set the dropdown value when the page loads
setDropdownValueFromPathname();
