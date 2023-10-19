function getPopulationForCountry(data, selectedCountry, selectedYear) {
  const countryNames = data['Country Name'];
  const indicatorNames = data['Indicator Name'];

  if (countryNames && indicatorNames) {
    const countryIndices = countryNames.reduce((indices, country, index) => {
      if (country === selectedCountry) {
        indices.push(index);
      }
      return indices;
    }, []);

    const populationIndex = indicatorNames.indexOf('Population, total');
    if (populationIndex !== -1) {
      for (const countryIndex of countryIndices) {
        if (indicatorNames[countryIndex] === 'Population, total' && data[selectedYear][countryIndex] !== null) {
          const population = data[selectedYear][countryIndex];
          return population;
        }
      }
    }
  }

  return null; // Country, indicator, or data not found
}

module.exports = getPopulationForCountry;
