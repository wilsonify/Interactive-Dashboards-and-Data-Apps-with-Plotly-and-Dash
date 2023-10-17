
const computeCountryOptionsUnique = require('../src/components/CountryOptions');


describe('CountryOptions', () => {
  it('renders the expected options', async () => {
    // Assuming that `povertyData` is your JSON data
    const povertyData = {
     'Country Name': ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina']
     };
    var countryOptionsUnique = computeCountryOptionsUnique(povertyData);
    console.log(countryOptionsUnique);

    const expectedOptions = [
      { label: 'Afghanistan', value: 'Afghanistan' },
      { label: 'Albania', value: 'Albania' },
      { label: 'Algeria', value: 'Algeria' },
      { label: 'Angola', value: 'Angola' },
      { label: 'Argentina', value: 'Argentina' },
    ];

    // Use Jest's expect function to make the assertion
    expect(countryOptionsUnique).toEqual(expectedOptions);

  });
});
