import React, { Component } from 'react';

// Import necessary modules
import pandas from 'pandas-js';
import { H1 } from 'dash-react';

class Read extends Component {
  constructor(props) {
    super(props);
    this.state = {
      countryOptions: [],
    };
  }

  componentDidMount() {
    // Simulate loading data
    const data = require('../../data/PovStatsData.json'); // Adjust the path as needed

    // Extract unique country names
    const countryNames = pandas.unique(data['Country Name']);

    // Create country options
    const countryOptions = countryNames.map((country) => ({
      label: country,
      value: country,
    }));

    this.setState({ countryOptions });
  }

  render() {
    return (
      <div>
        <H1>Data Loaded Successfully</H1>
        {/* You can render the country options or other components as needed */}
      </div>
    );
  }
}

export default Read;
