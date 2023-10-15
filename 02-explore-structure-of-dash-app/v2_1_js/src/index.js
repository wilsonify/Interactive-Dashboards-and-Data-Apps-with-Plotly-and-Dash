const dash = require('dash');
const dbc = require('dash-bootstrap-components');
const displayCountryReport = require('./v2_1/callbacks/display_country_report');
const primaryLayout = require('./v2_1/layouts/primary');

assert(displayCountryReport);
const app = dash.Dash({
  external_stylesheets: [dbc.themes.BOOTSTRAP],
});

app.layout = primaryLayout;

if (require.main === module) {
  app.run_server({ debug: true });
}
