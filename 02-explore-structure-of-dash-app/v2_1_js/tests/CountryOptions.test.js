
import { computeCountryOptionsUnique } from '../src/components/CountryOptions.js';



describe('CountryOptions', () => {
  it('renders the expected options', async () => {
    // Assuming that `povertyData` is your JSON data
    const povertyData = { 'Country Name': ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina'] };
    const countryOptionsUnique = computeCountryOptionsUnique(povertyData);
    console.log(countryOptionsUnique);
  });
});
