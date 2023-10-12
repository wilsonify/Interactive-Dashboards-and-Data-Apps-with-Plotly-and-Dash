// Assuming you have already set up your layout and imported necessary modules

// Get the required DOM elements
const mainContent = document.getElementById('main-content');
const location = document.getElementById('location');

// Define a function to update the main content
function displayContent() {
    const pathname = decodeURIComponent(window.location.pathname);

    if (countries.includes(pathname.substring(1))) {
        mainContent.innerHTML = countryDashboard; // Assume you have defined countryDashboard
    } else {
        mainContent.innerHTML = indicatorsDashboard; // Assume you have defined indicatorsDashboard
    }
}

// Add an event listener to trigger the function when the location changes
location.addEventListener('change', displayContent);

// Call the function on page load
displayContent();
