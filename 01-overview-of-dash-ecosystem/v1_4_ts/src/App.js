import React from 'react';

function App() {
  return (
    <div>
      <h1>Poverty And Equity Database</h1>
      <h2>The World Bank</h2>
      <div className="tabs">
        <div className="tab">
          <ul>
            <br />
            <li>Number of Economies: 170</li>
            <li>Temporal Coverage: 1974 - 2019</li>
            <li>Update Frequency: Quarterly</li>
            <li>Last Updated: March 18, 2020</li>
            <li>
              Source: <a href="https://datacatalog.worldbank.org/dataset/poverty-and-equity-database">https://datacatalog.worldbank.org/dataset/poverty-and-equity-database</a>
            </li>
          </ul>
        </div>
        <div className="tab">
          <ul>
            <br />
            <li>Book title: Interactive Dashboards and Data Apps with Plotly and Dash</li>
            <li>
              GitHub repo: <a href="https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash">https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default App;
