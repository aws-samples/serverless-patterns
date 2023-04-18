# ⚛️ Components - Common
This directory contains the main components that are shared between all components in the app.
### `FetchUserDetails`
- This component fetches the attributes for the Amplify user currently signed in and passes the data as props to the relevant components.
### `Helptools`
- This component is a template for a standard help section in the application. Currently each page has it's own specific help tools content, defined in the `ToolsContent` functional component in the `index.jsx` file for each page. You can however bypass this, and have a common HelpTools content on each page if you wish.
### `Sidebar`
- This component is a the main navigation for the application
### `TopNavigationHeader`
- This component is a the Top Navigation Header for the application
