import React, { useState, useEffect } from 'react';
import './index.css';
const computeCountryOptionsUnique = require('./components/CountryOptions');
const getPopulationForCountry = require('../src/components/getPopulationForCountry');

function App() {
  const [country, setCountry] = useState('');
  const [population, setPopulation] = useState('');
  const [countryOptions, setCountryOptions] = useState([]);

  useEffect(() => {
    // Fetch data from PovStatsData.json
    fetch('./PovStatsData.json')
      .then((response) => response.json())
      .then((data) => {
        const options = computeCountryOptionsUnique(data);
        setCountryOptions(options);

      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const handleCountryChange = (event) => {
    setCountry(event.target.value);
    fetch('./PovStatsData.json')
      .then((response) => response.json())
        .then((data) => {
          console.log(event.target.value);
          const selectedPopulation = getPopulationForCountry(data, event.target.value, "2010");
          console.log("selectedPopulation="+selectedPopulation);
          setPopulation(selectedPopulation);
        })
    };

  return (
    <div>
      <h1>Poverty And Equity Database</h1>
      <h2>The World Bank</h2>
      <select id="country" name="country" onChange={handleCountryChange}>
        <option value="">Select a country</option>
        {countryOptions.map((option) => (
          <option key={option.key} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      <br />
      <div id="report">
        {country && (
          <div>
            <h3>{country}</h3>
            <p>{`The population of ${country} in 2010 was ${population.toLocaleString()}.`}</p>
          </div>
        )}
      </div>
      <br />
      <div>
        <ul>
          <li>Number of Economies: 170</li>
          <li>Temporal Coverage: 1974 - 2019</li>
          <li>Update Frequency: Quarterly</li>
          <li>Last Updated: March 18, 2020</li>
          <li>
            Source: <a href="https://datacatalog.worldbank.org/dataset/poverty-and-equity-database">worldbank.org</a>
          </li>
        </ul>
        <ul>
          <li>Book title: Interactive Dashboards and Data Apps with Plotly and Dash</li>
          <li>
            GitHub repo: <a href="https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash">PacktPublishing</a>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default App;
