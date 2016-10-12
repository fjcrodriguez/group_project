import citydata as cty
import trulia as trl
import rent_com as rntcm
import rentHomefinder as rhf
import saleHomefinder as shf
import pandas as pd

homefinder_rent = rhf.parseHN()
homefinder_sale = shf.parseHN()
rentcom_rent = rntcm.rentcomData()
trulia_sale = trl.getSalesData()

median_incomes = cty.getMedianIncomes()

# consollidate date
housing_data = homefinder_rent + homefinder_sale + rentcom_rent + trulia_sale

# convert to pandas dataframe for easy aggregation
housing_data = pd.DataFrame.from_records(housing_data)

averages = housing_data.groupby(['City', 'Bed', 'Type'])['Price'].mean()

#find the ratios


