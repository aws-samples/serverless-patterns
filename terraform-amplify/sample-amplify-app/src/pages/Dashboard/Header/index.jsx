// /* eslint-disable react/no-unescaped-entities */
// /* eslint-disable react/prop-types */
// /* eslint-disable react/destructuring-assignment */
// import React from 'react';
// import {
//   HelpPanel,
//   Icon,
//   Button,
//   Header,
//   Box,
// } from '@cloudscape-design/components';
// import {
//   ExternalLinkItem,
//   InfoLink,
// } from '../../../common/common-components-config';

// export function EC2Info() {
//   return (
//     <HelpPanel
//       header={<h2>Service</h2>}
//       footer={
//         <>
//           <h3>
//             Learn more{' '}
//             <span role="img" aria-label="Icon external Link">
//               <Icon name="external" />
//             </span>
//           </h3>
//           <ul>
//             <li>
//               <ExternalLinkItem
//                 href="#"
//                 text="User Guide for Linux Instances"
//               />
//             </li>
//             <li>
//               <ExternalLinkItem
//                 href="#"
//                 text="User Guide for Windows Instances"
//               />
//             </li>
//             <li>
//               <ExternalLinkItem href="#" text="API Reference" />
//             </li>
//             <li>
//               <ExternalLinkItem
//                 href="#"
//                 text="EC2 section of the AWS CLI Reference"
//               />
//             </li>
//             <li>
//               <ExternalLinkItem
//                 href="#"
//                 text="EC2 Instance Connect API Reference"
//               />
//             </li>
//           </ul>
//         </>
//       }
//     >
//       <p>
//         Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides
//         resizeable computing capacity&mdash;literally, servers in Amazon's data
//         centers&mdash;that you use to build and host your software systems.
//       </p>
//     </HelpPanel>
//   );
// }

// export function DashboardHeader(props) {
//   return (
//     <Box padding={{ vertical: 'xl', horizontal: 'xxxl' }}>
//       <Header
//         variant="h1"
//         info={
//           <InfoLink
//             onFollow={() => props.loadHelpPanelContent(<EC2Info />)}
//             ariaLabel="Information about service dashboard."
//           />
//         }
//         actions={<Button variant="primary">Launch instance</Button>}
//       >
//         Dashboard
//       </Header>
//     </Box>
//   );
// }
