import React, { Component } from 'react';
import { Dropdown, Tabs, Tab, H1, H2, Ul, Li, A } from 'dash-react';
import countryOptions from './v2_1/read/country_options'; // Import your country options

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedCountry: null,
      report: null,
    };
  }

  handleCountryChange = (selectedCountry) => {
    // Handle the selected country change here
    this.setState({ selectedCountry });
    // You can also fetch and update the report here based on the selected country
  };

  render() {
    return (
      <div>
        <H1>Poverty And Equity Database</H1>
        <H2>The World Bank</H2>
        <Dropdown
          id="country"
          options={countryOptions}
          value={this.state.selectedCountry}
          onChange={this.handleCountryChange}
        />
        <br />
        <div id="report">
          {this.state.report}
        </div>
        <br />
        <Tabs>
          <Tab label="Key Facts">
            <Ul>
              <Li>Number of Economies: 170</Li>
              <Li>Temporal Coverage: 1974 - 2019</Li>
              <Li>Update Frequency: Quarterly</Li>
              <Li>Last Updated: March 18, 2020</Li>
              <Li>
                Source: <A href="https://datacatalog.worldbank.org/dataset/poverty-and-equity-database">https://datacatalog.worldbank.org/dataset/poverty-and-equity-database</A>
              </Li>
            </Ul>
          </Tab>
          <Tab label="Project Info">
            <Ul>
              <Li>Book title: Interactive Dashboards and Data Apps with Plotly and Dash</Li>
              <Li>
                GitHub repo: <A href="https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash">https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash</A>
              </Li>
            </Ul>
          </Tab>
        </Tabs>
      </div>
    );
  }
}

export default App;
