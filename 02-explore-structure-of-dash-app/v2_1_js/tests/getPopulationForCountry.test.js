
const getPopulationForCountry = require('../src/components/getPopulationForCountry');


describe('getPopulationForCountry', () => {
  it('renders the expected population', async () => {
    // Assuming that `povertyData` is your JSON data
    const povertyData = {
     'Country Name': ['Afghanistan', 'Albania', 'Algeria', 'Algeria', 'Angola', 'Argentina'],
     'Indicator Name': ['Population, total','Population, total','other','Population, total','Population, total','Population, total']
     "2010": [1, 2, 3, 4, 5],
     };
    var result = getPopulationForCountry(povertyData, "Algeria", "2010");
    console.log("result = " + result);
    const expectedResult = 4;
    expect(result).toEqual(expectedResult); // Use Jest's expect function to make the assertion

  });
});
