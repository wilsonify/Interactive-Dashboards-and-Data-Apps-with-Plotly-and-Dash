import React, { useState, useEffect } from 'react';
import './index.css';

function App() {
  const [country, setCountry] = useState('');
  const [population, setPopulation] = useState('');

  useEffect(() => {
    // Simulate fetching data from an API or other data source
    // You can replace this with actual data fetching logic
    const fetchData = async () => {
      if (country) {
        const response = await fetch(`./populationData.json`);
        const data = await response.json();
        setPopulation(data.population);
      }
    };

    fetchData();
  }, [country]);

  const handleCountryChange = (event) => {
    setCountry(event.target.value);
  };

  return (
    <div>
      <h1>Poverty And Equity Database</h1>
      <h2>The World Bank</h2>
      <select id="country" name="country" onChange={handleCountryChange}>
        <option value="">Select a country</option>
        <option value="Afghanistan">Afghanistan</option>
        <option value="Albania">Albania</option>
        <option value="Algeria">Algeria</option>
        {/* Add more country options here */}
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
            Source: <a href="https://datacatalog.worldbank.org/dataset/poverty-and-equity-database">https://datacatalog.worldbank.org/dataset/poverty-and-equity-database</a>
          </li>
        </ul>
        <ul>
          <li>Book title: Interactive Dashboards and Data Apps with Plotly and Dash</li>
          <li>
            GitHub repo: <a href="https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash">https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash</a>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default App;
