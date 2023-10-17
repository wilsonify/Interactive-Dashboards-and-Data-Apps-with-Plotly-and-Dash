function computeCountryOptionsUnique(data) {
  const uniqueCountries = Array.from(new Set(data['Country Name']));
  return uniqueCountries.map((country) => ({ label: country, value: country }));
}

module.exports = computeCountryOptionsUnique;