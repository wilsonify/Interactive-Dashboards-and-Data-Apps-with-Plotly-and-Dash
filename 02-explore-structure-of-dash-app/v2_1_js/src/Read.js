import React, { Component } from 'react';


class Read extends Component {
  constructor(props) {
    super(props);
    this.state = {
      countryOptions: [],
    };
  }

  async componentDidMount() {
    // Simulate loading data
    try {
      const response = await fetch('./populationData.json'); // Adjust the path as needed
      const data = await response.json();

      // Extract unique country names
      const countryNames = Array.from(new Set(data['Country Name']));

      // Create country options
      const countryOptions = countryNames.map((country) => ({
        label: country,
        value: country,
      }));

      this.setState({ countryOptions });
    } catch (error) {
      console.error('Error loading data:', error);
    }
  }

  render() {
    return (
      <div>
        <h1>Data Loaded Successfully</h1>
        {/* You can render the country options or other components as needed */}
      </div>
    );
  }
}

export default Read;
