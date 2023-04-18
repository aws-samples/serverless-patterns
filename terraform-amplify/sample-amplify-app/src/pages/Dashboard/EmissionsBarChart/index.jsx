/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import {
  Box,
  BarChart,
  Container,
  Header,
} from '@cloudscape-design/components';
import {
  commonChartProps,
  cpuSeries,
  cpuDomain,
  dateFormatter,
  barChartInstructions,
} from './chart-data';

export const EmissionsBarChart = () => {
  return (
    <Box margin="xxl" padding={{ vertical: '', horizontal: 'l' }}>
      <Container
        className="custom-dashboard-container"
        header={
          <Header
            variant="h2"
            description="Daily instance hours by instance type"
          >
            Instance hours
          </Header>
        }
      >
        <BarChart
          {...commonChartProps}
          height={220}
          yDomain={[0, 2000]}
          xDomain={cpuDomain}
          xScaleType="categorical"
          stackedBars
          series={cpuSeries}
          xTitle="Date"
          yTitle="Total instance hours"
          ariaLabel="Intance hours"
          ariaDescription={`Bar chart showing total instance hours per instance type over the last 15 days. ${barChartInstructions}`}
          i18nStrings={{
            ...commonChartProps.i18nStrings,
            filterLabel: 'Filter displayed instance types',
            filterPlaceholder: 'Filter instance types',
            xTickFormatter: dateFormatter,
          }}
        />
      </Container>
    </Box>
  );
};
