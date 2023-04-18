/* eslint-disable react/jsx-props-no-spreading */
import React from 'react';
import {
  Box,
  Container,
  Header,
  LineChart,
} from '@cloudscape-design/components';
import {
  commonChartProps,
  networkTrafficSeries,
  dateTimeFormatter,
  lineChartInstructions,
  networkTrafficDomain,
} from './chart-data';

export const EmissionsLineChart = () => {
  return (
    <Box margin="xxl" padding={{ vertical: '', horizontal: 'l' }}>
      <Container
        className="custom-dashboard-container"
        header={
          <Header
            variant="h2"
            description="Incoming and outgoing network traffic. Sample Data for example of component use)."
          >
            Network traffic
          </Header>
        }
      >
        <LineChart
          {...commonChartProps}
          height={220}
          series={networkTrafficSeries}
          yDomain={[0, 200000]}
          xDomain={networkTrafficDomain}
          xScaleType="time"
          xTitle="Time (UTC)"
          yTitle="Data transferred"
          ariaLabel="Network traffic"
          ariaDescription={`Line chart showing transferred data of all your instances. ${lineChartInstructions}`}
          i18nStrings={{
            ...commonChartProps.i18nStrings,
            filterLabel: 'Filter displayed instances',
            filterPlaceholder: 'Filter instances',
            xTickFormatter: dateTimeFormatter,
          }}
        />
      </Container>
    </Box>
  );
};
