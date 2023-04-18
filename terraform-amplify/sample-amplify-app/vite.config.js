/* eslint-disable import/no-extraneous-dependencies */

// <reference types="vitest" />
// <reference types="vite/client" />

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  base: '',
  build: {
    outDir: './build', // specifies the out directory as build to match react-app specs
  },
  plugins: [react()],
  resolve: {
    alias: {
      './runtimeConfig': './runtimeConfig.browser', // <-- addresses child_process missing issue
    },

    build: {
      rollupOptions: {
        external: ['child_process'], // builds child_process externally
      },
    },
  },
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/setupTests.js'],
  },
  server: {
    port: 8080,
  },
});
