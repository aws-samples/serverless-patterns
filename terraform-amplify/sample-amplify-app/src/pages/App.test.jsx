// Render allows rending of components and screen allows inspection/test of components
import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import '@testing-library/jest-dom';
// import { MemoryRouter } from 'react-router-dom';

import App from './App';

// Test suite
describe('App', () => {
  // Test
  it('Renders hello world', () => {
    // ARRANGE - Get test set up
    render(<App />);
    // ACT - Perform actions that user would do with the component
    // EXPECT - Check that after user interacts with page, we have the expected outcome
    expect(
      screen.getByRole('heading', {
        level: 1,
      })
    ).toHaveTextContent('Hello World');
  });
  // it('Renders not found if invalid path', () => {
  //   render(
  //   <MemoryRouter initialEntries={['/naruto']}>
  //     <App />
  //   </MemoryRouter>
  //   )
  // })
});
