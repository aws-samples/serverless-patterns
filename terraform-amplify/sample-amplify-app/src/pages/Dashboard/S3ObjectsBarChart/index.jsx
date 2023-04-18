/* eslint-disable no-console */
/* eslint-disable react/prop-types */
/* eslint-disable no-unused-vars */
/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import {
  Box,
  BarChart,
  Container,
  Header,
} from '@cloudscape-design/components';

export const EmissionsBarChart = ({ s3ObjectsMonthlyTotal }) => {
  const s3ObjectsMonthlyTotalProp = { s3ObjectsMonthlyTotal };
  console.log('s3ObjectsMonthlyTotal', s3ObjectsMonthlyTotal);
  console.log('s3ObjectsMonthlyTotalProp', s3ObjectsMonthlyTotalProp);

  // Can separate this in additional 'chart-data.jsx' file if you wish
  const percentageFormatter = (value) => `${(value * 100).toFixed(0)}%`;

  const numberTickFormatter = (value) => {
    if (Math.abs(value) < 1000) {
      return value.toString();
    }
    return `${(value / 1000).toFixed()}k`;
  };

  const dateTimeFormatter = (date) =>
    date
      .toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: false,
      })
      .split(',')
      .join('\n');

  const dateFormatter = (date) =>
    date
      .toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        hour12: false,
      })
      .split(' ')
      .join('\n');

  const commonChartProps = {
    loadingText: 'Loading chart',
    errorText: 'Error loading data.',
    recoveryText: 'Retry',
    empty: (
      <Box textAlign="center" color="inherit">
        <b>No data available</b>
        <Box variant="p" color="inherit">
          There is no data available
        </Box>
      </Box>
    ),
    noMatch: (
      <Box textAlign="center" color="inherit">
        <b>No matching data</b>
        <Box variant="p" color="inherit">
          There is no matching data to display
        </Box>
      </Box>
    ),
    i18nStrings: {
      filterLabel: 'Filter displayed data',
      filterPlaceholder: 'Filter data',
      filterSelectedAriaLabel: 'selected',
      legendAriaLabel: 'Legend',
      chartAriaRoleDescription: 'line chart',
      xAxisAriaRoleDescription: 'x axis',
      yAxisAriaRoleDescription: 'y axis',
      yTickFormatter: numberTickFormatter,
    },
  };

  const barChartInstructions =
    'Use left/right arrow keys to navigate between data groups.';

  const s3ObjectData = [
    {
      date: new Date('2020-1-31'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.jan.dataSizeMB,
    },
    {
      date: new Date('2020-2-28'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.feb.dataSizeMB,
    },
    {
      date: new Date('2020-3-31'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.march.dataSizeMB,
    },
    {
      date: new Date('2020-4-30'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.april.dataSizeMB,
    },
    {
      date: new Date('2020-5-31'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.may.dataSizeMB,
    },
    {
      date: new Date('2020-6-30'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.june.dataSizeMB,
    },
    {
      date: new Date('2020-7-31'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.july.dataSizeMB,
    },
    {
      date: new Date('2020-8-31'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.aug.dataSizeMB,
    },
    {
      date: new Date('2020, 9-30'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.sept.dataSizeMB,
    },
    {
      date: new Date('2020, 10-31'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.oct.dataSizeMB,
    },
    {
      date: new Date('2020, 11-30'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.nov.dataSizeMB,
    },
    {
      date: new Date('2020, 12-31'),
      dataSizeMB:
        s3ObjectsMonthlyTotalProp.s3ObjectsMonthlyTotal.dec.dataSizeMB,
    },
  ];

  const cpuDomain = s3ObjectData.map(({ date }) => date);

  const s3ObjectSeries = [
    {
      title: 'Data Size (MB)',
      type: 'bar',
      data: s3ObjectData.map((datum) => ({
        x: datum.date,
        y: datum.dataSizeMB,
      })),
    },

    // Additional properties for filtering. Must be present in your JSON data

    // {
    //   title: 'N2O',
    //   type: 'bar',
    //   data: s3ObjectData.map((datum) => ({ x: datum.date, y: datum.N2O })),
    // },
    // {
    //   title: 'CH4',
    //   type: 'bar',
    //   data: s3ObjectData.map((datum) => ({ x: datum.date, y: datum.CH4 })),
    // },
    // {
    //   title: 'CO2',
    //   type: 'bar',
    //   data: s3ObjectData.map((datum) => ({ x: datum.date, y: datum.CO2 })),
    // },
  ];

  return (
    <Box margin="xxl" padding={{ vertical: '', horizontal: 'l' }}>
      <Container
        className="custom-dashboard-container"
        header={
          <Header
            variant="h2"
            description="S3 Object metrics from the past year. (Real data fetched from from your DynamoDB table)."
          >
            Yearly S3 Object Metrics
          </Header>
        }
      >
        <BarChart
          {...commonChartProps}
          height={220}
          // Change 100 to maximum desired number
          yDomain={[0, 100]}
          xDomain={cpuDomain}
          xScaleType="categorical"
          stackedBars
          series={s3ObjectSeries}
          xTitle="Month"
          yTitle="S3 Data (MB)"
          ariaLabel="S3 Data (MB)"
          ariaDescription={`Bar chart showing total S3 Data for each month over the last year. ${barChartInstructions}`}
          i18nStrings={{
            ...commonChartProps.i18nStrings,
            filterLabel: 'Filter displayed S3 Object properties',
            filterPlaceholder: 'Filter S3 Object properties',
            xTickFormatter: dateFormatter,
          }}
        />
      </Container>
    </Box>
  );
};
