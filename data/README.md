# Project Documentation

## Introduction
- **Target Audience**:  
  This project is intended for data scientists, analysts, and real estate developers who aim to analyze and predict income, population trends, and affluence in various suburbs across Victoria, Australia.
  
- **Sources**:  
  The data used in this project includes:
  - Australian Bureau of Statistics (ABS) income data for regions (`ABS_Income_including_government_allowances_by_2021_SA2_Nov_2023.csv` and `au-govt-abs-abs-data-by-region-income-asgs-sa2-2011-2019-sa2-2016.csv`).
  - Demographic data from the ABS (`33010DO002_2022_ST_AUST.xlsx`) for population and fertility.
  - Shapefile data (`SA2_2021_AUST_GDA2020.shp`) for geographic boundaries of Statistical Areas Level 2 (SA2).
  - Crime data (`https://www.crimestatistics.vic.gov.au/crime-statistics/latest-victorian-crime-data/download-data`) for crime analysis
  - Rental data: Obtained through web scraping of domain.com.au

- **Aim**:  
  The objective of this project is to clean and merge income and population data with geographic shapefiles, handle missing values using machine learning techniques, forecast population and income trends, compute affluence scores, and provide insights into future demographic and economic conditions in Victoria.

---

## Datasets: Crime, Income, Fertility (Population), Rental

1. **Years**:  
   - **Income Data**: Data spans 2011 to 2020 for personal income, including various forms of earnings such as employee income, investment income, and government allowances.
   - **Population Data**: Data includes population estimates, fertility rates, and births from 2011 to 2022.
   - **Crime data**: Data includes crime rates per 100000 people per local government area from 2015 - 2024.
   - **Rental Data**: Data includes crime rates per 100000 people per local government area from 2011 - 2024.

2. **Preprocessing**:
   - **Income Data**: Columns with more than 50% missing data were removed. Missing numeric values were imputed using Random Forest Regressor, and rows with null values were dropped.
   - **Population Data**: Missing values were imputed using median values for fertility rates in earlier years. The dataset was cleaned, and columns were renamed to reflect demographic metrics across years.
   - **Geographic Data**: Shapefile data was merged with income and population datasets using the common `Statistical Areas Level 2 2021 code`.
   - **Crime data**: Removed rows irrelevant for analysis per SA2, e.g (Justice Institutions and Immigration Facilities) and converted strings to numerical data
   - **Rental data**: Filtered for rental listings that contain price. Removed outliers (negative price, highly unlikely number of bedrooms and bathrooms, etc.). Missing coordinates were also imputed using google maps API.


3. **Feature Engineering**:
   - **Income Data**: Features related to personal income, investment income, superannuation, and government allowances were used for analysis. After cleaning, the dataset was standardized for PCA.
   - **Population Data**: Features such as population estimates, birth rates, and fertility rates across years were used to forecast future population trends.
   -  **Crime Data**: No feature engineering needed, features were adequate
   - **Rental data**: Date into number of days since January 1, 2011, days on the market, bed and bath interaction, etc, before joining with other metrics: population, distance to public transportation, distance to amenities, etc.

4. **Feature Importance**:
   - **Income Data**: Correlation analysis and Recursive Feature Elimination (RFE) were used to select significant features for income prediction, with PCA applied to reduce dimensionality.
   - **Population Data**: Population and fertility rates were key features used for time series forecasting using the ARIMA model.
   - **Crime Data**: Crime rates throughout the years were all equally important
   - **Rental data**: N/A

5. **Prediction of Future Data (Insights)**:
   - **Income Data**: Linear Regression and PCA were used to predict income trends and compute affluence scores. Forecasts for median income in different suburbs were generated, with affluence scores identifying the most affluent suburbs in Victoria.
   - **Population Data**: ARIMA forecasting predicted population growth for 2023 and 2024, with insights indicating potential future population changes for individual suburbs and the entire state of Victoria.
   - **Crime Data**: Random forest regression was used to predict crime rates for 2011 - 2014 and 2025 - 2027.
   - **Rental data**: N/A

---

## Finalized Model
**Utilized random forest**:
  - Ran hyperparameter tuning multiple times using different samples, then tried certain sets that produced higher RMSE on the full training and validation set
  - Experimented with RFE and feature selection, but resulted in worse results and since features were not too many, we decided to use all the features


---

## Affluence Score Insights

1. **Affluence Score Calculation**:  
   - The affluence score was calculated using PCA and Linear Regression, leveraging income data from 2020.
   - The top 10 suburbs with the highest affluence scores include:
     - **Carlton**
     - **Toorak**
     - **Doncaster**
     - **Box Hill**
     - **Glen Waverley - East**
   - Affluence scores were aggregated by suburb to identify the most affluent regions in Victoria.

2. **Median Income Prediction**:  
   - Median income for each suburb was predicted using Linear Regression on selected principal components from the PCA model.
   - Forecasts for years 2011, 2014, 2015, 2016, and 2017 were generated based on income data trends.

3. **Population Forecasting**:  
   - Using ARIMA, population growth was forecasted for the years 2023 and 2024. Historical data from 2011 to 2022 was used to train the model, and additional insights were generated for both individual suburbs and the overall population trends in Victoria.

---

## Additional Section (Improvements)

- **Evaluation Metrics**:  
   - **Income Data**: Model performance for income prediction was evaluated using Mean Squared Error (MSE) and R² score. PCA-based feature reduction was validated by assessing the explained variance.
   - **Population Data**: The ARIMA model can be further validated by comparing predicted and actual values for years 2021 and 2022.

- **Visualization**:  
   - Cumulative explained variance was plotted for PCA to decide the number of principal components to retain. Additional visualizations, such as heatmaps of affluence scores and population trends across suburbs, would enhance the understanding of data distribution.
   
- **Further Feature Engineering**:  
   Additional factors such as real estate prices, migration data, and socio-economic indicators could be incorporated to further improve the affluence model and population forecast. Additionally, future models can benefit from including long-term historical income and population trends to enhance predictions.

---



